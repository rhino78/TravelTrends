import praw
from iso3166 import countries

reddit = praw.Reddit(client_id='JgiAaoEUbf86tA',
                     client_secret='bz4rt2sUhhQs0suOR_2uq4QuIhA',
                     password='thomas08',
                     user_agent='testscript by /u/rhino_78',
                     username='rhino_78')

travel = []
for submission in reddit.subreddit('Travel').hot(limit=5000):
        travel.append(submission.title)

c = []
d = {}
d["none"] = 0
for i in countries:
    c.append(i.name)

for t in travel:
    foundone = False
    for word in t.split(' '):
        if word in c:
            foundone = True
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
    if not foundone:
        d["none"] = d["none"] + 1


d_sorted = sorted(d.items(), key=lambda x: x[1], reverse=True)
for k in d_sorted:
    print(k)




