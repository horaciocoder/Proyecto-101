import random
dice = ["[-----]\n[     ]\n[  0  ]\n[     ]\n[-----]", "[-----]\n[ 0   ]\n[     ]\n[   0 ]\n[-----]", 
        "[-----]\n[0    ]\n[  0  ]\n[    0]\n[-----]", "[-----]\n[0   0]\n[     ]\n[0   0]\n[-----]",
        "[-----]\n[0   0]\n[  0  ]\n[0   0]\n[-----]", "[-----]\n[0   0]\n[0   0]\n[0   0]\n[-----]"]

while True:
    num = random.randint(1, 6)
    print(dice[num - 1])
    response = input("¿Quieres tirar de nuevo? Presiona 'y' para intentar de nuevo o 'n' para salir... ")
    if response == 'n':
        break