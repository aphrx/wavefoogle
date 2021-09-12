import requests
import psycopg2
import config as config
from youtube_transcript_api import YouTubeTranscriptApi

con = psycopg2.connect(database=config.DB_DATABASE, user=config.DB_USER, password=config.DB_PASS, host=config.DB_HOST, port="5432")
cur = con.cursor()

REPLACE_DICT = {
    "marquez": "Marques",
    "apple": "Apple",
    "andrew": "Andrew",
    "tesla": "Tesla",
    "google": "Google",
    "samsung": "Samsung",
    "iphone": 'iPhone',
    "doug": 'Doug',
    "demuro": 'DeMuro',
    "porsche": 'Porsche',
}

def create_tables():
    cur.execute("""
        CREATE TABLE public.video
        (
            "videoId" text COLLATE pg_catalog.default NOT NULL,
            "videoTitle" text COLLATE pg_catalog.default NOT NULL,
            "datePosted" date,
            CONSTRAINT video_pkey PRIMARY KEY ("videoId")
        );
        CREATE TABLE public.transcript
        (
            id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 0 MINVALUE 0 MAXVALUE 2147483647 CACHE 1 ),
            "startTime" integer NOT NULL,
            caption text COLLATE pg_catalog."default" NOT NULL,
            "videoId" text COLLATE pg_catalog."default" NOT NULL,
            CONSTRAINT transcript_pkey PRIMARY KEY (id)
        );
        """)

def insert_video_details(d):
    cur.execute("""
        INSERT INTO public.video(
        "videoId", "videoTitle", "datePosted")
        VALUES (%s, %s, %s);
    """, (d['id']['videoId'], d['snippet']['title'], d['snippet']['publishedAt'][:10]))

def insert_captions(videoId):
    list =  None
    try:
        list = YouTubeTranscriptApi.get_transcript(videoId)
    except:
        return
    for caption in list:
        print(caption['text'])
        text = caption['text']
        for orig, replacement in REPLACE_DICT.items():
            text = text.replace(orig, replacement)
        cur.execute("""
            INSERT INTO public.transcript(
            "startTime", caption, "videoId")
            VALUES (%s, %s, %s);
        """, (int(caption['start']), text, videoId))

def get_channel_details():
    return requests.get(f"https://www.googleapis.com/youtube/v3/search?key={config.API_KEY}&channelId={config.CHANNEL_ID}&part=snippet,id&order=date&maxResults=50")

def run():
    response = get_channel_details()
    print(response.status_code)

    if response.status_code == 200:
        data = response.json()
        for d in data['items']:
            if d['id']['kind'] == 'youtube#video':
                cur.execute("SELECT * FROM public.video")
                row = [item[0] for item in cur.fetchall()]
                #print(row)
                insert_captions(d['id']['videoId'])
                insert_video_details(d)


#create_tables()
run()
con.commit()
con.close()





