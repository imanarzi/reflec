import requests
import json

if __name__ == "__main__":
    print("\n\n\nBeginning of Transcript:\n\n\n")
    url = 'https://reflec-46d2b.firebaseio.com/izzi.json'
    response = requests.get(url = url)
    react_data = response.json()
    # print(react_data)
    url = 'https://reflec-46d2b.firebaseio.com/speech.json'
    response = requests.get(url = url)
    speech_data = response.json()
    # print(speech_data)
    react_seconds = list(react_data.keys()) 
    speech_seconds = list(speech_data.keys())
    j = 0
    #print(j)
    for i in range(len(speech_seconds)):
        speech_values = list(speech_data.values())
        if i >= len(speech_values):
            break
        linecase = str(list(speech_values[i].values())[1])
        if j < len(react_seconds):
            #print(j)
            react_values = list(react_data.values())
            while int(react_seconds[j]) <= int(speech_seconds[i]) :
                linecase += str(" *")
                linecase += list(react_values[j].values())[0]
                linecase += "* "
                j += 1
        print(linecase)
        print("")
    
    # string = list(speech_values[-1].values())[1]
    # while(j < len(react_seconds)):
    #     string += " *" + list(react_values[j].values())[0] + "* "
    #     j += 1
    # print(string)

    # apple = {'1581245767530': {'success': True, 'transcription': 'when you choose and honest beverage'}, '1581245779084': {'success': True, 'transcription': "organic and fair-trade certified p.m. ingredients you're making a small decision that creates"}}
    # apple = speech_data
    # something = list(apple.values())
    # print(list(something[0].values())[1])

# tup1 = ('physics', ('chemistry', 1997, 2000))
# print(tup1[1])
# print(tup1[1][1])

# {'1581260050035': {'reaction': 'confused'}, '1581260050463': {'reaction': 'confused'}, '1581260060338': {'reaction': 'laughing'}, '1581260060491': {'reaction': 'laughing'}, '1581260060652': {'reaction': 'laughing'}, '1581260060838': {'reaction': 'laughing'}, '1581260061804': {'reaction': 'smiley'}, '1581260065459': {'reaction': 'lost'}, '1581260075186': {'reaction': 'laughing'}, '1581260075693': {'reaction': 'laughing'}, '1581260076202': {'reaction': 'love'}, '1581260077880': {'reaction': 'love'}, '1581260078124': {'reaction': 'love'}, '1581260079515': {'reaction': 'sad'}, '1581260079871': {'reaction': 'sad'}, '1581260080193': {'reaction': 'sad'}, '1581260080492': {'reaction': 'sad'}, '1581260080654': {'reaction': 'sad'}, '1581260080807': {'reaction': 'sad'}, '1581260081099': {'reaction': 'sad'}, '1581260081236': {'reaction': 'sad'}, '1581260081372': {'reaction': 'sad'}, '1581260081525': {'reaction': 'sad'}, '1581260081686': {'reaction': 'sad'}, '1581260083485': {'reaction': 'sad'}, '1581260084097': {'reaction': 'lost'}, '1581260084783': {'reaction': 'lost'}, '1581260085309': {'reaction': 'lost'}, '1581260091246': {'reaction': 'confused'}, '1581260091602': {'reaction': 'confused'}, '1581260092304': {'reaction': 'confused'}, '1581260092974': {'reaction': 'confused'}, '1581260093167': {'reaction': 'confused'}, '1581260093360': {'reaction': 'confused'}, '1581260093554': {'reaction': 'confused'}, '1581260096361': {'reaction': 'sad'}, '1581260097184': {'reaction': 'sad'}, '1581260097829': {'reaction': 'sad'}, '1581260104068': {'reaction': 'lost'}, '1581260104529': {'reaction': 'lost'}, '1581260104706': {'reaction': 'lost'}, '1581260104917': {'reaction': 'lost'}, '1581260109531': {'reaction': 'smiley'}, '1581260110082': {'reaction': 'smiley'}, '1581260113354': {'reaction': 'sad'}, '1581260113669': {'reaction': 'sad'}, '1581260114053': {'reaction': 'sad'}, '1581260114313': {'reaction': 'sad'}, '1581260114597': {'reaction': 'sad'}, '1581260114879': {'reaction': 'sad'}, '1581260115210': {'reaction': 'sad'}, '1581260115792': {'reaction': 'sad'}, '1581260116902': {'reaction': 'sad'}, '1581260122537': {'reaction': 'sad'}, '1581260122738': {'reaction': 'sad'}, '1581260122982': {'reaction': 'sad'}, '1581260130891': {'reaction': 'sad'}}
# {'1581260053685': {'success': True, 'transcription': "I don't want"}, '1581260057271': {'error': 'Unable to recognize speech', 'success': True}, '1581260067509': {'success': True, 'transcription': 'this freaking potato chip bag'}, '1581260086866': {'success': True, 'transcription': "if you don't work I will beat you up"}, '1581260098692': {'success': True, 'transcription': 'that we are going to fight and actually'}, '1581260104170': {'success': True, 'transcription': "if you don't generate"}, '1581260107754': {'success': True, 'transcription': 'data'}}