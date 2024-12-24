input_str = "Sf zrjš pütn pftü!"

def decrypt_caesar(input_str: str) -> list:
    input_str = list(input_str)

    alphabet = "ABCDEFGHIJKLMNOPRSŠZŽTUVÕÄÖÜ"
    alphabet = list(alphabet)

    sentences = []

    for shift in range(len(alphabet)):
        new_sentence = []
        for character in input_str:
            if character in " ,.!?:;-—":
                new_sentence.append(character)
            else:
                index = alphabet.index(character.upper())
                new_index = (index - shift) % len(alphabet)
                new_sentence.append(alphabet[new_index])
        sentences.append("".join(new_sentence))
    
    return sentences

for sentence in decrypt_caesar(input_str):
    print(sentence) # Leidke ise õige lause