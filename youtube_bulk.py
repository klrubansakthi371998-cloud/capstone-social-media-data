from googleapiclient.discovery import build
import pandas as pd
import time

# Replace with your API key
API_KEY = "AIzaSyCrooYGBZwYutOFowJ8XZw_ZHbkSJSYsn8"

youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)

keywords = [
    "ChatGPT",
    "AI Agents",
    "Automation",
    "AWS",
    "Databricks",
    "Data Engineering",
    "Digital Marketing",
    "SEO",
    "Influencer Marketing",
    "Startup",
    "SaaS",
    "Digital Transformation"
]

data = []

for keyword in keywords:

    print(f"\nSearching: {keyword}")

    try:
        search_response = youtube.search().list(
            q=keyword,
            part="snippet",
            type="video",
            maxResults=10
        ).execute()

        for video in search_response["items"]:

            # Skip non-video results
            if "videoId" not in video["id"]:
                continue

            video_id = video["id"]["videoId"]
            video_title = video["snippet"]["title"]

            try:
                comments_response = youtube.commentThreads().list(
                    part="snippet",
                    videoId=video_id,
                    maxResults=50
                ).execute()

                for comment in comments_response["items"]:

                    c = comment["snippet"]["topLevelComment"]["snippet"]

                    data.append({
                        "Keyword": keyword,
                        "Video ID": video_id,
                        "Video Title": video_title,
                        "Comment Text": c["textDisplay"],
                        "Author": c["authorDisplayName"],
                        "Published Date": c["publishedAt"],
                        "Like Count": c["likeCount"]
                    })

                print("Collected:", len(data))

            except Exception as e:
                print("Comment Error:", e)

            time.sleep(1)

    except Exception as e:
        print("Search Error:", e)

# Save dataset
df = pd.DataFrame(data)

df.to_csv(
    "youtube_master_dataset.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nDONE!")
print("Total Records:", len(df))