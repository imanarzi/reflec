import requests
import json

if __name__ == "__main__":
    url = 'https://reflec-46d2b.firebaseio.com/izzi.json'
    response = requests.get(url = url)
    react_data = response.json()
    # print(react_data)
    url = 'https://reflec-46d2b.firebaseio.com/speech.json'
    response = requests.get(url = url)
    speech_data = response.json()
    # print(speech_data)
    react_seconds = list(react_data.keys()) 
    speech_seconds = list(react_data.keys())
    j = 0
    for i in range(len(speech_seconds)):
        speech_values = list(speech_data.values())
        if i >= len(speech_values):
            break
        linecase = list(speech_values[i].values())[1]
        while j < len(react_seconds):
            react_values = list(react_data.values())
            if int(react_seconds[j]) <= int(speech_seconds[i]):
                linecase += " *"
                linecase += list(react_values[j].values())[0]
                linecase += "* "
            j += 1
        print(linecase)

    # apple = {'1581245767530': {'success': True, 'transcription': 'when you choose and honest beverage'}, '1581245779084': {'success': True, 'transcription': "organic and fair-trade certified p.m. ingredients you're making a small decision that creates"}}
    # apple = speech_data
    # something = list(apple.values())
    # print(list(something[0].values())[1])

# tup1 = ('physics', ('chemistry', 1997, 2000))
# print(tup1[1])
# print(tup1[1][1])
