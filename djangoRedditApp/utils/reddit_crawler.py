import os 
import praw
import json


class RedditCrawler():
    """Class created to communicate with Reddit API"""

    USERNAME="Django CrawlerApp"
    User_Agent = "your bot 0.1"
    REDDIT_SECRET=""
    REDDIT_CLIENTID=""
    FILENAME="utils/app_conf.json"

    conf = ""

    try:
        with open(FILENAME, 'r') as f:
            conf = json.load(f)
            REDDIT_SECRET = conf["Secret"]
            REDDIT_CLIENTID = conf["ClientID"]
    except FileNotFoundError as e:
        print("[ERROR]: Configuration file not found!")

    reddit = praw.Reddit(  
        client_id=REDDIT_CLIENTID,
        client_secret=REDDIT_SECRET,
        user_agent=User_Agent
    )

    @staticmethod
    def sub_exists(subreddit_name):
        exists = True
        try:
            RedditCrawler.reddit.subreddits.search_by_name(subreddit_name, exact=True)
        except Exception:
            print("[INFO]: Submitted subreddit ({subreddit_name}) doesn't exist!")
            exists = False
        return exists

    @staticmethod
    def get_posts_data(subreddit_name, limit=6):
        posts = []
        if subreddit_name == '':
            print("[ERROR]: Wrong subreddit name. Exiting program")
            return posts
        reddit_posts = RedditCrawler.reddit.subreddit(subreddit_name).top(limit=limit)
        for submission in reddit_posts:
            posts.append({"author": submission.author, "title": submission.title, "score": submission.score,
                "url": f"https://reddit.com{submission.permalink}", "image_url": submission.url})
        return posts

if __name__ == '__main__':
    print(f"[DEBUG]: Hi you are in {__name__}!")
    