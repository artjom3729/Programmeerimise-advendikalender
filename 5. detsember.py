events = """Naaber viib prügikoti välja: 0
Naaber kaevab midagi tagahoovis: 5
Naaber kannab raskeid kotte autosse: 2
Naaber lohistab suurt musta kotti keldrisse: 10
Naaber vaatab pikalt aknast välja: 7
Naaber viib hilisõhtul midagi autosse: 4
Naaber grillib keset talve: 1
Naaber paneb keset päeva kardinad kinni: 6
Naaber lahkub hilisõhtul majast: 3
Naabril käivad pidevalt külalised, kes kauaks ei jää: 7
Naaber väldib teisi naabreid: 5
Naaber jalutab oma koera: -1
Naaber parandab oma aeda: -3
Naaber kaunistab maja: -2
Naaber on alati sõbralik: -5
Naaber laenab suhkrut, et piparkooke küpsetada: 0"""

neighbours = """0: Naaber on alati sõbralik, Naaber vaatab pikalt aknast välja, Naaber jalutab oma koera, Naaber viib prügikoti välja, Naaber vaatab pikalt aknast välja
1: Naaber parandab oma aeda, Naaber kaunistab maja, Naaber grillib keset talve
2: Naaber lahkub hilisõhtul majast, Naabril käivad pidevalt külalised, kes kauaks ei jää, Naaber kannab raskeid kotte autosse, Naaber väldib teisi naabreid
3: Naaber väldib teisi naabreid, Naaber väldib teisi naabreid
4: Naaber kaunistab maja, Naaber viib hilisõhtul midagi autosse, Naaber viib prügikoti välja"""

def parse_neighbours(neighbours: str) -> list:
    neighbours = neighbours.replace(", N", "; N")
    
    neighbours_list = []

    neighbours = neighbours.strip().splitlines()

    for line in neighbours:
        _, actions = line.split(':')
        actions_list = [action.strip() for action in actions.split(';')]
        neighbours_list.append(actions_list)

    return neighbours_list

def parse_events(events: str) -> dict:
    events_dict = {}

    for line in events.strip().splitlines():
        event, number = line.split(':', 1)
        events_dict[event.strip()] = int(number.strip())

    return events_dict

def find_sus_neighbours(neighbours: str, events: str) -> int:
    neighbours_list = parse_neighbours(neighbours)
    events_dict = parse_events(events)
    
    neighbours_scores = []

    for neighbour in neighbours_list:
        neighbour_score = 0
        for action in neighbour:
            neighbour_score += events_dict[action]
        neighbours_scores.append(neighbour_score)

    sus_neighbours = 0

    for score in neighbours_scores:
        if score > 10:
            sus_neighbours += 1
    
    return sus_neighbours
    
print(find_sus_neighbours(neighbours, events)) # Oodatav väljund: 1


