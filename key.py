import praw 

reddit = praw.Reddit(
    client_id="AppID",
    client_secret="AppSecretKey",
    password="RedditAccountPassword",
    user_agent="Description",
    username="RedditUsername"
)
