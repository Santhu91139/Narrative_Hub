import spacy
import random

nlp = spacy.load("en_core_web_sm")

badwords = ['fuck', 'shit', 'bastard', 'cunt', 'bick', 'buck off', 'asshole', 'bitch', 'stupid', 'lofer']

def generate_abstract_story(user_input, min_words=200):
    for sentence in user_input:
        for badword in badwords:
            sentence = sentence.replace(badword, '')

    doc = nlp(user_input)

    entities = {ent.label_: ent.text for ent in doc.ents}

    sentences = []

    for entity_type, entity_value in entities.items():
        sentences.append(f"In a {entity_value},")
        sentences.append(f"{entity_value} embarked on a journey.")
        sentences.append(f"The adventure unfolded with {entity_value} facing {entity_value} and {entity_value}.")

    generated_story = " ".join(sentences)

    while len(generated_story.split()) < min_words and sentences:
        new_sentence = random.choice(["And then", "Meanwhile", "In another part of the", "As the journey continued"])
        new_sentence += " " + random.choice(sentences)
        generated_story += " " + new_sentence
        sentences.append(new_sentence)

    return generated_story
