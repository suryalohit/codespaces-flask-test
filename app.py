from flask import Flask, render_template
import requests
TOKEN = "6994416717:AAH_qEF1vSy1gZc1nXQ4eyM4dErJshFGJaM"
chat_id = "998041732"


app = Flask(__name__)

@app.route("/")
def hello_world():
    message="sopsdel"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)
    return render_template("index.html", title="Hello")
