# Gestion "regarder avant de sauter"
def divide(a, b, default=None):
    if b == 0:  # situation exceptionnelle
        print("zero division detected")  # Gestion de l'erreur
        return default
    return a / b  # Situation les plus communes
    # Gestion "on essaye et on voit"


def divideExcept(a, b, default=None):
    try:
        return a / b  # situation les plus communes
    except ZeroDivisionError:  # situation exceptionnelle
        print("zero division detected")  # Gestion de l'erreur
        return default


# %%
def find(key, dictio, val=None):
    try:
        return (dictio[key])
    except KeyError:
        return (val)


def finder(key, dictio):
    if key in dictio:
        return (dictio[key])
    else:
        return None


dic = {"une": 1, "deux": 2}
find('un', dic)


def reprint():
    try:
        n = int(input("Donne le nombre khouya: "))
        return (n)
    except ValueError:
        return (reprint())


print(finder("une", dic))

# %%
import timeit

squares = {x: x ** 2 for x in range(1, 100000)}
number = "bomba"
t = timeit.timeit(lambda: find(number, squares))  # test dela fonction facon if
print(t)
t1 = timeit.timeit(lambda: finder(number, squares))  # Test dela fonction facon try
print(t1)


# %%
class Ligne():
    def __init__(self, nom, ligne, debut, fin):
        self.nom = nom
        self.debut = debut
        self.fin = fin
        self.ligne = ligne
        self.arrets = []
        self.Trag = []

    def Horaire(self, heure):
        longtraj = 0
        for i in range(len(self.Trag) - 1):
            longtraj = longtraj + self.Trag[0]

        heure = self.debut
        while heure + longtraj <= self.fin:

            # parcour louleni men A lel B
            print("station", self.arrets[0], self.debut, "direction A")
            for i in range(len(self.Trag) - 1):
                heure = heure + self.Trag[i]
                print("station", self.arrets[i + 1], heure, "direction A")

            # parcour theni mel B lel A
            print(("station: ", self.arrets[len(self.Trag) - 1], heure, "direction B"))
            for i in range(len(self.Trag), 0, -1):
                heure = heure + self.Trag[i]
                print("station: ", self.arrets[i + 1], heure, "direction B")

        print("chama3na, ahbtou naykou 3la zebi")


class Metro(Ligne):
    def __init__(self):
        Ligne.__init__(self)


class Bus(Ligne):
    def __init__(self, essence):
        self.essence = essence


class Tram(Ligne):
    def __init__(self):
        Ligne.__init__(self)