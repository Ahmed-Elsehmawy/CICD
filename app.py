from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Azure CI/CD with the flask!"

@app.route("/loop")
def loop():
    for i in range (1000000):
        print(i)
    return ("Loop is completed")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
    
