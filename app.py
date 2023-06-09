import random
from flask import Flask
app = Flask(__name__)
from quotes import quotes
from advices import *
import gunicorn
@app.get("/")
def welcome_text():
    return {"Text":"Welcome in SelfBetterAPI"}
@app.get("/randomQuote")
def get_random_quote():
    return quotes[random.randint(0,100)]
@app.get("/advice/angry")
def get_angry_advice():
    return angryAdvices[random.randint(0,19)]
@app.get("/advice/sad")
def get_sad_advice():
    return sadAdvices[random.randint(0,19)]
@app.get("/advice/mixed")
def get_mixed_advice():
    return mixedAdvices[random.randint(0,19)]
@app.get("/advice/neutral")
def get_neutral_advice():
    return neutralAdvices[random.randint(0,19)]
@app.get("/advice/happy")
def get_happy_advice():
    return happyAdvices[random.randint(0,19)]
if __name__ == "__main__":
    app.run()
