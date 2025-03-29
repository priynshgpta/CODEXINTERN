from textblob import TextBlob

def analyze(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    polarity = sentiment.polarity # from -1 to 1
    
    if polarity > 0:
        category = "Positive"
    elif polarity < 0:
        category = "Negative"
    else:
        category = "Neutral"

    return category

text = input("Enter you text: ")
result = analyze(text)
print(f"Sentiment: {result}")