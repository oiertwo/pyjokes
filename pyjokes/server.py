from flask import Flask
import pyjokes as pj
import random

app = Flask(__name__)

@app.route("/")
def joke():
    if random.random() < 0.5 :
        joke = pj.get_chuck_nerd_joke()
    else:
        joke = pj.get_local_joke()
    return(joke)

@app.route("/chuck")
def chuck():
    joke = pj.get_chuck_nerd_joke()
    return(joke)

@app.route("/local")
def local():
    joke = pj.get_local_joke()
    return(joke)

if __name__ == "__main__":
    app.run()
