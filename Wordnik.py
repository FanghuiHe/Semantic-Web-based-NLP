from wordnik import *
def main():
	apiUrl = 'http://api.wordnik.com/v4'
	apiKey = '63fe5ae2405ccfebff0315362680f2ee0d5bfc35df19b5208'
	client = swagger.ApiClient(apiKey, apiUrl)
	wordApi = WordApi.WordApi(client)
	# example = wordApi.getTopExample('irony')
	# print(example.text)
	# wordApi = WordApi.WordApi(client)
	# https://api.wordnik.com/v4/word.json/take/definitions?limit=5&includeRelated=false&useCanonical=false&includeTags=false&api_key=YOURAPIKEY
	definitions = wordApi.getDefinitions('take',limit = 10)
	for elt in definitions:
		print(elt.text)
	
	
main()