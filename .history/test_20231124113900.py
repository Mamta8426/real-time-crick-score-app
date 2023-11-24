import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

headers = {
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com",
        "X-RapidAPI-Key": "d313f6989dmsh7b393da34ef3c81p16408ajsn9baeb880e3a2"  # Replace with your RapidAPI key
    }
response = requests.get(url, headers=headers)
print(response.json())
  
