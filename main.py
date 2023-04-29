import tweepy
import datetime
import json

ACCESS_KEY = '1649342617400885251-HYC9IY7ecJ6XRuj7WUhHnSkD9MmMLX'
ACCESS_SECRET = 'HfYJLXZ6R4d2d3Lwrcc2U3fbGCDDKpOUDDMTA6HnvY7QK'
CONSUMER_KEY = 'W8z2SCyZUcYKC4onnSm3HvY0V'
CONSUMER_SECRET = 'l1Nk5nY7SKuszc9xVIqGDFj8tCk8qxjewLsM8MyRxEo9LLHSWy'
BEARER_TOKEN = r"AAAAAAAAAAAAAAAAAAAAAIiHmwEAAAAAeteZUItJUXCpMVX1sEbMuSu6vZU%3DXDTUVHkrMcyd0lCAC3XRWZjBGfUx7XnMkORW08TuskGsIGabuG"


client = tweepy.Client(bearer_token=BEARER_TOKEN,
                    consumer_key=CONSUMER_KEY,
                    consumer_secret=CONSUMER_SECRET,
                    access_token=ACCESS_KEY,
                    access_token_secret=ACCESS_SECRET)

auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

print("API active")


date = datetime.datetime.now().strftime("%m-%d")
with open("bday.json") as json_file:
        data = json.load(json_file)["operators"]
namelist = []

def tweet():
    for i in range(len(data)):
        if(date == data[i]["day"]):
            namelist.append(data[i]["name"])

    if (len(namelist)== 0):
        return print("No operator has their birthday today :(")
    
    for name in namelist:
        text = f'Happy Birthday {name}!'
        img = f"r6-operators-list-{name.lower()}.png"

        print(text)
        
        mediaID = api.media_upload(f"img/{img}")
        client.create_tweet(text=text, media_ids=[mediaID.media_id])
    
    print("Tweeted successfully")

tweet()