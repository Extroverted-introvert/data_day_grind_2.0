import tweepy


def get_tweet_sentiment(city):
        
    auth = tweepy.OAuthHandler("Blank", "Blank")
    auth.set_access_token("Blank", "Blank")

    api = tweepy.API(auth)
    try:
        places = api.search_geo(query=city, granularity="city")
    except:
        places = api.search_geo(query="Delhi", granularity="city")    
    place_id = places[0].id
    print(place_id)
    tweets = api.search_tweets(q="covid-19 OR covid OR vaccination OR virus place:{} lang:en -has:links -has:media -has:images -has:videos -is:retweet".format(place_id), tweet_mode="extended")
    return tweets
