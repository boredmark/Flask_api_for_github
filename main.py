from flask import Flask, request
import requests
import config


app = Flask(__name__)

github_token = config.github_token


@app.route("/<string:name>/repos", methods=['GET'])
def get_list_of_repo(name):
    res = requests.get(f'https://api.github.com/users/{name}/repos')
    list_of_repos = []
    data = {}
    for i in res.json():
        list_of_repos.append(i['name'])
    data['repos'] = list_of_repos
    return data


@app.route("/<string:name>/<string:repo>/issues", methods=['POST'])
def set_issue(name, repo):
    headers = {'Accept': 'application/vnd.github+json',
               'Authorization': f'Bearer {github_token}'}

    data = request.json

    res = requests.post(f'https://api.github.com/repos/{name}/{repo}/issues',
                        headers=headers,
                        json=data)

    result_code = res.status_code

    if result_code == 201:
        return {"issue_created": True}
    else:
        return {"issue_created": False}

