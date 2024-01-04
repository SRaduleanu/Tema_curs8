# def suma_numere():
#     x = int(input('x: '))
#     y = int(input('y: '))
#     suma = x + y
#     print(f'Suma lui x si y este= {suma}')
#
# suma_numere()

# def par_impar(x):
#     if x % 2 ==0:
#         par = True
#     else:
#         par = False
#     return par
# y = int(input('Numarul de verificat: '))
# if par_impar(y):
#     print(f'Este numarul {y} par? TRUE')
# else:
#     print(f'Este numarul {y} par? FALSE')

# def numar_caractere(x):
#     litere = 0
#     separatori_cuvinte = [' ','-']
#     for i in range(0,len(x)):
#         char = x[i]
#         if not (char in separatori_cuvinte):
#             litere += 1
#     return litere
# n = str(input('Introduceti numele complet: '))
# print(f'Numarul total de caractere din numele dumneavoastra este: {numar_caractere(n)}')

# def arie_dreptunghi(latime, lungime):
#     aria = float(latime) * float(lungime)
#     return aria
# a = float(input('Introduceti latimea dreptunghiului: '))
# b = float(input('Introduceti lungimea dreptunghiului: '))
# print(f'Aria dreptunghiului este: ', arie_dreptunghi(a,b))

# import math
# def arie_cerc(raza):
#     aria = math.pi * raza ** 2
#     return aria
# r = float(input('Introduceti raza cercului: '))
# print(f'Aria cercului este: ',arie_cerc(r))

# def cautare_caracter():
#     text = str(input('Introduceti textul: '))
#     char = str(input('Indroduceti caracterul: '))
#     if char in text:
#         print(True)
#     else:
#         print(False)
#
# cautare_caracter()

# def numarare_caractere(s):
#     d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
#     for c in s:
#         if c.isupper():
#             d["UPPER_CASE"] += 1
#         elif c.islower():
#             d["LOWER_CASE"] += 1
#         else:
#             pass
#     print('Textul introdus : ', s)
#     print('Numarul de caractere lower case: ', d["LOWER_CASE"])
#     print('Numarul de caractere upper case: ', d["UPPER_CASE"])
# text = str(input('Introduceti textul: '))
# numarare_caractere(text)

# def lista_nr_pozitive(lista):
#     lista_initiala = []
#     for i in range (0, len(lista)):
#         if lista[i] > 0:
#             lista_initiala.append(lista[i])
#     return lista_initiala
# lista1 = [3, 41, -2, -4, 55, -98, 10, 231]
# print(f'Lista initiala este: {lista1}')
# print(f'Lista finala este: {lista_nr_pozitive(lista1)}')

# def comparare(x, y):
#     if x > y:
#         print(f'Primul numar ({x}) este mai mare decat al doilea numar ({y}).')
#     elif y > x:
#         print(f'Al doilea numar ({y}) este mai mare decat primul numar ({x}).')
#     else:
#         print(f'Numerele sunt egale!')
#
# a = float(input('Introduceti x: '))
# b = float(input('Introduceti y: '))
# comparare(a,b)

# def verificare_nr(numar, lista):
#     existent = False
#     if numar in lista:
#         existent = True
#         print(f"Numarul nu a fost adaugat in set deoarece exista deja.")
#     else:
#         lista.append(numar)
#         print(f"Numarul '{numar}' a fost adaugat cu succes in set.")
#     return existent
# lista = [23, 5, 15, 62, 75, 34, 66]
# print(f'Lista: {lista}')
# nr = int(input('Introduceti numarul: '))
# verificare_nr(nr, lista)

# import calendar
# def zile_luna(luna, an):
#     nr_zile = calendar.monthrange(an, luna)[1]
#     print(f'Numarul de zile din luna {luna}, anul {an} este: ', nr_zile)
# luna = int(input('Introduceti luna: '))
# an = int(input('Introduceti anul: '))
# zile_luna(luna, an)

# def calculator(x,y):
#     print('Suma celor doua numere este: ', x + y)
#     print('Diferenta dintre cele doua numere este: ', x - y)
#     print('Inmultirea dintre cele doua numere este: ', x * y)
#     print('Impartirea dintre cele doua numere este:', x / y)
# a = float(input('Introduceti primul numar: '))
# b = float(input('Introduceti al doilea numar: '))
# calculator(a,b)

# def dictionar(lista):
#     dict = {i:lista.count(i) for i in lista}
#     print(dict)
# lista_numere =[2, 4, 6, 1, 2, 6, 7, 8, 9, 3, 3, 1, 5, 7]
# print(f'Lista numerelor este: {lista_numere}')
# dictionar(lista_numere)

# def maxim(a, b, c):
#     if (a >= b) and (a >= c):
#         largest = a
#     elif (b >= a) and (b >= c):
#         largest = b
#     else:
#         largest = c
#     return largest
# x = int(input('Introduceti primul numar: '))
# y = int(input('Introduceti al doilea numar: '))
# z = int(input('Introduceti al treilea numar: '))
# print(f'Cel mai mare numar este: ',maxim(x,y,z))

# def suma(numar):
#     s = sum(range(numar+1))
#     return s
# nr = int(input('Introduceti numarul: '))
# print(f'Suma numerelor pana la {nr} este: ', suma(nr))

# def dubluri(list1,list2):
#     intersectie = list(set(list1).intersection(list2))
#     return  intersectie
# lista1 = [2, 4, 5, 7, 3, 1, 9]
# lista2 = [5, 3, 8, 1, 6, 11, 32]
# print(f'Lista 1 este urmatoarea: {lista1}')
# print(f'Lista 2 este urmatoarea: {lista2}')
# print(f'Numerele comune din cele doua liste sunt: {dubluri(lista1,lista2)}')

def reducere_pret(pret, reducere):
    if reducere in range(1, 100):
        pret_final = pret * (100 - reducere) / 100
    else:
        print('Reducerea nu este corecta.')
    return pret_final
pret = float(input('Pretul este: '))
reducere = int(input('Reducerea este: '))
print(f'Pretul redus este: {reducere_pret(pret,reducere)} lei')