from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask running in Docker!"

if __name__ == "__main__":
    # Bind to 0.0.0.0 so it’s accessible externally
    app.run(host="0.0.0.0", port=8080)

