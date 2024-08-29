# from helper import test_fnc
# import logging
#
# logger = logging.getLogger('MAIN')
# logger.error('Error happened in the app')
#
#
# user_input_list = input("input something comma separated values: ")
# for item in user_input_list.split(','):
#     test_fnc(item)

import requests

response = requests.get('https://gitlab.com/api/v4/users/adwiza1/projects')

my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']} Project URL: {project['web_url']}")
