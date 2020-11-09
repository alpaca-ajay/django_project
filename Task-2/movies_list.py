import requests, json

url = "https://api.themoviedb.org/3/search/person?api_key=f3a05026119d09f84c9aaef927a18ac2&language=en-US&query={}&page=1&include_adult=false"

# Pass any director name in query variable

query = "Quentin Tarantino"


'''
listsAllMovies func retrun all movies list in sorted order by release_date

'''

def listsAllMovies(url,query):
	response = requests.get(url.format(query))
	data_in_json = response.json()

	movies_list = data_in_json["results"][0]["known_for"]
	movies_list.sort(key = lambda x:x["release_date"],reverse=True)
	return movies_list

print(listsAllMovies(url,query))

