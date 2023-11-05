from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("dictionary.csv")
df = df[["word"]]


@app.route("/")
def home():
    return render_template("home.html",data=df.to_html())


@app.route("/api/v1/<word>/")
def api(word):
    definition = df.loc[df['word'] == word]['definition'].squeeze()
    dict = {"word": word, "definition":definition }
    return dict


if __name__ == "__main__":
    app.run(debug=True, port = 5001)