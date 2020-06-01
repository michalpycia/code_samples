def validate_pesel():
    '''
    Program to check if PESEL is correct
    :return: True if Pesel is correct, False if not
    '''
    pesel = str(input("Podaj 11 cyfrowy pesel: "))
    while len(pesel) != 11:
        print("Zła długość pesel")
        pesel = str(input("Podaj 11 cyfrowy pesel: "))
    pesel_list = []
    for i in pesel:
        pesel_list.append(i)
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = 0

    for index, element in enumerate(pesel_list[0:10]):
        num = int(element)
        num1 = wagi[index]
        result = num * num1
        suma = result + suma
    mod = suma % 10
    if mod == 10:
        mod = 0
    control = 10 - mod
    return print(control == int(pesel_list[-1]))


    print(suma)



if __name__ == '__main__':
    validate_pesel()