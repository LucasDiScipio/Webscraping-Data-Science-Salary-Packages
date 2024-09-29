import os
import praw
from dotenv import load_dotenv

POSTS_DIRECTORY_PATH=os.path.join(os.getcwd(), "data", "posts")

def main():
    load_dotenv()
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
    )

    subreddit_name = "BESalary"
    queries = ("data analyst", "data scientist", "data engineer")
    for query in queries:
        query_dir = os.path.join(POSTS_DIRECTORY_PATH, query.replace(" ", "_"))
        if not os.path.exists(query_dir): 
            os.makedirs(query_dir)
        for submission in reddit.subreddit(subreddit_name).search(query=query, sort="new", limit=None):
            if submission.link_flair_text == "Salary":
                with open(os.path.join(query_dir, f"{submission.id}.txt"), "w", encoding="utf-8") as f:
                    f.write(submission.selftext)


if __name__ == "__main__":
    main()