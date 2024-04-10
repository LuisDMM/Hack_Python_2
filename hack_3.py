"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    letras = ["f", "b", "n", "q", "x"]
    box = ''

    for character in s:
        if character not in letras:
            contenedor= character.replace("o", "0").replace("i", "¡").replace("a", "@").replace("u", "v")
        else:
            contenedor = character.replace("f", "F").replace("b", "B").replace("n", "N").replace("q", "Q").replace("x", "X")
        box += contenedor
        
    return box

r_1 = fn_hack_3("fooziman")
r_2 = fn_hack_3("barziman")
r_3 = fn_hack_3("3q")
r_4 = fn_hack_3("qu")
r_5 = fn_hack_3("qux")

print(r_1)
print(r_2)
print(r_3)
print(r_4)
print(r_5)
