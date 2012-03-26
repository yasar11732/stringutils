from string import (letters, digits, punctuation,
                    whitespace, lowercase, uppercase,
                    hexdigits, octdigits, printable)
from itertools import groupby
from os import name as osname

if osname == "nt":
    newline = "\r\n"
else:
    newline = "\n"

isSomething = lambda thing: lambda x: x in thing
allSomething = lambda thing: lambda string : all(thing(x) for x in string)
anySomething = lambda thing: lambda string : any(thing(x) for x in string)
removeSomething = lambda thing: lambda string: "".join(x for x in string
                                                       if not thing(x))
onlySomething = lambda thing: lambda string: "".join(x for x in string
                                                     if thing(x))
func_dic = {
        "Letter" : letters,
        "Digit" : digits,
        "Alphanum" : letters + digits,
        "Punctuation" : punctuation,
        "Whitespace" : whitespace,
        "Lower" : lowercase,
        "Upper" : uppercase,
        "Hex" : hexdigits,
        "Octal" : octdigits,
        "Printable" : printable,
    }
cat_order = ["Whitespace","Upper","Lower","Punctuation","Digit","Printable"]
for k, v in func_dic.iteritems():
    predicate = isSomething(v)
    globals()["is" + k] = predicate
    globals()["all" + k] = allSomething(predicate)
    globals()["any" + k] = anySomething(predicate)
    globals()["remove" + k] = removeSomething(predicate)
    globals()["only" + k] = onlySomething(predicate)

"""
def strtonum(string):
    if not allDigits(string):
        raise ValueError("Non-digit karakter in string")
    return reduce(lambda x,y: 10 * x + y,
                  [x -48 for x in [ord(x) for x in string]])
"""

words = lambda string : removePunctuation(string).split(" ")
unwords = lambda lst : " ".join(lst)

lines = lambda string : string.split(newline)
unlines = lambda lst : newline.join(lst)

def category(char):
    for cat in cat_order:
        if char in func_dic[cat]:
            return cat
    raise ValueError("Couldn't determine the type of %s" % char)

def makestrfunctions(string,k):
    predicate = isSomething(string)
    globals()["is" + k] = predicate
    globals()["all" + k] = allSomething(predicate)
    globals()["any" + k] = anySomething(predicate)
    globals()["remove" + k] = removeSomething(predicate)
    globals()["only" + k] = onlySomething(predicate)

categories = lambda string : [category(x) for x in string]
groups = lambda string: ["".join(iterator) for (kate, iterator) in groupby(string,category)]
reversewords = lambda string: unwords("".join(reversed(x)) for x in words(string))
