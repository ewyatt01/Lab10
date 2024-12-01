#find freqnecy of the first letters of the last names. Use dictionary to take care of number of similar first names.

cpsc_names = ["Margaret", "Laneman", "Lily", "DeYoung", "Serenity", "Schuler", "Olivia", "Beck" "Colleen", "Hand", "Anna", "Raycroft",
              "Victoria", "Garcia Jimenez", "Gwyneth", "Gangwer", "Mairi", "Weber-Hess", "Aliza", "Litvak", "Elizabeth", "Wyatt", "Rylee", "Taylor"]

def freq_first_in_last(d):
    name_histogram = {}
    for i in range(1, len(cpsc_names), 2):
        last_name = cpsc_names[i]
        first_letter = last_name[0]
        if first_letter in name_histogram:
            name_histogram[first_letter] += 1
        else:
            name_histogram[first_letter] = 1
    return name_histogram

print(freq_first_in_last(cpsc_names))
    


