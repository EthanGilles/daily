import praw
import sys
import re
sys.path.append("..") 
from key import *

print("\033[0;35m\n Thanks for running the\033[0;31m DAILY\033[0;35m script! Here's your daily Reddit feed: \033[0m \n \n \n")

file = open("subreddits.txt", "r")
contents = file.read()
subreddits = []
quoted = re.compile('"[^"]*"')
for string in quoted.findall(contents):
    subreddits.append(string[1:len(string)-1])

for subreddit in subreddits:
    interesting = reddit.subreddit(subreddit)
    interesting = interesting.hot(limit=5)
    print(f"\033[1;31m   From r/{subreddit} \033[0m \n")
    for i, submission in enumerate(interesting):
        if(i > 1 and i < 5):
            print(f"-> {submission.title}")
    print()
