#initiate Wolfram Alpha Answer Engine - Dev Edition
# Python 3.7.3 - proxy/interface

import wolframalpha
client = wolframalpha.Client("GPT6RK-WA3H4YJ7PV")

def runQuery(query):
	res = client.query(query)
	
	try:
		(next(res.results).text)
	except:
		return("QueryError: No results found on this query. The query could alsobe invalid")
	
	return (next(res.results).text)

#if called then run the function
if __name__ == '__main__':
	qIn = input('Enter query:	')
	print(runQuery(qIn))