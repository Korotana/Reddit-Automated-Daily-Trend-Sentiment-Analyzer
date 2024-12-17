from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity < 0:
        return "negative"
    else:
        return "neutral"

def analyze_multiple_sentiment_average(comments):
    average_sentiment = 0

    for comment in comments:
        if analyze_sentiment(comment.body) == "positive":
            average_sentiment += 1
        if analyze_sentiment(comment.body) == "negative":
            average_sentiment -= 1

    if average_sentiment > 0:
        return "positive"
    elif average_sentiment < 0:
        return "negative"
    else:
        return "neutral"
