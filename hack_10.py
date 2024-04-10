"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    contador = 1
    _ls = []

    for i in result:
        nueva_cadena = {}
        nueva_cadena[str(contador)] = str(contador + 1)
        contador += 2
        _ls.append(nueva_cadena)
    return _ls

r1 = fn_hack_10([{"a":"b"},{"c","d"},{"e":"f"}])
print(r1)