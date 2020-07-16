#include "Modell.h"

#define EXPORT __declspec(dllexport)

extern "C"
{
	EXPORT Modell* createModell(ModellDaten daten, int seed) {
		Modell* modell = new Modell(daten, seed);
		return modell;
	}

	EXPORT void deleteModell(Modell* modell) {
		delete modell;
	}

	EXPORT void simuliere(Modell* modell) {
		modell->simuliere();
		modell->countStates();
	}

	EXPORT int getGesund(Modell* modell) {
		return modell->gesamt_gesund;
	}
	EXPORT int getKrank(Modell* modell) {
		return modell->gesamt_infiziert;
	}
	EXPORT int getGenesen(Modell* modell) {
		return modell->gesamt_genesen;
	}

	EXPORT int getGesund_b(Modell* modell) {
		return modell->b_gesund;
	}
	EXPORT int getKrank_b(Modell* modell) {
		return modell->b_infiziert;
	}
	EXPORT int getGenesen_b(Modell* modell) {
		return modell->b_genesen;
	}

	EXPORT int getGesund_nb(Modell* modell) {
		return modell->nb_gesund;
	}
	EXPORT int getKrank_nb(Modell* modell) {
		return modell->nb_infiziert;
	}
	EXPORT int getGenesen_nb(Modell* modell) {
		return modell->nb_genesen;
	}
}