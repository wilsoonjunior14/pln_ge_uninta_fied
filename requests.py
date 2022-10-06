import requests
import json

headers = { 'Authorization' : 'Bearer AAAAAAAAAAAAAAAAAAAAAEd4gwEAAAAAycbDIptmlB6UuCa8%2FI1uRWelsC4%3Df2RCGCZzu0KtTA4ozeLWzYLjXFUTtB6Er9JKzC7MqckZTJ5Ofr'}

print (headers)

x = requests.get('https://api.twitter.com/2/tweets/search/recent?query=politica&tweet.fields=lang', headers=headers)

print(len(json.loads(x.text)["data"]))

for i in range(0, len(json.loads(x.text)["data"])):
    print (json.loads(x.text)["data"][i]["text"])
    print (json.loads(x.text)["data"][i]["lang"])
    print ("\n")
