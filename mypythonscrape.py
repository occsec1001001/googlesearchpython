#!/usr/bin/env python

# prior to using, I used pip install beautifulsoup4 and pip install googlesearch in bash to insure already installed as I use these elsewhere.

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

query = "site:ENTER-YOUR-URL-HERE filetype:xls OR filetype:csv -ppt -doc -docx"
mydict = {'filter' : '0'}

for j in search(query, tld="co.uk",lang='en', start=0, stop=1000, num=50, pause=30,extra_params=mydict,user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'):
  print(j)

# my use has been as example:
# python mypythonscrape.py >> mylinks.list
# which I can then use in terminal to manipulate
# eg renaming and sending upto GCP storage with gsutil cp *.xls gs://mybucket

# I am still refining this code, as on large results I get HTTP Error 429: Too Many Requests - so I will look to create a loop and rotate my 2 hop VPN and change the user_agent
# the timing pause does not seem to counteract when I have c.500+ files I am looking to strip from a website.
