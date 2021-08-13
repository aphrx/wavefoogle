import requests
import psycopg2
import config as config
from youtube_transcript_api import YouTubeTranscriptApi

con = psycopg2.connect(database="waveform", user="postgres", password=config.DB_PASS, host="127.0.0.1", port="5432")
cur = con.cursor()

def insert_video_details(d):
    cur.execute("""
        INSERT INTO public.video(
        "videoId", "videoTitle", "datePosted")
        VALUES (%s, %s, %s);
    """, (d['id']['videoId'], d['snippet']['title'], d['snippet']['publishedAt'][:10]))

def insert_captions(videoId):
    list = YouTubeTranscriptApi.get_transcript(videoId)
    for caption in list:
        print(caption['text'])
        cur.execute("""
            INSERT INTO public.transcript(
            "startTime", caption, "videoId")
            VALUES (%s, %s, %s);
        """, (int(caption['start']), caption['text'], videoId))

def get_channel_details():
    return requests.get(f"https://www.googleapis.com/youtube/v3/search?key={config.API_KEY}&channelId={config.CHANNEL_ID}&part=snippet,id&order=date&maxResults=50")

def run():
    response = get_channel_details()
    print(response.status_code)

    if response.status_code == 200:
        data = response.json()
        for d in data['items']:
            print(d)
            if d['id']['kind'] == 'youtube#video':
                insert_video_details(d)
                insert_captions(d['id']['videoId'])

    con.commit()
    con.close()

run()



