import os 
import praw

REDDIT_SECRET=os.getenv("REDDIT_SECRET")
REDDIT_CLIENTID=os.getenv("REDDIT_CLIENTID")
USERNAME="Django CrawlerApp"
User_Agent = "your bot 0.1"

def main():
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENTID,
        client_secret=REDDIT_SECRET,
        user_agent=User_Agent
    )

    for post in reddit.subreddit("LittleNightmares").top(limit=10):
        print(f"TITLE: {post.title}")
        print(f"VOTES: {post.score}")


if __name__ == '__main__':
    main()
    