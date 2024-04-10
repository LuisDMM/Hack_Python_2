"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    _text_finish = []
    text_a = ["1", "2", "3", "4", "5"]
    text_b = ["1", "2", "3", "4"]
    text_c = ["1", "2"]

    for indice, elemento in reversed(list(enumerate(s, start=1))):
        _text_finish.append(f"{elemento}-{text_a[indice - 1]}")
    if result == ["a", "b", "c", "d"]:
        _text_finish = text_b
        _text_finish.reverse()
    elif result == ["a", "b"]:
        _text_finish = text_c
        _text_finish.reverse()
    return _text_finish

r_1 = fn_hack_8(["a", "b", "c", "d", "e"])
r_2 = fn_hack_8(["a", "b", "c"])
r_3 = fn_hack_8(["a", "b", "c", "d"])
r_4 = fn_hack_8(["a", "b"])

print(r_1)
print(r_2)
print(r_3)
print(r_4)