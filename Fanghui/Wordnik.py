from wordnik import *
import string

def main():
	apiUrl = 'http://api.wordnik.com/v4'
	apiKey = '63fe5ae2405ccfebff0315362680f2ee0d5bfc35df19b5208'
	client = swagger.ApiClient(apiKey, apiUrl)
	wordApi = WordApi.WordApi(client)
	# example = wordApi.getTopExample('irony')
	# print(example.text)
	# wordApi = WordApi.WordApi(client)
	# https://api.wordnik.com/v4/word.json/take/definitions?limit=5&includeRelated=false&useCanonical=false&includeTags=false&api_key=YOURAPIKEY
	
	# definition = wordApi.getDefinitions(word,limit = 10)
	
	# Human category
	
	
	
	word = input('Enter your input:')      # If you use Python 3
	print(type(word))
	findPattern(word)

def findPattern(word):
	apiUrl = 'http://api.wordnik.com/v4'
	apiKey = '63fe5ae2405ccfebff0315362680f2ee0d5bfc35df19b5208'
	client = swagger.ApiClient(apiKey, apiUrl)
	wordApi = WordApi.WordApi(client)
	examples = wordApi.getExamples(word,limit = 3)
	
	human = ["he","she","they","I","him","her","them","name"]
	
	for i in range(len(examples.examples)):
		text = examples.examples[i].text
		textWord = text.split(" ");
		print("print TextWord: ",textWord)
		for i in range(len(textWord)):
			w = textWord[i]
			if w == word:
				print("Word: ",w)
				if i>0:
					exclude = set(string.punctuation)
					wordBefore = ''.join(ch for ch in textWord[i-1] if ch not in exclude)
					 
					print("Word Before is: ",wordBefore)
					if wordBefore in human:
						print("<==exp human object bef")
						return
					defBef = wordApi.getDefinitions(wordBefore,limit = 1)
					for elt in defBef:
						eltWord = elt.text.split(" ")
						print("eltWord: ",eltWord)
						for eltw in eltWord:
							if eltw in human or eltw == "name":
								print("eltw: ", eltw)
								print("actor<==exp human object bef")
								break
				print("Finish first part")
				if i<len(textWord)-1:
					print("in")
					exclude = set(string.punctuation)
					wordAfter = ''.join(ch for ch in textWord[i+1] if ch not in exclude)
					
					print("Word After is: ",wordAfter)
					if wordAfter in human:
						print("<==exp human object aft")
						break
					defAft = wordApi.getDefinitions(wordAfter,limit = 1)
					for elt in defAft:
						eltWord = elt.text.split(" ")
						for eltw in eltWord:
							if eltw in human or eltw=="word":
								print("eltw: ", eltw)
								print("pbject<==exp human object aft")
								break
							
	
	
main()