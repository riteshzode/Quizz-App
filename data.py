import requests

parameter = {
    "amount": 10,
    "category": 18,
    "type": "boolean",
}

request = requests.get(url="https://opentdb.com/api.php?", params=parameter)
request.raise_for_status()

question_data = request.json()['results']


