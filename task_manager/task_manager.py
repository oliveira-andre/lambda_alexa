import requests

auth_header = { 'token': 'set_your_token' }
rep = requests.get(
        'http://localhost:3334/api/v1/projects',
        headers=auth_header
        )

projects = rep.json()
projects_count = len(projects)

for project in projects:
    print project['title']
