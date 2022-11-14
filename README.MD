# Test FlaskAPI

Simple flask api to interact with github api

## Features

Using this API:
- you can get a list of the user's public repositories on github
- you can create an issues to public repositories

## Installation

Dillinger requires [Flask](https://flask.palletsprojects.com/en/2.2.x/) to run.


```sh
git clone 
pip install -r requirments.txt
export GITHUB_TOKEN=<your github token>
```

## Executing program

```sh
flask run 
```

## Sample requests

GET list repositories for github user

```sh
curl -X GET http://"127.0.0.1:5000/<GIT_USERNAME>/repos"
```
Sample output

```sh
{
  "repos": [
    "be-dev-englishbot",
    "be-dev-flask-githubapi",
    "bot-template",
    "Bugs-Hunt-OdynokovTeam",
    "clean-code-javascript",
    "cv-mate-academy",
    "Filippenko_CSharp",
    "git-guide",
    "how-web-works",
    "JavaScript30",
    "reloadium"
  ]
}
```

POST issue to repo


```sh
curl -X POST http://127.0.0.1:5000/<GIT_USERNAME>/<GIT_REPONAME>/issue -H 'Content-Type:application/json' -d '{"title":"issue title","body":"test issue text"}'
```

Sample body for POST request from GitHub Docs


```sh
-d '{
    "title":"Found a bug",
    "body":"I'm having a problem with this.",
    "assignees":["octocat"],
    "milestone":1,
    "labels":["bug"]
    }'
```

Sample output

```sh
"issue_created": true
```

