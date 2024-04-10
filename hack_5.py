"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    _ls = []
    for i in s:
        if "fooziman" in s:
            nueva_cadena = s.replace("fooziman", "fo-zi-ma-")
        elif "barziman" in s:
            nueva_cadena = s.replace("barziman", "ba-zi-an")
        elif "qux" in s:
            nueva_cadena = s.replace("qux", "qu-")

        else:
            nueva_cadena = s
    
    return nueva_cadena

r_1 = fn_hack_5("fooziman")
r_2 = fn_hack_5("barziman")
r_3 = fn_hack_5("qux")
r_4 = fn_hack_5("eq")

print(r_1)
print(r_2)
print(r_3)
print(r_4)
