from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def sentiment_analysis():
    result = None
    if request.method == 'POST':
        text = request.form.get('text', '').strip()
        if text:
            analysis = TextBlob(text)
            result = {
                'text': text,
                'polarity': analysis.sentiment.polarity,
                'subjectivity': analysis.sentiment.subjectivity
            }
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
