"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(s):
    result = s
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    letras = []

    for i in s:
        if i == "b":
          letras.append(2)
        elif i == "d":
          letras.append(4)
        else:
          letras.append(i)

    if not letras:
      return [0]

    for i in range(len(letras)):
      if isinstance(letras[i], str) and letras[i].isalpha():
          indice = alfabeto.index(letras[i].lower()) + 1
          letras[i] = str(indice)

    return letras

r_1 = fn_hack_7(["a","b","c","d","e"])
r_2 = fn_hack_7([])

print(r_1)
print(r_2)
