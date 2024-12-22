sisend = """Hei Kristjan, olete kutsutud minu peole!
Peol on kohal ka palju teisi külalisi, nii et kindlasti on kelleltki midagi huvitavat kuulda.
Ilma teie osaluseta ei saa see pidu kindlasti nii lõbus olema!
----------------------------------
Tere Ülle, olete kutsutud minu peole!
Peol on kohal ka palju teisi külalisi, nii et kindlasti on kelleltki midagi huvitavat kuulda.
----------------------------------
Hei Maire, olete kutsutud minu peole!
Õhtusööki saadab mõnus muusika ja meeleolukas seltskond.
Ilma teie osaluseta ei saa see pidu kindlasti nii lõbus olema!"""

def count_blocks(text):
    # Split the text into individual invitations
    invitations = text.split('----------------------------------')

    total_3x3 = 0
    total_2x2 = 0
    total_1x1 = 0
    
    for invitation in invitations:
        lines = invitation.strip().split('\n')
        height = len(lines)
        
        if height == 3:
            max_row = max(len(line) for line in lines)
            total_3x3 += (max_row // 3)
            max_row %= 3
            if max_row == 2:
                total_2x2 += 1
                total_1x1 += 2
            if max_row == 1:
                total_1x1 += 3
        if height == 2:
            max_row = max(len(line) for line in lines)
            total_2x2 += (max_row // 2)
            max_row %= 2
            if max_row == 1:
                total_1x1 += 2
        if height == 1:
            total_1x1 += len(lines[0])
                
    return total_3x3, total_2x2, total_1x1

blocks_3x3, blocks_2x2, blocks_1x1 = count_blocks(sisend)
print(f"{blocks_3x3}, {blocks_2x2}, {blocks_1x1}")