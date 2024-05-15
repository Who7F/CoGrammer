import numpy as np
import pandas as pd
import spacy
from textblob import TextBlob

def review_clean(df, COLUMN_RVW, COLUMN_AYS, x):
    if pd.isna(df.at[x, COLUMN_AYS]):
        nlp = spacy.load('en_core_web_md')
        reviews_data = df[COLUMN_RVW][x].lower().strip()
        df.at[x, COLUMN_AYS] = sentiment_analysis(clean_text(reviews_data, nlp=nlp))
    

def clean_text(text, nlp):
    doc = nlp(text)
    cleaned_tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct and not token.like_num]
    cleaned_text = ' '.join(cleaned_tokens)
    return cleaned_text

    
def sentiment_polarity(review):
    analysis = TextBlob(review)
    return analysis.sentiment.polarity


def sentiment_analysis(review):
    analysis = TextBlob(review)
    return analysis.sentiment.polarity

def dfReady(df, COLUMN_RVW, COLUMN_AYS):
    df = df.dropna(subset=[COLUMN_RVW])
    df[COLUMN_AYS] = pd.Series(dtype='int')
    
def main():
    # Set statics
    DATA_FILE = "data/amazon_product_reviews.csv"
    COLUMN_RVW = "reviews.text"
    COLUMN_AYS = "analysis"
    x = 674

    # Load in file
    df = pd.read_csv(DATA_FILE, dtype=str)
    # Claen subset
    
    dfReady(df, COLUMN_RVW, COLUMN_AYS)
    
    review_clean(df, COLUMN_RVW, COLUMN_AYS, x)

    print(f"\nReviews:\n{df['reviews.text'][x]}\n\n Score:\n{df['analysis'][x]}")

    print('done')
    
if __name__=='__main__':
    main()
