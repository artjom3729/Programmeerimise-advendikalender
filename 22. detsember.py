from itertools import combinations

traps_text = """0: puit:55, naelad:66, köis:79
1: puit:88, naelad:36, köis:17
2: puit:80, naelad:29, köis:38
3: puit:14, naelad:42, köis:72
4: puit:81, naelad:90, köis:34
5: puit:14, naelad:38, köis:31
6: puit:93, naelad:65, köis:68
7: puit:13, naelad:85, köis:53
8: puit:58, naelad:22, köis:83
9: puit:90, naelad:29, köis:75
10: puit:32, naelad:62, köis:89
11: puit:43, naelad:72, köis:29
12: puit:50, naelad:32, köis:25
13: puit:91, naelad:69, köis:93
14: puit:93, naelad:70, köis:86
15: puit:55, naelad:23, köis:96
16: puit:51, naelad:61, köis:13
17: puit:87, naelad:60, köis:33
18: puit:21, naelad:100, köis:86
19: puit:86, naelad:76, köis:96
20: puit:82, naelad:68, köis:50
21: puit:85, naelad:66, köis:60
22: puit:84, naelad:36, köis:43
23: puit:10, naelad:12, köis:18
24: puit:94, naelad:45, köis:48"""

resources_text = """puit: 315
naelad: 431
köis: 400"""

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
    
    # Iterate through all possible combination sizes
    for r in range(len(traps) + 1):
        current_combos = []
        for combo in combinations(traps, r):
            if can_build_subset(combo, resources):
                current_combos.append([t[0] for t in combo])
        if current_combos:
            # Keep the largest valid combination size
            best_combo = min(current_combos)  # Lexicographically smallest
    return best_combo

best_trap_combo = find_best_combo(traps_text, resources_text)
print("Best combination of traps:", best_trap_combo)
