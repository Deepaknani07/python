mystr=input("enter the string:")
new_str=""
for c in mystr:
    if c not in punctuations:
        new_str+=c
        print(new_str)
