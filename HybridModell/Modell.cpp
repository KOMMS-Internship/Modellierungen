#include "Modell.h"

Modell::Modell(ModellDaten daten, int seed) : daten(daten), random(Random(seed)) 
{
	init();
}

void Modell::init()
{
	// Verteile Infizierte und Genesene gleichmäßig auf befolgende und nicht befolgende Personen
	int befolgend_infiziert = daten.befolgend * daten.infiziert / daten.personen;
	nb_infiziert = daten.infiziert - befolgend_infiziert;
	int befolgend_genesen = daten.befolgend * daten.genesen / daten.personen;
	nb_genesen = daten.genesen - befolgend_genesen;

	nb = daten.personen - daten.befolgend;
	nb_gesund = nb - nb_infiziert - nb_genesen;

	befolgend = std::vector<char>(daten.befolgend);
	for (int i = 0; i < daten.befolgend; ++i)
	{
		// Branchless Programming:
		// In C++ wird eine boolean Wert als 1 (true) oder 0 (false) verwendet
		// Ist i < befolgend_genesen, ist dieser Ausdruck 0. Für alle i < befolgend_genesen, ist der State somit 2 (GENESEN)
		// Ist befolgende_genesen <= i < befolgend_infiziert + befolgend_genesen, so ist das Ergebnis 1 (KRANK)
		// Ist i >= befolgend_infiziert + befolgend_genesen, so ist das Ergebnis 0 (GESUND)
		// Die Anzahl an genesenen, infizierte uns gesunden wird also genau eingehalten
		befolgend[i] = 2 - (i >= befolgend_genesen) - (i >= befolgend_infiziert + befolgend_genesen);
	}
}

void Modell::simuliere()
{
	if(befolgend.size() > 0)
		automat();
	if(nb > 0)
		SIR();
	countStates();
	SIR2();
}

void Modell::automat()
{
	// Mische alle Personen, die die Besachränkungen befolgen (Fisher-Yates-Shuffle)
	random.shuffle(befolgend);

	// In diesem Array werden alle infizierbaren / gesunden Personen einer Gruppe gespeichert
	char** infizierbar = new char*[daten.erlaubteGruppen];
	for (int i = 0; i < daten.erlaubteGruppen; ++i)
	{
		infizierbar[i] = nullptr;
	}

	// Anzahl der einzelnen States pro Gruppe
	int infiziert = 0, gesund = 0, gesamt = 0;

	for (int i = 0; i < befolgend.size(); ++i)
	{
		// Zähle, wie oft die einzelnen States vorkommen
		char state = befolgend[i];
		gesund += (state == GESUND);
		infiziert += (state == KRANK);
		++gesamt;
		if (befolgend[i] == GESUND)
		{
			// Füge den Gesunden dem Array hinzu
			// 1. gesunder an Index 0, 2. bei Index 1, usw. (gesund - 1)
			// &(befolgend[i]) gibt die Speicheradresse der i-ten Person aus (char*)
			infizierbar[gesund - 1] = &(befolgend[i]);
		}

		// Falls bereits die maximale Gruppengröße erreicht ist oder das die letzte Person ist
		if (gesamt == daten.erlaubteGruppen || i + 1 == befolgend.size())
		{
			// Wahrscheinlichkeit für eine Neuinfektion beta * I/N
			double p = (double)infiziert / gesamt * daten.infektionsRate;
			for (int k = 0; k < daten.erlaubteGruppen; ++k)
			{
				if (infizierbar[k] != nullptr && random.random() < p)
				{
					// Setze die Person auf KRANK. Das '*' dereferenziert den Pointer, macht also aus char* ein char,
					// welchem man den Wert KRANK zuweisen kann.
					*(infizierbar[k]) = KRANK;
				}
				// entferne die Person aus dem Array (nullptr ist ähnlich zu null in Java, C#, ... oder None in Python)
				infizierbar[k] = nullptr;
			}
			gesamt = 0; gesund = 0; infiziert = 0;
		}

		if (befolgend[i] == KRANK && random.random() < daten.genesungsRate)
		{
			befolgend[i] = GENESEN;
		}
	}

	// In C++ muss man Objekte, die mit new Erzeugt wurden, manuell löschen
	// Da es ein Array war, muss "delete[]" statt nur "delete" verwendet werden.
	delete[] infizierbar;
}

void Modell::SIR()
{
	// Wende das SIR Modell auf "nicht befolgende" (nb) Personen an
	double infiziert = daten.infektionsRate * nb_gesund * nb_infiziert / nb;
	double genesen = daten.genesungsRate * nb_infiziert;

	nb_gesund -= infiziert;
	nb_infiziert += infiziert - genesen;
	nb_genesen += genesen;
}

void Modell::SIR2()
{
	// Wende das SIR Modell erneut auf alle Personen an
	double p_infiziert = daten.beta2 * gesamt_infiziert / daten.personen;
	double p_genesen = daten.gamma2;

	double infiziert = nb_gesund * p_infiziert;
	double genesen = nb_infiziert * p_genesen;

	nb_gesund -= infiziert;
	nb_infiziert += infiziert - genesen;
	nb_genesen += genesen;

	for (int i = 0; i < befolgend.size(); ++i)
	{
		if (befolgend[i] == GESUND)
		{
			if (random.random() < p_infiziert)
			{
				befolgend[i] = KRANK;
			}
		}
		else if(befolgend[i] == KRANK)
		{
			if (random.random() < p_genesen)
			{
				befolgend[i] = GENESEN;
			}
		}
	}
}

void Modell::countStates()
{
	gesamt_gesund = nb_gesund;
	gesamt_infiziert = nb_infiziert;
	gesamt_genesen = nb_genesen;

	b_gesund = 0; b_infiziert = 0; b_genesen = 0;

	for (char c : befolgend)
	{
		gesamt_gesund    += c == GESUND;
		gesamt_infiziert += c == KRANK;
		gesamt_genesen   += c == GENESEN;

		b_gesund += c == GESUND;
		b_infiziert += c == KRANK;
		b_genesen += c == GENESEN;
	}
}
