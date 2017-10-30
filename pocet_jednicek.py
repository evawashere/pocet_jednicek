def pocet_jednicek(cislo):
    pomocny_pocet_jednicek = 0

    for i in cislo:
        if i == '1':
            pomocny_pocet_jednicek += 1
    return('Pocet jednicek v cisle {} je {}.'.format(cislo, pomocny_pocet_jednicek))


print(pocet_jednicek(input("Zadejte cislo: ")))


def pocet_jednicek_jinak(cislo):
    pocet = 0
    while cislo > 0:
        zbytek = cislo % 10
        if zbytek == 1:
            pocet += 1
        cislo = cislo // 10
    return pocet
