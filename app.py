from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#Use the following code to run the application on local development and start the app
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
