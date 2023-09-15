import requests

url = "https://chatgpt-chatgpt3-5-chatgpt4.p.rapidapi.com/v1/chat/completions"


def new_text(teext):
    payload = {
	    "model": "gpt-3.5-turbo",
	    "messages": [
		    {
			    "role": "user",
			    "content": teext
		    }
	    ],
	    "temperature": 0.8
    }
    headers = {
    	"content-type": "application/json",
    	"X-RapidAPI-Key": "498c5e5108mshb898ed543cf291ap1e5557jsnf29b89295af5",
    	"X-RapidAPI-Host": "chatgpt-chatgpt3-5-chatgpt4.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    text = response.json()['choices'][0]['message']['content']
    return text