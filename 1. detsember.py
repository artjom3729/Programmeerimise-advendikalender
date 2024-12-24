input_str = "odForMedFuDrDynamiti"

total = 0

prices = {
    "Kelluke": 1.64,
    "ForMe": 1.89,
    "Dynamit": 0.92
}

total += prices["Kelluke"] * input_str.count("Kelluke")
total += prices["ForMe"] * input_str.count("ForMe")
total += prices["Dynamit"] * input_str.count("Dynamit")

print(total) # Oodatav väljund: 2.81