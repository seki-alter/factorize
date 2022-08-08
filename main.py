""" This small program takes an expression as an input,
it returns factors of the expression and the result,
expression is filtered of whitespaces,
the sequence of actions is preserved."""

import sys


def split_to_factors():
    input_expression = input("Type the expression: ")
    calc_quit(input_expression)
    input_clean = input_expression.replace(" ", "")
    expression = list(input_clean)

    word = []
    factors = []
    previous = ""
    count = len(expression)
    i = 0

    while (i < count):
        if (expression[i].isdigit()):
            if (i + 1 >= count):
                word.append(expression[i])
                factors.append(list_to_string(word))
                break
            if (expression[i + 1].isdigit()):
                word.append(expression[i])
                i += 1
            else:
                word.append(expression[i])
                factors.append(list_to_string(word))
                word.clear()
                i += 1
        else:
            factors.append(expression[i])
            i += 1

    print(f'Expression: {list_to_string(factors)}')
    print("\nFactors:")
    for f in factors:
        if (f.isdigit()):
            print(f'-{f}') if (previous == "-") else print(f'{f} ')
        previous = f
    print(f'\nResult: {eval(list_to_string(factors))}\n')

    calc_quit(input())


def list_to_string(l):
    str1 = " "
    str1 = str1.join(l)
    str2 = str1.replace(" ", "")
    return (str2)


def calc_quit(c):
    if c.lower() == "q":
        sys.exit()
    elif c == "":
        split_to_factors()


print("Warning! Works only for decimals. Enter \"q\" to quit or enter to continue.\n")
while (True):
    split_to_factors()
    calc_quit(input())