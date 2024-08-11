numberInput = int(input("Star : "))
text = ""
space = numberInput-1
for x in range(numberInput):
    text += "*"
    print(" "*(space)+text)
    text +=  "*"
    space -= 1
