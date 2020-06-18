# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 14:54:20 2020

@author: Anes ABBAD

@website : https://abbadanes.github.io/

"""

from instaloader import Instaloader
from facebook_scraper import get_posts

class Connector():
    def __init__(self):
        self.youtube_key = "AIzaSyDWHObbnmXksvoz1AI9hOszswe3fSHvuqY"
        self.posts = []
        
    def get_posts(self,from_fb=True,from_instgram=True,from_yt=False,from_twitter=False,max_results_per_sn=50):
        if from_yt == True:
            from apiclient.discovery import build
            youtube = build("youtube", "v3",developerKey=self.youtube_key)
            search_response = youtube.search().list(q="décès jaques chirac", type="video", order = "relevance",
                                      part="snippet",maxResults=max_results_per_sn,).execute()
            videos = search_response["items"]
            items = []
            for i in videos:
                item = self.__parse_data([i["snippet"]["description"], i["snippet"]["channelTitle"], i["snippet"]["publishedAt"], i["snippet"]["thumbnails"]["high"]["url"], i["snippet"]["title"]],"Youtube")
                items.append(item)
            self.posts.extend(items)
        if from_instgram == True:
            loader = Instaloader()
            results = loader.get_hashtag_posts("jacques_chirac")
            feeds = []
            counter = 0
            for post in results:
                item = self.__parse_data([post.caption, post.owner_username, post.date_utc, post.url, None],"Instagram")
                counter = counter + 1
                if counter > max_results_per_sn:
                    break
                feeds.append(item)
            self.posts.extend(feeds)
        if from_twitter == True:
            import GetOldTweets3 as got
            tweetCriteria = got.manager.TweetCriteria().setQuerySearch('décès jaques chirac').setMaxTweets(max_results_per_sn)
            tweets = got.manager.TweetManager.getTweets(tweetCriteria)
            posts = []
            for tweet in tweets:
                item = self.__parse_data([tweet.text, tweet.username, tweet.date, tweet.urls, None],"Twitter")
                posts.append(item)
            self.posts.extend(posts)
        if from_fb == True:
            posts = []
            count = 0
            for post in get_posts('Jacques-Chirac-117785189620491', pages=100):
                item = self.__parse_data([post['text'], "pages", post['time'], post['image'], None],"Facebook")
                posts.append(item)
                count = count + 1
                if count > 50:
                    break
            self.posts.extend(posts)
            
        return self.posts
    
    def __parse_data(self,data,source):
        temp = {}
        temp["source"] = source
        temp["content"] = data[0]
        temp["publisher"] = data[1]
        temp["published_at"] = data[2]
        temp["picture"] = data[3]
        temp["title"] = data[4]
        return temp
        
        
