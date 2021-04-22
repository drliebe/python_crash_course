import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

def get_repo_list(url=
    'https://api.github.com/search/repositories?q=language:python&sort=stars'):
    r = requests.get(url)
    return r

def get_repo_dicts(r):
    # Store API response in a variable.
    response_dict = r.json()
    print("Total repositories:", response_dict['total_count'])

    # Explore information about the repositories.
    repo_dicts = response_dict['items']
    return repo_dicts

# Make an API call and store the response.
r = get_repo_list()
print(r.status_code)

repo_dicts = get_repo_dicts(r)
print("Repositories returned:", len(repo_dicts))


names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # Get the project description, if one is available.
    description = repo_dict['description']
    if not description:
        description = "No description provided."
    
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description, 
        'xlink': repo_dict['html_url']
        }
    plot_dicts.append(plot_dict)

# Make visualization.
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')