# source: https://www.etera.ee/zoom/201466/view?page=1&p=separate&tool=info
from estnltk.vabamorf.morf import syllabify_words

input_str = """teel eal sumpas aga väike langesid üksinda jõuan
pimedus puna taas vöö sügavad uus mille eal nad ka
jõuluvanal päkapikuke et päkapikule kas
kuueta lumehangesid püksisääre langes peal siin
kuuele hangede jõulukringel helvestena et täitub suur"""

rows = input_str.strip().splitlines()

def count_syllables(row):
    words = row.split()
    syllabified = syllabify_words(words)
    syllable_count = sum(len(word_list) for word_list in syllabified)
    return syllable_count

syllable_counts = [count_syllables(row) for row in rows]

amount = len([count for count in syllable_counts if count != 16])

print(amount)