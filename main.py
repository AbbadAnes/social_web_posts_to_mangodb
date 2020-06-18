# -*- coding: utf-8 -*-
"""
@author: Anes ABBAD
"""

from modules.Database import Database as DB
from modules.Connector import Connector

"""
To run the code correctly, please make sur you have the following librairies :

!pip install pymongo
!pip install instaloader
!pip install facebook_scraper

To run the bonus i.e Using Youtube API and Scrap from twitter,
please make sur you have the following librairies, and don't forget to turn FROM_YT and FROM_twitter to TRUE

!pip install apiclient
!pip install --upgrade google-api-python-client
!pip install GetOldTweets3

"""


def main():
    #Create the Database and the collection
    db = DB(db_name="Kaisens_data_Jacques_chirac",client="mongodb://localhost:27017/")
    collection = db.create_collection(name="posts")
    
    #Get Data From Social Networks API
    cnt = Connector()
    posts = cnt.get_posts(from_fb=True, from_instgram=True,
                          from_yt=False, from_twitter=False, max_results_per_sn=20)
    
    #Store the social web posts on our MongoDB database
    db.store(collection,posts)

if __name__ == "__main__":
    main()

