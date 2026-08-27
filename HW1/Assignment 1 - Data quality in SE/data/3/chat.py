from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
app = Flask(__name__)
myBot=ChatBot(name='Aouataf', storage_adapter="chatterbot.storage.SQLStorageAdapter")
""" greetings=["hi there!","hi","how are you doing?","fine","good", "great", "what's your name?","aouataf"]
math1=["pythagorean theorem","a squared plus b squared equals c squared"]
math2=["law of cosine","c**2= a**2+b**2-2*a*b*cos(gamma)"]
list_trainer=ListTrainer(myBot)
for item in (greetings,math1, math2):
    list_trainer.train(item) """



corpus_trainer=ChatterBotCorpusTrainer(myBot)
corpus_trainer.train('chatterbot.corpus.english')
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(myBot.get_response(userText))

if __name__ == "__main__":
    app.run()