#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ---------------------------------------
# Professional Cycling - Data to Text
# ---------------------------------------
#
# GetTweets.py
#   Makes use of the tweepy package. 
#   This .py gets all the Twitter data for any race that's entered. Eg. 2015 Tour de France
# ----------------------------------------
#
import tweepy, csv
from tweepy import OAuthHandler
 
class GetTweets():
    def getting_query_result(self, query):
        consumer_key = 'mRJGFxAWklN3ffMzNnbbPwmyi'
        consumer_secret = 'nGSxb13owzSxfSaFofSyTVtziL6PZYmaqpbR0CdUbCJYeU5VYz'
        access_token_raw = '78868741-ioDSiXl5FvBcd6CDqGgBLLul7elMFLbtLFyDdgOwu'
        access_token = access_token_raw.encode('utf-8')
        access_secret = 'EnsD9n880W0TWD6G8pJ5C8n9FUqafi7AdPFszC2IH8ysF'
        
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        
        api = tweepy.API(auth)
    
        csvFile = open('E:/PythonProjects/CyclingDataToText/tweet.csv', 'wb+')
        
        csvWriter = csv.writer(csvFile)
        
        # print api.rate_limit_status()
        # print ""
        # query = raw_input("Enter a query search term: ")
       
        for tweet in tweepy.Cursor(api.search, 
                            q=query, 
                            show_user = False, 
                            lang="en").items(500):
            csvWriter.writerow([tweet.text.encode('utf-8')])
            #print tweet.text.encode('utf-8')
        print "Saved sample tweets from query in tweet.csv"
        csvFile.close()
        
def main():
    f = GetTweets()
    f.getting_query_result("2015 Tour de France")

main()