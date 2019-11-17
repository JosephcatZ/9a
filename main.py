key = {}
IN = open("input").readlines()
for i in range(len(IN)):
    print(IN[i])
    if "\n" in IN[i]:
        IN[i] = IN[i][0:len(IN[i])-1]
    IN[i] = IN[i].split(" ")
furthest = 0
alphabet = "qwertyuiopasdfghjklzxcvbnm./'][\=-0987654321`~!@#$%^&*()_+|}{POIUYTREWQASDFGHJKL:\\\"?><MNBVCXZ"
Times = {}
for i in IN:
    if i[0] not in key:
        key[i[0]] = alphabet[furthest]
        furthest += 1
    if i[2] not in key:
        key[i[2]] = alphabet[furthest]
        furthest += 1
    Times[key[i[0]]+key[i[2]]] = int(i[4])
keys = []
print(Times)
for i in Times:
    if not i[0] in keys:
        keys.append(i[0])
    if not i[1] in keys:
        keys.append(i[1])
factorials ={
    1:1,
    2:2,
    3:6,
    4:24,
    5:120,
    6:720
}
print(len(keys))  
def combos(x):
    total = []
    if len(x) > 3:
        print(x)
    for i in range(len(x)):
        j= []
        for l in x:
            j.append(l)
        if len(x) == 1:
            return([x[0]])
        else:
            j.remove(x[i%len(x)])
            for k in combos(j):
                total.append(x[i%len(x)]+k)
    return(total)            
ways = combos(keys)
valids = {}

def dist(x):
    total = 0
    for i in range(len(x)-1):
        #print(x[i]+x[i+1])
        if x[i] + x[i+1] in Times:
            total+=(Times[x[i]+x[i+1]])
        else:
            total+=(Times[x[i+1]+x[i]])
    return(total)
print(ways)
Min = 9999999999
Max = 0
for i in ways:
    j = dist(i)
    if j < Min:
        Min = j
    if j > Max:
        Max = j
print("Min",Min,"\nMax",Max)