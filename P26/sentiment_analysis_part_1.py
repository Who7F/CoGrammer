import numpy as np
import pandas as pd
import spacy
from textblob import TextBlob

# Show data fraim detals
def get_head(df):
    print(f"\nHead\n{df.head}")
    print(f"\nNull\n{df.isnull().sum()}")
    print(f"\nInfo\n{df.info()}")
    print(f"\nShape\n{df.shape}")
    
# Due to time it take to clean the data this will be moved to a new progam
def sentiment_analysis(review):
    analysis = TextBlob(review)
    return analysis.sentiment.polarity

# Clean data
def review_clean(df, COLUMN_DATA):
    nlp = spacy.load('en_core_web_md')
    reviews_data = df[COLUMN_DATA].str.lower()
    get_head(reviews_data)
    return reviews_data.apply(clean_text, nlp=nlp)
    
# appy nlp
def clean_text(text, nlp):
    doc = nlp(text)
    cleaned_tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    cleaned_text = ' '.join(cleaned_tokens)
    return cleaned_text
    

def main():
    # Set statics
    DATA_FILE = "data/amazon_product_reviews.csv"
    TEXT_FILE = "data/text.txt"
    CSV_FILE = "data/text.csv"
    COLUMN_DATA = "reviews.text"
    
    # Load in file
    df = pd.read_csv(DATA_FILE)
    get_head(df)

    # Claen subset
    df_dropna = df.dropna(subset=[COLUMN_DATA])
    clean_sebset = review_clean(df_dropna, COLUMN_DATA)

    # Store subset
    clean_sebset.to_csv(CSV_FILE, sep=',', index=False, encoding='utf-8')
    with open(TEXT_FILE, 'w', encoding='utf-8') as my_file:
        my_file.write('\n'.join(clean_sebset))

    print('done')
