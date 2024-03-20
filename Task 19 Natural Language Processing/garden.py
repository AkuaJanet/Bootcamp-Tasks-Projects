# Import spacy module and its English language model. Store the model
# in a variable called nlp.

import spacy
nlp = spacy.load('en_core_web_sm')

# Store the garden path sentences in a list
gardenpathSentences = [
                    "The old man the boats.", 
                    "The horse raced past the barn fell.",
                    "Mary gave the child a Band-Aid.",
                    "That Jill is never here hurts.",
                    "The cotton clothing is made of grows in Mississippi."
                    ]

# Loop through the list to tokenize the sentences and perform NER
for token in gardenpathSentences:
    doc = nlp(token)
    for ent in doc.ents:
        print(f"{ent.text:{14}} {ent.label_}")

print(spacy.explain('PERSON'))
print(spacy.explain('GPE'))

# PERSON - People, including fictional. The entity is associated appropriately.
# GPE - Countries, cities, states. This entity matches the word. 