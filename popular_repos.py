import requests
import pygal

while (True):
    print("This application returns a chart of popular Github repos by language.")
    language = input("Which programming language are you interested in? ")

    # make an API call and store the response
    url = 'https://api.github.com/search/repositories?q=language:' + language.lower() + '&sort=stars'
    r = requests.get(url)
    print('Status code:', r.status_code)
    if r.status_code == 200:
        with open('langauges.txt', 'a') as f:
            f.write(language + '\n')
        break
    print('Could not find requested language. Please try again.')

response_dict = r.json()
print('Total repositories:', response_dict['total_count'])
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

# examine top repos
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # value determines the height of the bar
    # xlink adds an active link to the bar
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url']
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
chart.title = 'Most-Starred' + language.title() + 'Projects on Github'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('popular_repos.svg')