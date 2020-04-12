import twitter
import json



with open('key.json','r') as f:
    keys = json.load(f)

api = twitter.Api(consumer_key=keys["consumer key"],
                  consumer_secret= keys["consumer secret"],
                  access_token_key= keys["access token"],
                  access_token_secret= keys["access token secret"])

results = api.GetSearch(raw_query="q=%24%%20&result_type=recent&since=2014-07-19&count=100")

print(results)
