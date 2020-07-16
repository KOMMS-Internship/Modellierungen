#pragma once
#include "Random.h"
#include <vector>

#define GESUND 0
#define KRANK 1
#define GENESEN 2

struct ModellDaten
{
	int personen;

	int infiziert;
	int genesen;
	
	int befolgend;
	int erlaubteGruppen;

	double infektionsRate;
	double genesungsRate;

	double beta2;
	double gamma2;
};


class Modell {
public:

	Random random;
	ModellDaten daten;

	// Es werden nur die States (GESUND, KRANK, GENESEN) der Personen gespeichert,
	// welche in einen 8bit Wert (char) passen.
	std::vector<char> befolgend;

	// "nb" steht für "nicht befolgend"
	int nb;
	double nb_gesund;
	double nb_infiziert;
	double nb_genesen;

	// "b" steht für "befolgend"
	double b_gesund;
	double b_infiziert;
	double b_genesen;

	double gesamt_gesund;
	double gesamt_infiziert;
	double gesamt_genesen;

	Modell(ModellDaten daten, int seed);

	void init();

	void simuliere();
	void automat();
	void SIR();
	void SIR2();

	void countStates();
};