# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Studying ISP has been a great experience for me because it helps me understand how real software systems are built. - Nisara Ploysuttipol"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)
