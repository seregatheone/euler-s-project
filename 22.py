su = 0
f = open(r"p022_names.txt","r")
text= f.read()
f.close()
text = text.replace('"',"").split(",")
text.sort()
for i in range(1,len(text)+1):
    word = list(text[i-1])
    for el in word:
        su+=(ord(el)-64)*i
print(su)
