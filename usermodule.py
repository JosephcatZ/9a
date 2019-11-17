Times = {
    "ab":464,
    "ac":518,
    "bc":141
}
keys = []
for i in Times:
    if not i[0] in keys:
        keys.append(i[0])
    if not i[1] in keys:
        keys.append(i[1])
def factorial(x):
    if x == 1:
        return(1)
    else:
        return(x*factorial(x-1))    
print(factorial(2))
def combos(x):
    total = []
    for i in range(factorial(len(x))):
        j = x
        if len(x) == 1:
            return([x[0]])
        else:
            j.remove(x[i%len(x)])
            for k in combos(j):
                total.append(x[i%len(x)]+k)
    return(total)            
print(combos(keys))
