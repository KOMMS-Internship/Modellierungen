import ctypes
import pathlib

# load library from path
lib = ctypes.CDLL("HybridModell.dll")


class Modell:
    def __init__(self, daten, seed):
        lib.createModell.restype = ctypes.c_longlong
        # man muss nach c_longlong casten, da x64 pointer verwendet werden
        self.handle = ctypes.c_longlong(lib.createModell(daten, seed))

        self.gesund = 0
        self.krank = 0
        self.genesen = 0

        self.nb_gesund = 0
        self.nb_krank = 0
        self.nb_genesen = 0

        self.b_gesund = 0
        self.b_krank = 0
        self.b_genesen = 0


    def simuliere(self):
        lib.simuliere(self.handle)

        self.gesund = lib.getGesund(self.handle)
        self.krank = lib.getKrank(self.handle)
        self.genesen = lib.getGenesen(self.handle)

        self.nb_gesund = lib.getGesund_nb(self.handle)
        self.nb_krank = lib.getKrank_nb(self.handle)
        self.nb_genesen = lib.getGenesen_nb(self.handle)

        self.b_gesund = lib.getGesund_b(self.handle)
        self.b_krank = lib.getKrank_b(self.handle)
        self.b_genesen = lib.getGenesen_b(self.handle)

    def __del__(self):
        lib.deleteModell(self.handle)


class ModellDaten(ctypes.Structure):
    _fields_ = [("personen", ctypes.c_int),
                ("infiziert", ctypes.c_int),
                ("genesen", ctypes.c_int),
                ("befolgend", ctypes.c_int),
                ("erlaubteGruppen", ctypes.c_int),
                ("infektionsRate", ctypes.c_double),
                ("genesungsRate", ctypes.c_double),
                ("beta2", ctypes.c_double),
                ("gamma2", ctypes.c_double)]

    def __init__(self, infektionsRate=0.3, genesungsRate=0.1, beta2=0.05, gamma2=0.01, personen=1000, erlaubteGruppen=2,
                 befolgend=100, infiziert=20, genesen=0):
        self.infektionsRate = infektionsRate
        self.genesungsRate = genesungsRate
        self.personen = personen
        self.erlaubteGruppen = erlaubteGruppen
        self.befolgend = befolgend
        self.infiziert = infiziert
        self.genesen = genesen
        self.beta2 = beta2
        self.gamma2 = gamma2
