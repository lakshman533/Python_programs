import keyword
word=input()
words=['break', 'case', 'continue', 'default', 'defer', 'else', 'for', 'func', 'goto', 'if', 'map', 'range', 'return', 'struct', 'type', 'var']
if word in words and keyword.iskeyword(word):
    print(word + " is python keyword")
else:
    print(word + " is not a python keyword")