import pandas as pd
import spacy
nlp = spacy.load('en_core_web_lg')

# PRACTICAL TASK 1

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Cat and monkey had the highest score in the comparisons. This can be attributed
# to the fact that they are both animals. Monkey and banana had the second highest and this
# might be because monkeys eat bananas. Cat and banana had the lowest score, most likely due
# to bananas not being a common meal for cats so the model is unable to recognize a relationship.  


tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
            "Hello, there is my car",
            "I\'ve lost my car in my car",
            "I\'d like my boat back",
            "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - " + str(similarity))


# ------------------------------------My Example-----------------------------------------
my_word1 = nlp("Student")
my_word2 = nlp("Umbrella")
my_word3 = nlp("Book")
my_word4 = nlp("Water")

print(my_word1.similarity(my_word3))
print(my_word2.similarity(my_word4))
print(my_word2.similarity(my_word3))
print(my_word3.similarity(my_word4))


# --------------------------Small language model on example file-------------------------
# The small model has no word vectors loaded. The similarity scores were lower comaptred
# to when medium model was used. 


# PRACTICAL TASK 2

# Get data from file using pandas and save in a variable called movies
movies = pd.read_csv('movies.txt', delimiter='\t', header=None)
print(movies)

# Create the function to recommend a movie. 
def recommend_movie(description):
    desc_token = nlp(description)

    # Calculate semantic similarity with each movie description
    similarity_scores = []
    for index, row in movies.iterrows():
        movies_token = nlp(row[0])
        similarity_score = desc_token.similarity(movies_token)
        similarity_scores.append(similarity_score)

    # Find the index of the movie with the highest similarity score
    recommended_movie_index = similarity_scores.index(max(similarity_scores))

    # Return the recommended movie title
    return movies.loc[recommended_movie_index, 0]

# Get a movie recommendation
already_watched = '''Will he save their world or destroy it? When the Hulk becomes too dangerous 
                for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space 
                to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet 
                Sakaar where he is sold into slavery and trained as a gladiator.'''

recommendation = recommend_movie(already_watched)
print("Recommended Movie:", recommendation)