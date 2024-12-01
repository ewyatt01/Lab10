d1 = { "Amy": 12, "Jack": 20}


def my_get(d1, x, default):
    if x in d1:
        return d1[x]
    else:
        return default

print(my_get(d1, "Amy", 0 ))

print(d1.get('Amy', 0)) 
