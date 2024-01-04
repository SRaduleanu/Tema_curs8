# prezenti = ['Moraru Alexandru', 'Melinte Camelia', 'Dogaru Valentin', 'Pal Camelia', 'Raduleanu Serban', 'Borbey Robert', 'Runcanu Irina', 'Neamtu Gabriel', 'Ivan Cristina', 'Catrinel - Alexandra Ripeanu']
# for x in prezenti:
#     print(x)
# prezenti = ['Moraru Alexandru', 'Melinte Camelia', 'Dogaru Valentin', 'Pal Camelia', 'Raduleanu Serban', 'Borbey Robert', 'Runcanu Irina', 'Neamtu Gabriel', 'Ivan Cristina', 'Catrinel - Alexandra Ripeanu']
# i = 0
# while i<len(prezenti):
#     print(prezenti[i])
#     i+=1;
# prezenti = ['Moraru Alexandru', 'Melinte Camelia', 'Dogaru Valentin', 'Pal Camelia', 'Raduleanu Serban', 'Borbey Robert', 'Runcanu Irina', 'Neamtu Gabriel', 'Ivan Cristina', 'Catrinel - Alexandra Ripeanu']
# for i in range(len(prezenti)):
#     print(prezenti[i])

list1 = [4, 7, 1, 9, 23, 65, 3]
print(f"Lista nesortata este: {list1}")

def bubble_sort(list1):
    for i in range(0,len(list1)-1):
        for j in range(len(list1)-1):
            if (list1[j]>list1[j+1]):
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return list1

print(f'Lista sortata este: {bubble_sort(list1)}')

fotbalisti_pe_echipe = {
            "Barcelona":{
                "Dica":
                    {
                        "Nume complet":"Nicolae Dica",
                        "Varsta":45,
                        "Numar Tricou":10
                    },
                "Banel":
                    {
                        "Nume complet":"Banel Nicolita",
                        "Varsta":47,
                        "Numar Tricou":3
                    },
                "Dukadam":
                    {
                        "Nume complet":"Helmut Dukadam",
                        "Varsta":65,
                        "Numar Tricou":7
                    }
            }
}
# print(f'Numarul de pe tricoul lui Banel Nicolita este: {fotbalisti_pe_echipe["Barcelona"]["Banel"]["Numar Tricou"]}')
# fotbalisti_pe_echipe["Barcelona"].pop("Dukadam")
# print(fotbalisti_pe_echipe)


for p_id, p_info in fotbalisti_pe_echipe["Barcelona"].items():
    print(f'\nLa echipa Barcelona joaca jucatorul: ')
    for key in p_info:
        print(f'Detalii jucator - ',key + ':', p_info[key], end=',')
    print()