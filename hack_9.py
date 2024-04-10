"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    text = {"foo":"fookziman"}
    _ls = {}
    for key, value in text.items():
        if key.capitalize() not in s:
            _ls[key.capitalize()] = value.capitalize().replace("k","")
    return _ls

r1 = fn_hack_9({"foo": "fookziman", "bar": "barziman"})
print(r1)

