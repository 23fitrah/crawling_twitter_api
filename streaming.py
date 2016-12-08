from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#import jsonpickle
import json

ACCESS_TOKEN = '177761429-eSe8cuVnvL8y4r3pMU0J4tc9G50BeXhncgBnZiaF'
ACCESS_SECRET = 'NunlqWeP8VCdlavxv8tvOlQbkdmi6xgVjf9q6XIWvsMFY'
CONSUMER_KEY = 'zduGTJ6z16uyPwxUiPFfLrNDQ'
CONSUMER_SECRET = 'afUu3u8RfHNsiuhvurMqnJ979WO7xS514kO0yZVKxf1jr8Oypt'
global result;
result=[];
class listener(StreamListener):
    def on_data(self,data):
        decode=json.loads(data)
        file = open("result_streaming.json","wb")
        json.dump(decode,file,indent=4,sort_keys=True)
        file.close()
        return True
    def on_error(self,status):
        print status

auth=OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

twitterStream=Stream(auth,listener())
twitterStream.filter(track=["Ahok"])
