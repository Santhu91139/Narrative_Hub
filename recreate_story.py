import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# NLP and Sentiment Analysis
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def recreate_story(input_story):
    # Text preprocessing

    # Tokenize the cleaned story into sentences
    sentences = nltk.sent_tokenize(input_story)

    badwords = ['fuck', 'shit', 'bastard', 'cunt', 'bick', 'buck off', 'asshole', 'bitch', 'stupid', 'lofer']

    # Create dialogue based on sentiment
    recreated_story = ""
    for sentence in sentences:
        sentiment_score = sia.polarity_scores(sentence)['compound']

        for badword in badwords:
            sentence = sentence.replace(badword, '****')

        if sentiment_score >= 0.05:
            recreated_story += f"Character 1: {sentence}\nCharacter 2: That's great!\n"
        elif sentiment_score <= -0.05:
            recreated_story += f"Character 1: {sentence}\nCharacter 2: That's sad.\n"
        else:
            recreated_story += f"Character 1: {sentence}\nCharacter 2: Hmm...\n"

    return recreated_story
