import dictionary1

print (dictionary1.d)
text= "hola yo soy una chica de España mi nombre es Monica tengo un hermano y una hermana mañana no clase"

translate= ""
words= text.split()
for w in words:
    translate = translate + dictionary1.d[w]

print (translate)