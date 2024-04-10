"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(s):
    result = s
    letras = "o", "i", "a","u"
    _ls = ''

    for character in s:
        if character not in letras:
            _ls += character
    return _ls

r_1 = fn_hack_2("fooziman")
r_2 = fn_hack_2("barziman")
r_3 = fn_hack_2("qux")

print(r_1)
print(r_2)
print(r_3)