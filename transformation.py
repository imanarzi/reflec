import requests
import json

if __name__ == "__main__":
    url = 'https://reflec-46d2b.firebaseio.com/izzi.json'
    response = requests.get(url = url)
    react_data = response.json()
    #print(react_data)
    #react_seconds = list(react_data.keys()) 
    #print(react_seconds[0])
    url = 'https://reflec-46d2b.firebaseio.com/speech.json'
    response = requests.get(url = url)
    speech_data = response.json()
    #print (speech_data)
   # for i in range(react_data[0]): iterate through these keys and search in the range of emotion keys
    #    for i
    #    we were thirsty \t \t happy happy sad