# daily.py
--------------------------------------------

## Purpose

daily.py grabs the titles from a list of subreddits you can customize 
using the praw library in python and the Reddit API for authentication.

It is meant to be a simple CLI tool for listing some information from the internet.
The script is called daily as its meant to be called once daily, to update you 
on whatever you would like to see. 

## Implementation

The script imports the authentication object which is just called 'reddit' from a 
file called key.py. To create credentials, create an app with a Reddit account.

[Create a Reddit App](https://old.reddit.com/prefs/apps/)

Then update the following code in the *key.py* file
```python
import praw 

reddit = praw.Reddit(
    client_id="AppID",
    client_secret="AppSecretKey",
    password="RedditAccountPassword",
    user_agent="Description",
    username="RedditUsername"
)
```

Now you're all set to run the script! If you want to be fancy, you can add 
a command to your *.bashrc* file to run the script as well. Here is my example:

```bash 
alias daily="python3 ~/python/daily/daily.py"
```

## Example Output

Thanks for running the DAILY script! Here's your daily Reddit feed:

   From r/news

-> Chechen warlord accuses Elon Musk of ‘remotely disabling’ his Cybertruck

-> FTC sues drug middlemen for allegedly inflating insulin prices

-> Flight diverted after passenger finds live mouse in meal


   From r/stocks

-> Intel approached by Qualcomm for a possible takeover of chip design business -- WSJ

-> FTC sues drug middlemen (UNH, CVS, CI) for allegedly inflating insulin prices

-> A Three Mile Island nuclear reactor could restart under a new deal with Microsoft

