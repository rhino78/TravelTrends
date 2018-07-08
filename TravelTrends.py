import csv

import praw
from iso3166 import countries

import PrawCreds

reddit = praw.Reddit(client_id=PrawCreds.client_id,
                     client_secret=PrawCreds.client_secret,
                     password=PrawCreds.password,
                     user_agent=PrawCreds.user_agent,
                     username=PrawCreds.username)

travel = []
for submission in reddit.subreddit('Travel').hot(limit=5000):
        travel.append(submission.title)

country_list = []
cities = []
country_dict = {}
city_dict = {}

for i in countries:
    country_list.append(i.name)

with open('world_cities.csv') as csvfile:
    rdr = csv.reader(csvfile, delimiter=',')
    for row in rdr:
        cities.append(row[0])


for i in countries:
    country_list.append(i.name)

cities.remove('Ho')
cities.remove('Wa')
cities.remove('Bo')
cities.remove('Mon')
cities.remove('San')
cities.remove('Bar')
cities.remove('Bor')
cities.remove('Best')

for t in travel:
    for c in country_list:
        if c in t:
            if c in country_dict:
                country_dict[c] = country_dict[c] + 1
            else:
                country_dict[c] = 1
    for c in cities:
        if c in t:
            if c in city_dict:
                city_dict[c] = city_dict[c] + 1
            else:
                city_dict[c] = 1


d_sorted = sorted(country_dict.items(), key=lambda x: x[1], reverse=True)
c_sorted = sorted(city_dict.items(), key=lambda x: x[1], reverse=True)

print('----------')

for k in range(0, 15):
    print(d_sorted[k])

print('----------')

for k in range(0, 15):
    print(c_sorted[k])
