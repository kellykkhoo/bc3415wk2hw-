from flask import Flask, render_template, request 
import google.generativeai as palm 
import os

#api = "AIzaSyCNYWXiaRU1zUpf6w08yrvHjMqaV77r3R8" cannot post api keys 
api = os.getenv("MAKERSUITE_API_TOKEN") 
palm.configure(api_key=api)
model = {"model": "models/chat-bison-001"}

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    return(render_template("index.html")) 

@app.route("/financial_QA",methods=["GET","POST"])
def financial_QA():
    return(render_template("financial_QA.html"))

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    return(render_template("prediction.html"))

@app.route("/joke",methods=["GET","POST"])
def joke():
    return(render_template("joke.html"))

@app.route("/makersuite",methods=["GET","POST"])
def makersuite():
    q = request.form.get("q")
    r = palm.chat(messages=q, **model)
    return(render_template("makersuite.html",r=r.last))



if __name__ == "__main__":
    app.run()