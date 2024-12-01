#Frequency of first names by storing the same names in lists



classmates = {"Laneman": "Margaret", "DeYoung": "Lily", "Schuler": "Serenity", "Beck": "Olivia", "Hand": "Colleen", "Raycroft": "Anna",
              "Garcia Jimenez": "Victoria", "Gangwer":"Gwyneth", "Weber-Hess": "Mairi", "Litvak": "Aliza", "Wyatt": "ELizabeth", "Taylor":"Rylee"}

vals = classmates.values()
d1 = {}

def histogram(d):
    for x in vals:
        if x not in d1:
            d1[x] = 1
        else:
            d1[x] += 1
    return d1

print(histogram(classmates))

        



