max_weight = 48
input_str = """44
41
25
25
24
22
20
18
16
12"""

def min_trucks(max_weight, input_str):
    weights = list(map(int, input_str.strip().split()))
    weights.sort(reverse=True)
    
    trucks = []
    
    for weight in weights:
        placed = False
        for truck in trucks:
            if sum(truck) + weight <= max_weight:
                truck.append(weight)
                placed = True
                break
        if not placed:
            trucks.append([weight])
    
    return len(trucks)


result = min_trucks(max_weight, input_str)
print(result) # Expected output: 6
