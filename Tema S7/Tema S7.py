# class SistemOperare:
#     def __init__(self,telefon):
#         self.telefon = telefon
#
# class Android(SistemOperare):
#     def so(self):
#         return "Sistemul de operare al telefonului este Android!"
#
# class iOS(SistemOperare):
#     def so(self):
#         return "Sistemul de operare al telefonului este iOS!"
#
# samsung = Android(telefon="Samsung")
# iphone = iOS(telefon="Apple iPhone")
# print(samsung.so())
# print(iphone.so())


# class XiaomiMi12:
#     def tip_telefon(self):
#         return "Acesta este un telefon cu Android"
#
# class OnePlus10:
#     def tip_telefon(self):
#         return "Acesta este un telefon cu iOS"
#
# def afiseaza_tip_telefon(telefoane):
#     print(telefoane.tip_telefon())
#
# xiaomi = XiaomiMi12()
# oneplus = OnePlus10()
#
# afiseaza_tip_telefon(xiaomi)
# afiseaza_tip_telefon(oneplus)

# from abc import ABC, abstractmethod
#
# class SistemeOperare(ABC):
#     def __init__(self, versiune, an_lansare):
#         self.versiune = versiune
#         self.an_lansare = an_lansare
#     @abstractmethod
#     def detalii(self):
#         pass
#
# class Android(SistemeOperare):
#     def detalii(self):
#         print("Versiune: ", self.versiune);
#         print("An lansare: ",self.an_lansare);
#
#     def antivirus(self):
#         print("Nu are aceasta optiune!")
#
#
# class iOS(SistemeOperare):
#     def detalii(self):
#         print("Versiune: ", self.versiune);
#         print("An lansare: ", self.an_lansare);
#
#     def antivirus(self):
#         print("Are aceasta optiune!")
#
# SamsungS21 = Android("13", "2022")
# SamsungS21.detalii()
# SamsungS21.antivirus()

class Android:
    def __init__(self, versiune, an_lansare):
        self.versiune = versiune
        self.an_lansare = an_lansare
        self.telefon = []
        self._unitatiVandute = 0
        self.__totalUnitati = 3000000
        self.discontinued = False

    def adaugare_telefon(self, telefon):
        self.telefon.append(telefon)

    def stergere_telefon(self, telefon):
        self.telefon.remove(telefon)

    def nr_unitati_vandute(self, nr_unitati_vandute):
        self._unitatiVandute += nr_unitati_vandute

    @property
    def totalUnitati(self):
        pass

    @totalUnitati.getter
    def totalUnitati(self):
        return self.__totalUnitati

    @totalUnitati.setter
    def totalUnitati(self, total_modificat):
        self.__totalUnitati += total_modificat

    @totalUnitati.deleter
    def totalUnitati(self):
        self.__totalUnitati = 0

Samsung = Android("13", "2022")
print(f'Modelul telefonului cu Android este: {Samsung.telefon}')
print(f'Numarul de unitati vandute este: {Samsung._unitatiVandute}')
#GETTER
print(f'Totalul unitatilor vandute apelate prin GETTER: {Samsung.totalUnitati}')
#SETTER
Samsung.totalUnitati = 23000
print(f'Totalul unitatilor vandute apelate prin SETTER: {Samsung.totalUnitati}')
#DELETER
del Samsung.totalUnitati
print(f'Totalul unitatilor vandute apelate prin DELETER: {Samsung.totalUnitati}')