from matplotlib import pyplot as plt
import hybrid_modell


def simuliere(personen, befolgend, infiziert, genesen, erlaubteGruppen, infektionsRate, genesungsRate, beta2, gamma2, dauer,
              zeige_gesamt, zeige_befolgend, zeige_nichtbefolgend):

    daten = hybrid_modell.ModellDaten(personen=personen, befolgend=befolgend, infiziert=infiziert, genesen=genesen,
                             erlaubteGruppen=erlaubteGruppen, infektionsRate=infektionsRate, genesungsRate=genesungsRate,
                             beta2=beta2, gamma2=gamma2)
    modell = hybrid_modell.Modell(daten, 1000)

    plt_gesund = []
    plt_krank = []
    plt_genesen = []

    plt_nb_gesund = []
    plt_nb_krank = []
    plt_nb_genesen = []

    plt_b_gesund = []
    plt_b_krank = []
    plt_b_genesen = []

    for tag in range(dauer):
        modell.simuliere()

        plt_gesund.append(modell.gesund)
        plt_krank.append(modell.krank)
        plt_genesen.append(modell.genesen)

        plt_nb_gesund.append(modell.nb_gesund)
        plt_nb_krank.append(modell.nb_krank)
        plt_nb_genesen.append(modell.nb_genesen)

        plt_b_gesund.append(modell.b_gesund)
        plt_b_krank.append(modell.b_krank)
        plt_b_genesen.append(modell.b_genesen)

    if zeige_gesamt:
        plt.plot(plt_gesund, 'g')
        plt.plot(plt_krank, 'r')
        plt.plot(plt_genesen, 'k')

    if zeige_nichtbefolgend:
        plt.plot(plt_nb_gesund, 'g:')
        plt.plot(plt_nb_krank, 'r:')
        plt.plot(plt_nb_genesen, 'k:')

    if zeige_befolgend:
        plt.plot(plt_b_gesund, 'g--')
        plt.plot(plt_b_krank, 'r--')
        plt.plot(plt_b_genesen, 'k--')

    plt.show()

