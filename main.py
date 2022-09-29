from flask import Flask
import requests


app = Flask(__name__)

github_token = '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'


@app.route("/<string:name>/repos")
def get_list_of_repo(name):
    res = requests.get(f'https://api.github.com/users/{name}/repos')
    list_of_repos = []
    data = {}
    for i in res.json():
        list_of_repos.append(i['name'])
    data['repos'] = list_of_repos
    return data


@app.route("/<string:name>/<string:repo>/issues")
def set_issue(name, repo):
    headers = {'Accept': 'application/vnd.github+json',
               'Authorization': f'Bearer {github_token}'}

    data = {"title": "issue title",
            "body": "test issue text"}

    res = requests.post(f'https://api.github.com/repos/{name}/{repo}/issues',
                        headers=headers,
                        json=data)

    result_code = res.status_code

    if result_code == 201:
        return {"issue_created": True}
    else:
        return {"issue_created": False}

