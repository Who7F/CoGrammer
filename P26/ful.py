import numpy as np
import pandas as pd
import spacy
from textblob import TextBlob

def review_clean(df, COLUMN_DATA, x):
    nlp = spacy.load('en_core_web_md')
    reviews_data = df[COLUMN_DATA][x].lower() 
    df['analysis'][x] = sentiment_analysis(clean_text(reviews_data, nlp=nlp))
    

def clean_text(text, nlp):
    doc = nlp(text)
    cleaned_tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    cleaned_text = ' '.join(cleaned_tokens)
    return cleaned_text

    
def sentiment_analysis(review):
    analysis = TextBlob(review)
    return analysis.sentiment.polarity


def main():
    # Set statics
    DATA_FILE = "data/amazon_product_reviews.csv"
    COLUMN_DATA = "reviews.text"

    # Load in file
    df = pd.read_csv(DATA_FILE)

    # Claen subset
    df = df.dropna(subset=[COLUMN_DATA])
    df['analysis'] = pd.Series(dtype='int')
    
    review_clean(df, COLUMN_DATA, 5)

    print(f"\nThis is a better way\n\n{df['reviews.text'][5]}\n\n {df['analysis'][5]}")

    print('done')

    
if __name__=='__main__':
    main()
