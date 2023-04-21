import tweepy
import datetime
import json

client = tweepy.Client(bearer_token=BEARER_TOKEN,
                    consumer_key=CONSUMER_KEY,
                    consumer_secret=CONSUMER_SECRET,
                    access_token=ACCESS_KEY,
                    access_token_secret=ACCESS_SECRET)

auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


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

        mediaID = api.media_upload(f"img/{img}")
        client.create_tweet(text=text, media_ids=[mediaID.media_id])

tweet()
