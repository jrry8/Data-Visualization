import requests
from operator import itemgetter

# API call to get top stories
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('topstories status code:', r.status_code)

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # API call for each top story
    url = 'https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json'
    submission_r = requests.get(url)
    print('id ' + str(submission_id) + ' status code:', submission_r.status_code)
    response_dict = submission_r.json()
    submission_dict = {
        'title': response_dict['title'],
        'link':  'http://news.ycombinator.com/item?id=' + str(submission_id), 
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

# sort stories in descending order based on number of comments
submission_dicts.sort(key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print('\nTitle:', submission_dict['title'])
    print('Discussion link:', submission_dict['link'])
    print('Comments:', submission_dict['comments'])