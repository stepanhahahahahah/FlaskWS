from flask import Flask, request, redirect, render_template
import api

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.j2',image=api.getapi())

def main():
    app.run("0.0.0.0", 8000, True)

if __name__ == "__main__":
    main()