max_weight = 7933006
sisend = """2726153
4186044
3136410
4592531
2447141
2949780
3752986
4305189
1169064
1352819
2055567
1963417
4745234
2481507
4602506
1131692"""

def min_trucks(max_weight, sisend):
    weights = list(map(int, sisend.strip().split()))
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

result = min_trucks(max_weight, sisend)
print(result)
