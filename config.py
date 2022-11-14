from os import environ

github_token = environ.get('GITHUB_TOKEN')
assert github_token is not None
