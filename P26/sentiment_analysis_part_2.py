from textblob import TextBlob
    
def sentiment_analysis(review, x):
    analysis = TextBlob(review[x])
    return analysis.sentiment.polarity


def main():
    # Set statics
    TEXT_FILE = "data/text.txt"
    
    with open(TEXT_FILE, 'r', encoding='utf-8') as file:
        cleaned_reviews = file.readlines()

    print(cleaned_reviews[3])
    print(sentiment_analysis(cleaned_reviews, 3))
    print('done')

    
if __name__=='__main__':
    main()
