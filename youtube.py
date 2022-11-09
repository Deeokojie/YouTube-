from typing import ValuesView
import requests 
import pandas as pd
import time 

# API key needed

API_KEY = 'AIzaSyCD2-hRGpl1wszaXQpwyxxsaPVl_RA_RgI'
channel_id = 'UCS56RICRuwlgWQV0SeqaglA'
def get_videos(df):

#test API call
    response = requests.get("https://api.github.com").json()

    url = 'https://www.googleapis.com/youtube/v3/search'+API_KEY+"&channel_id="+channel_id+"&parts=snippet,id&order= date&maxresults=1000"+pagetoken

    response ['items'][0]['videoid']
    video_id = response['items'][0]['videoid']

    upload_date = response['items'][0]['snippet']['published']
    upload_date = str(upload_date).split("T")[0]


     #build data frame

    df = pd.dataframe(columns = ["video_id", "video_tittle", "upload_date", "view_count", "like_count", "dislike_count", "comment_count"])

    df = get_videos(df)

    def get_video_details(videos_id):

    #second API call
    # collecting view, like, dislike, comment

        url_video_stats = "https://www.googleapis.com/youtube/v3/videos?id="+video_id+"&part=statistics&key="+API_KEY
            
    response_video_stats = requests.get(url_video_stats).json()
            
    view_count = response_video_stats['items'][0]['statistics']['viewcount']
    like_count = response_video_stats['items'][0]['statistics']['likecount']
    dislike_count = response_video_stats['items'][0]['statistics']['dislikecount']
    comment_count = response_video_stats['items'][0]['statistics']['commentcount']

    return view_count, like_count, dislike_count, comment_count

    
    
def get_videos(df):
        #make api call
        pagetoken = ""
url= 'https://www.googleapis.com/youtube/v3/search'

response = requests.get(url).json()

time.sleep(1)

for video in response ['items']:
        if video ['id']['kind'] == "youtube#video":
            video_id = video ['id']['videoid']
            video_tittle = video['snippet']['tittle']
            upload_date = video['snippet']['publishedAt']
            upload_date = str(upload_date).split("T")[0]

            view_count, like_count, dislike_count, comment_count = get.video.details(video_id)
            #save data in pandas df
            df = df.append({'video_id': video_id, 'video_tittle': video_tittle,
             'upload_date': upload_date, 'view_count': view_count, 'like_count': like_count,
              'dislike_count': dislike_count, 'comment_count': comment_count}, ignore_index=True)

        print(df)
        



 





            

           

           


















