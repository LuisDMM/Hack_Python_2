"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    letras = "f", "b", "n"
    _str = ''

    for character in s:
        if character not in letras:
            _str += character
    return _str

r_1 = fn_hack_4("fooziman")
r_2 = fn_hack_4("barziman")
r_3 = fn_hack_4("qux")

print(r_1)
print(r_2)
print(r_3)
