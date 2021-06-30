from flask import Flask, render_template, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/screening')
def screening():
    return render_template('screening.html')

@app.route('/gettoknow')
def gettoknow():
    return render_template('gettoknow.html')

@app.route('/helpline')
def helpline():
    return render_template('helpline.html')

@app.route('/mentalhealth')
def mentalhealth():
    return render_template('mentalhealth.html')

@app.route('/suicideanalysis')
def suicideanalysis():
    return render_template('suicideanalysis.html')

@app.route('/analysis', methods=["GET", "POST"])
def analysis():
    if request.method == "POST":
        inp = request.form.get("inp")
        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(inp)
        neg = score["neg"]
        pos = score["pos"]
        if neg > pos:
            return render_template('analysis.html', message="You are currently having some Negative thoughts!", mood="😢", thank="Thank you for trying out our Sentiment Analyser hope you get clarity on your thoughts and feelings.")
        elif pos > neg:
            return render_template('analysis.html', message="You are currently having some Possitive thoughts!", mood="😊", thank="Thank you for trying out our Sentiment Analyser hope you get clarity on your thoughts and feelings.")
        else:
            return render_template('analysis.html', message="You are currently having some Neutral thoughts!", mood="😌", thank="Thank you for trying out our Sentiment Analyser hope you get clarity on your thoughts and feelings.")
    else:
        return render_template('analysis.html',  mood="Please enter your thoughts and click 'Submit' to know your results.")


    return render_template('analysis.html')