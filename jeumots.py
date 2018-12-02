a=input()
liste=[a]
while True:
    a=input("")
    if a in liste:
        print("Неправильно")
        continue
    else:
        if liste [-1][-1] == a[0]:
            liste.append(a)
            continue
        else:
            print("Неправильно")
            continue
