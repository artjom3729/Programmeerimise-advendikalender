friends = """Meelis
Raimond
Lilian
Marek
Valeria
Henrik
Riho
Jelena
Sulev
Joel"""

dislike = """Valeria: Lilian
Jelena: Lilian, Meelis
Sulev: Raimond, Marek, Lilian, Valeria, Joel"""

not_invited = """Meelis
Raimond
Valeria
Marek
Riho
Jelena
Sulev
Joel"""

def parse_list(s):
    return s.strip().splitlines()

def parse_dislike(s):
    dislike_dict = {}
    for line in s.strip().splitlines():
        person, dislikes = line.split(': ')
        dislike_dict[person] = dislikes.split(', ')
    return dislike_dict

def filter_friends(friends, not_invited):
    return [friend for friend in friends if friend not in not_invited]

def find_invited(friends, dislike, not_invited):
    friends_list = parse_list(friends)
    not_invited_list = parse_list(not_invited)
    dislike_dict = parse_dislike(dislike)
    
    filtered_friends = filter_friends(friends_list, not_invited_list)
    invited = []
    
    for friend in filtered_friends:
        if all(disliked not in invited for disliked in dislike_dict.get(friend, [])):
            invited.append(friend)
    
    return invited

result = find_invited(friends, dislike, not_invited)
print(", ".join(result))
