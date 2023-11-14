from flask import Flask, jsonify
import random

app = Flask(__name__)


@app.route('/random_trivia', methods=['GET'])
def get_random_trivia():

    print("Request received")
    with open('weather_facts.txt', 'r') as file:
        lines = file.readlines()
        random_trivia = random.choice(lines).strip()

    return jsonify(trivia=random_trivia)


if __name__ == "__main__":
    app.run(port=5000)