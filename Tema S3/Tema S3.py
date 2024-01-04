lista1 = [2, 6, 'opt', 5.55, 'Cristi', False]
print(f'Al doilea element din lista este: "{lista1[1]}"')
print(f'Indexul cifrei "2" din lista este: {lista1.index(2)}')
lista1.append("Serban")
print(f'Lista cu elementul adaugat cu append (la sfarsitul listei) este: {lista1}')
lista1.insert(4,113)
print(f'Lista cu elementul adaugat cu insert (pe pozitia 4) este: {lista1}')
lista1.pop(3)
print(f'Lista cu elementul sters cu pop (de pe pozitia 3) este: {lista1}')
lista1.remove("Cristi")
print(f'Lista cu elementul sters cu remove (cu valoarea data) este: {lista1}')
print(f'Lista mea are {len(lista1)} elemente')
print(f'Elementul "113" apare in lista de {lista1.count(113)} ori')
lista2 = [2, 90, 88, 91]
lista1.extend(lista2)
lista2.sort()
print(f'Lista2 sortata este: {lista2}')
lista2.sort(reverse=True)
print(f'Lista2 sortata este descendent: {lista2}')
lista2.clear()

tuplu1 = (2, 5, 8, 'Serban', 7, 13, 12, 99)
tuplu_gol = ()
print(f'Al 4-lea element din tuplu este: {tuplu1[3]}')
print(f'Elementul "7" are indexul {tuplu1.index(7)} in tuplu meu')
print(f'Elementul 5 apare de {tuplu1.count(5)} ori in tuplu meu')
print(f'Elementul "99" se afla la index {tuplu1.index(99)}')

set1 = {3, 2, 5, 6, 1, 1, 7, 3, 88}
set1.add(105)
print(f'Setul meu dupa adaugarea elementului "105" este: {set1}')
set1.pop()
print(f'Setul sters cu pop (primul element) este: {set1}')
set1.remove(3)
print(f'Setul sters cu remove (elementul "3") este: {set1}')
set2 = {5, 6 ,7}
print(set2.issubset(set1))
print(set2.issuperset(set1))
set3 = {5, 88, 23, 12}
print(f'Intersectia seturilor set1 si set3 este: {set1.intersection(set3)}')
print(f'Diferenta dintre set1 fata de set3 este: {set1.difference(set3)}')
set3.clear()

telefoane = {
    "brand":"Samsung",
    "model":"S23 Ultra",
    "an":2023
}
print(telefoane)
telefoane.update({'capacitate':'512Gb'})
telefoane["culoare"] = "Negru"
print(telefoane)
print(f'Modelul telefonului este: {telefoane.get("model")}')
print(f'Anul aparitiei telefonului este: {telefoane["an"]}')
telefoane.pop("capacitate")
print(telefoane)
telefoane.popitem() # sterge ultimul element adaugat
print(telefoane)
chei = telefoane.keys()
print(chei)
valori = telefoane.values()
print(valori)
iteme = telefoane.items()
print(iteme)