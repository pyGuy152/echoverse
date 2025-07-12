import requests

def askAI(prompt):
    headers = {"Content-Type":"application/json"}
    data = {'messages':[{"role": "user", "content": prompt}]}
    response = requests.post("https://ai.hackclub.com/chat/completions",headers=headers,json=data)
    response.raise_for_status()
    output = response.json()
    return output['choices'][0]['message']['content']