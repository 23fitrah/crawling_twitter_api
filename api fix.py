import tweepy,jsonpickle,json

ACCESS_TOKEN = '177761429-eSe8cuVnvL8y4r3pMU0J4tc9G50BeXhncgBnZiaF'
ACCESS_SECRET = 'NunlqWeP8VCdlavxv8tvOlQbkdmi6xgVjf9q6XIWvsMFY'
CONSUMER_KEY = 'zduGTJ6z16uyPwxUiPFfLrNDQ'
CONSUMER_SECRET = 'afUu3u8RfHNsiuhvurMqnJ979WO7xS514kO0yZVKxf1jr8Oypt'

file = open("result.json","w")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

public_tweets = api.search('Tangerang',count=100)
result=[];
for tweet in public_tweets:
   result.append(tweet._json);
json.dump(result,file,indent=4);
file.close();
#file.write(jsonpickle.encode(tweet._json, unpicklable=False) +'\n')

#for status in tweepy.Cursor(api.home_timeline).items(10):
#    print status.text

#for friend in tweepy.Cursor(api.friends).items(2):
#   file.write(jsonpickle.encode(friend._json, unpicklable=False))

with open('result.json','r') as f:
     geo_data = {
        "type": "FeatureCollection",
        "features": []
    }
     tweets=json.loads(f.read());
     for tweet in tweets:
          if tweet['coordinates']:
             geo_json_feature = {
                "type": "Feature",
                "geometry": tweet['coordinates'],
                "properties": {
                    "text": tweet['text'],
                    "created_at": tweet['created_at']
                }
             }
             geo_data['features'].append(geo_json_feature);
             #print geo_data['features'];
             with open('geo_data.json','w') as fout:
                json.dumps(geo_data,fout,indent=4);
