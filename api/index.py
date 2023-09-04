from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/random')
def random():
    return redirect("https://youtu.be/dQw4w9WgXcQ")

if __name__ == "__main__":
    app.run(debug=True)
