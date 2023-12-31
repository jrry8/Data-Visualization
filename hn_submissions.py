import pygal
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

names, plot_dicts = [], []
for submission_dict in submission_dicts:
    print('\nTitle:', submission_dict['title'])
    print('Discussion link:', submission_dict['link'])
    print('Comments:', submission_dict['comments'])
    names.append(submission_dict['title'])
    plot_dict = {
        'value': submission_dict['comments'],
        'xlink': submission_dict['link']
    }
    plot_dicts.append(plot_dict)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config)
chart.title = 'Most Active Discussions on Hacker News'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('hn_submissions.svg')
