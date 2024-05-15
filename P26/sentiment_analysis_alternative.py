import numpy as np
import pandas as pd
import spacy
from textblob import TextBlob

# Gets polarity and subjectivity and adds them do the datafraim
def review_clean(df, COLUMN_RVW: str, COLUMN_POL: str, COLUMN_SUB: str, x: int)-> None:
    if pd.isna(df.at[x, COLUMN_POL]):
        nlp = spacy.load('en_core_web_md')
        reviews_data = df[COLUMN_RVW][x].lower().strip()
        clean_test = cleanText(reviews_data, nlp=nlp)
        df.at[x, COLUMN_POL] = sentiment_polarity(clean_test)
        df.at[x, COLUMN_SUB] = sentiment_subjectivity(clean_test)
    
# removes all unwanted data
def cleanText(text: str, nlp)-> str:
    doc = nlp(text)
    cleaned_tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct and not token.like_num]
    cleaned_text = ' '.join(cleaned_tokens)
    return cleaned_text


# https://textblob.readthedocs.io/en/dev/quickstart.html
# Sentiment(polarity=0.39166666666666666, subjectivity=0.4357142857142857)
# return subjectivity
def sentiment_subjectivity(review: str)-> float:
    analysis = TextBlob(review)
    return analysis.sentiment.subjectivity

# return polarity
def sentiment_polarity(review: str)-> float:
    analysis = TextBlob(review)
    return analysis.sentiment.polarity

# I dont know why this isn't working
def dfReady(df, COLUMN_RVW: str, COLUMN_POL: str, COLUMN_SUB: str):
    df = df.dropna(subset=[COLUMN_RVW])
    df[COLUMN_POL] = pd.Series(dtype='int')
    df[COLUMN_SUB] = pd.Series(dtype='int')


def main():
    # Set statics
    DATA_FILE: str = "data/amazon_product_reviews.csv"
    COLUMN_RVW: str = "reviews.text"
    COLUMN_POL: str = "polarity"
    COLUMN_SUB: str = "subjectivity"
    x: int = 2250

    
    df = pd.read_csv(DATA_FILE, dtype=str)
    # Claen subset
    # dfReady(df, COLUMN_RVW, COLUMN_POL, COLUMN_SUB)
    df = df.dropna(subset=[COLUMN_RVW])
    df[COLUMN_POL] = pd.Series(dtype='int')
    df[COLUMN_SUB] = pd.Series(dtype='int')

    review_clean(df, COLUMN_RVW, COLUMN_POL, COLUMN_SUB, x)

    print(f"\nReviews:\n{df[COLUMN_RVW][x]}\n\nPolarity Score:\n{df[COLUMN_POL][x]}\n\nSubjectivity Score:\n{df[COLUMN_SUB][x]}")

    print('done')
    
if __name__=='__main__':
    main()
