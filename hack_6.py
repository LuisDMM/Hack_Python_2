"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    letras = []

    for i in range(0, len(s), 2):
        letras.extend([s[i], "-"]) 
    if letras and letras[-1] == "-":
        letras.pop() 
    if not letras:
        return ["0"]
    for i in range(len(letras)):
        if letras[i].isalpha():
            indice = alfabeto.index(letras[i].lower()) + 1
            letras[i] = str(indice)

    return letras

r_1 = fn_hack_6(["a","b","c","d","e"])
r_2 = fn_hack_6([])

print(r_1)
print(r_2)


