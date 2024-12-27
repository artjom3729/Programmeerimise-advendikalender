invited_guests = """ema-165-35-punane mantel
isa-175-40-sinine jakk
Heino-180-45-räpane särk
lilian-160-30-puhas mantel"""

coming_guests = """165 cm, 35 aastat vana, seljas on punane mantel
180 cm, 45 aastat vana, seljas on räpane särk
160 cm, 30 aastat vana, seljas on sinine mantel
180 cm, 45 aastat vana, seljas on räpane särk"""

def parse_invited_guests(s):
    guests = {}
    for line in s.strip().splitlines():
        name, height, age, description = line.split('-')
        guests[f"{height} cm, {age} aastat vana, seljas on {description}"] = name
    return guests

def parse_coming_guests(s):
    return s.strip().splitlines()

def face_control(invited_guests, coming_guests):
    invited = parse_invited_guests(invited_guests)
    coming = parse_coming_guests(coming_guests)
    
    allowed = set()
    not_allowed = set()
    
    for guest in coming:
        if guest in invited and guest not in allowed:
            allowed.add(guest)
        else:
            not_allowed.add(guest)
    
    return len(allowed), len(not_allowed)


allowed_count, not_allowed_count = face_control(invited_guests, coming_guests)
print(f"Sissepääs lubatud: {allowed_count}. Sissepääs keelatud: {not_allowed_count}.") # Expected output: Sissepääs lubatud: 2. Sissepääs keelatud: 2.
