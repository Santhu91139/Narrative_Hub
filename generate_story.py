
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

story_dataset = pd.read_csv('story_dataset.csv')

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def generate_story(selected_mood, selected_genre):
    selected_stories = story_dataset[(story_dataset['Mood'] == selected_mood) & (story_dataset['Genre'] == selected_genre)]
    combined_story = " ".join(selected_stories['Story'])

    sentences = nltk.sent_tokenize(combined_story)

    dialogue_based_story = ""
    for sentence in sentences:
        sentiment_score = sia.polarity_scores(sentence)['compound']
 
        if sentiment_score >= 0.05:
            dialogue_based_story += f"Character 1: {sentence}\nCharacter 2: That's great!\n"
        elif sentiment_score <= -0.05:
            dialogue_based_story += f"Character 1: {sentence}\nCharacter 2: That's sad.\n"
        else:
            dialogue_based_story += f"Character 1: {sentence}\nCharacter 2: Hmm...\n"

    return dialogue_based_story
