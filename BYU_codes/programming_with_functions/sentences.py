import random

def main():
    sentences = []
    for i in range(6):
        quantity = int(input("Tell me the quantity (1 or more): "))
        tense = input("Tell me the tense (past, present or future): ")
        sentence = make_sentence(quantity, tense)
        sentences.append(sentence)
    print("\nHere are the sentences:\n")
    for sentence in sentences:
        print(sentence)
    print()

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird","boy","car","cat","child","dog","girl","man","rabbit","woman"]
    else:
        nouns = ["birds","boys","cars","cats","children","dogs","girls","men","rabbits","women"]
    
    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    if tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present":
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    else:
        verbs = ["will drink","will eat","will grow","will laugh","will think","will run","will sleep","will talk","will walk","will write"]
    
    verb = random.choice(verbs)
    return verb

def get_prepositional_phrase(quantity):
    prepositions = ["across", "near", "under", "without", "from", "behind"]
    preposition = random.choice(prepositions)

    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    return f" {preposition} {determiner} {noun}"

def get_adjective():
    adjectives = ["happy", "tiny", "angry", "big", "lazy", "sleepy", "playful"]
    adjective = random.choice(adjectives)
    return adjective

def get_adverb():
    adverbs = ["quickly", "slowly", "quietly", "loudly", "angrily", "kindly", "gently"]
    adverb = random.choice(adverbs)
    return adverb

def make_sentence(quantity, tense):
    sentence = f"{get_determiner(quantity)} {get_adjective()} {get_noun(quantity)} {get_prepositional_phrase(quantity)} {get_adverb()} {get_verb(quantity, tense)} {get_determiner(quantity)} {get_adjective()} {get_noun(quantity)} {get_prepositional_phrase(quantity)}."
    return sentence
    
main()