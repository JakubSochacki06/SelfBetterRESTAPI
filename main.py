import random
from flask import Flask
app = Flask(__name__)
from quotes import quotes

@app.get("/")
def welcome_text():
    return {"Text":"Welcome in SelfBetterAPI"}
@app.get("/randomQuote")
def get_random_quote():
    return quotes[random.randint(0,100)]

if __name__ == "__main__":
    app.run()
