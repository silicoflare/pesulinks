import json

finale = """from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

"""

with open('data/data.json') as file:
    data = json.loads(file.read())

for l in data.get('links'):
    finale += f"""@app.route('{l.get('endpoint')}')
def {l.get('name')}():
    return redirect("{l.get('link')}")

"""

# finale += """if __name__ == "__main__":
#     app.run(debug=True)
# """


with open('api/index.py', 'w') as file:
    file.write(finale)