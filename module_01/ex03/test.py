from generator import generator

text = (
    "-> -> Le Lorem Ipsum est simplement :> du faux texte <:"
    "et non pas :> du vrai texte <: . <- <-"
)
print('### Normal ###\n')
for word in generator(text, sep=" "):
    print(word)

print('\n### Ordered ###\n')
for word in generator(text, sep=" ", option="ordered"):
    print(word)

print('\n### Shuffle ###\n')
for word in generator(text, sep=" ", option="shuffle"):
    print(word)

print('\n### Unique ###\n')
for word in generator(text, sep=" ", option="unique"):
    print(word)

print('\n### Error ###\n')
for word in generator(text, sep=" ", option="error"):
    print(word)

print('\n### Error 2 ###\n')
for word in generator(1):
    print(word)

print('\n### Error 3 ###\n')
for word in generator(text, sep=1):
    print(word)

print('\n### Error 4 ###\n')
for word in generator(text, sep=" ", option=1):
    print(word)
