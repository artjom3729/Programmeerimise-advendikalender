from itertools import combinations

traps = """0: puit:10, naelad:11, köis:11
1: puit:11, naelad:11, köis:10
2: puit:10, naelad:11, köis:10
3: puit:10, naelad:10, köis:10
4: puit:11, naelad:11, köis:11
5: puit:11, naelad:10, köis:10"""

resources = """puit: 42
naelad: 49
köis: 49"""

def parse_traps(traps_str):
    trap_list = []
    for line in traps_str.strip().split("\n"):
        left, right = line.split(": ", 1)
        trap_id = int(left)
        parts = right.split(", ")
        trap_resources = {}
        for p in parts:
            k, v = p.split(":")
            trap_resources[k.strip()] = int(v.strip())
        trap_list.append((trap_id, trap_resources))
    trap_list.sort(key=lambda x: x[0])
    return trap_list

def parse_resources(resources_str):
    resource_dict = {}
    for line in resources_str.strip().split('\n'):
        name, val = line.split(':')
        resource_dict[name.strip()] = int(val.strip())
    return resource_dict

def can_build_subset(subset, resources):
    used = {r: 0 for r in resources}
    for _, trap_res in subset:
        for r, amt in trap_res.items():
            used[r] += amt
            if used[r] > resources[r]:
                return False
    return True

def find_best_combo(traps_str, resources_str):
    traps = parse_traps(traps_str)
    resources = parse_resources(resources_str)
    best_combo = []
    
    for r in range(len(traps) + 1):
        current_combos = []
        for combo in combinations(traps, r):
            if can_build_subset(combo, resources):
                current_combos.append([t[0] for t in combo])
        if current_combos:
            best_combo = min(current_combos)
    return best_combo

best_trap_combo = find_best_combo(traps, resources)
print(", ".join(map(str, best_trap_combo)))
