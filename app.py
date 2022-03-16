import requests as reqs
import os
import pandas as pd
import json

url = "https://api.twitter.com/2/tweets/search/recent?query=from:ryebreadnyc&tweet.fields=created_at,geo"

bearer_token = os.environ['TWITTER_BEARER_TOKEN']
hed = {'Authorization': 'Bearer ' + bearer_token}
response = reqs.get(url, headers = hed)

data_dict = json.loads(response.content.decode('utf8'))
data = pd.DataFrame(data_dict['data'])
til_tweets = data[data['text'].str.startswith('TIL')]
print(til_tweets)
