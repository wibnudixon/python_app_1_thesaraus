import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
       return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn=input("Did you mean %s instead? Enter Y if yes, or No if no:" % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesnt exist"
        else:
            return "We didnt uncerstand your query"
    else:
        return "The word does not exist.PLease double check your word"

        

word = input("Enter word :")

print(translate(word))