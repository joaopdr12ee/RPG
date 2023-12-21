from flask import Flask, redirect, render_template, request

app = Flask(__name__, template_folder='template')

@app.route('/')

def login():
    render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
