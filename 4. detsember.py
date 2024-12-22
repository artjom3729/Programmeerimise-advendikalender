sisend = "Sf zrjš pütn pftü!"

sisend = list(sisend)

tahestik = "ABCDEFGHIJKLMNOPRSŠZŽTUVÕÄÖÜ"
tahestik = list(tahestik)

laused = []

for arv in range(len(tahestik)):
    nihe = arv
    uus_lause = []
    for n in sisend:
        if n == " ":
            uus_lause.append(" ")
        elif n == ",":
            uus_lause.append(",")
        elif n == ".":
            uus_lause.append(".")
        elif n == "!":
            uus_lause.append("!")
        elif n == "?":
            uus_lause.append("?")
        else:
            try:
                index = tahestik.index(n.upper())
                new_index = (index - nihe) % len(tahestik)
                uus_lause.append(tahestik[new_index])
            except ValueError:
                
                uus_lause.append(n)
    laused.append("".join(uus_lause))
            
for n in laused:
    print(n)