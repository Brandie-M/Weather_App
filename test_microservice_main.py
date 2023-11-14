import requests


def get_random_trivia():
    response = requests.get("http://localhost:5000/random_trivia")

    if response.status_code == 200:
        print("Requesting Random Trivia")
        trivia = response.json().get("trivia")
        return trivia
    else:
        print("failed to get trivia")
        return None


random_trivia = get_random_trivia()
if random_trivia is not None:
    print("Random trivia: ", random_trivia)


