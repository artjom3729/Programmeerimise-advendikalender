sisend = "v v p p p p p v p v"

sisend = sisend.strip().split()
sisend = [n for n in sisend if n != " "]

arv = 1

for n in sisend:
    if n == "p":
        arv *= 2
    if n == "v":
        arv = arv * 2 - 1

print(arv)