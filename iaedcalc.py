# IAEDcalc 1.0
# Created by Nuno Florência(ist1105865) || IST-LETI 2022/23
#
# Contacts
# Email: nuno.v.florencia@gmail.com
# GitHub: spokiris
# IG: nuno.florencia

from math import sqrt


def proj():
    while True:
        try:
            p1 = float(input("nota p1: "))
            p2 = float(input("nota p2: "))
            tp = float(input("nota TP: "))

            if 0 <= p1 <= 20 and 0 <= p2 <= 20 and 0 <= tp <= 20:
                break
            else:
                print("As notas têm de estar entre 0 e 20.")
        except ValueError:
            print("Introduza um valor numérico.")

    return min((p1 + p2) / 2, tp) + sqrt(abs((p1 + p2) / 2 - tp) / 2)


def labs():
    while True:
        try:
            labs = float(input("nota labs: "))
            if 0 <= labs <= 20:
                break
            else:
                print("A nota tem de estar entre 0 e 20.")
        except ValueError:
            print("Introduza um valor numérico.")

    return labs


def exame():
    while True:
        try:
            exa = float(input("nota exame: "))
            if 0 <= exa <= 20:
                break
            else:
                print("A nota tem de estar entre 0 e 20.")
        except ValueError:
            print("Introduza um valor numérico.")

    return exa


def calcula():
    return labs() * 0.3 + exame() * 0.3 + proj() * 0.4


def calcula_exame():
    while True:
        try:
            tg = float(input("nota final target: "))
            if 0 <= tg <= 20:
                break
            else:
                print("A nota tem de estar entre 0 e 20.")
        except ValueError:
            print("Introduza um valor numérico.")

    p = proj()
    l = labs()

    na = p * 0.4 + l * 0.3

    if na >= tg:
        print("ARDEU!!!")
        print(f"precisas de {na:.2f}")
    else:
        return (tg - na) / 0.3


def __otpt__():
    print("-enter \"h\" para exibir definicoes")

    while True:
        user_input = input("IAEDcalc> ")

        if user_input == "e":
            nota_necessaria = calcula_exame()
            if nota_necessaria is not None:
                print(f"Nota necessária no exame: {nota_necessaria:.2f}")
        elif user_input == "c":
            nota_final = calcula()
            print(f"Nota final: {nota_final:.2f}")
        elif user_input == "q":
            break
        elif user_input == "h":
            print("-enter \"e\" para calcular a nota necessária no exame\n"
                  "-enter \"c\" para calcular a nota final\n")
        else:
            print("Opção inválida.")

    return


__otpt__()
