#find all numbers which are divisble by 7 but are not s multiple 5
l=[]
for i in range(0,1000):
    if i%7==0 and i%5!=0:
        l.append(str(i))
print(','.join(l))
