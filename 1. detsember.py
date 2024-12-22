sisend = "odForMedFuDrDynamiti"

summa = 0

hinnad = {
    "Kelluke": 1.64,
    "ForMe": 1.89,
    "Dynamit": 0.92
}

summa += hinnad["Kelluke"] * sisend.count("Kelluke")
summa += hinnad["ForMe"] * sisend.count("ForMe")
summa += hinnad["Dynamit"] * sisend.count("Dynamit")

print(summa)