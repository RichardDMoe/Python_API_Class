import json
import requests


my_username = "RichardDMoe"


def create_repo(repo_name: str, token: str) --> str:
    
    repo_data = {"name": repo_name}
    json_data = json.dumps(repo_data)

    headers = {"Authorization": f"token{token}"}

    r= requests.post(f"https://api.github.com/user/repos", data=json_data, headers=headers)

    response_code = r.status_code
    response = r.text
    print(response_code,response)

    return response

def show_respos(username:str,token:str):
    url = f"https://api.github.com/users/{username}/repos"

    headers= {"Authorization": f"token {token}"}
    r = requests.get(url, headers=headers)
    resp_headers = r.headers
    print(f"""Rate - \n            Limit: {resp_headers['X-RateLimit-Limit']}
            Used: {resp_headers['X-RateLimit-Used']}
            Remaining: {resp_headers['X-RateLimit-Remaining']}""")


    repos = list(r.json())

    for repo in repos:
        print(repo['name'])

    return repos

def get_token():
    with open("/home/student/token") as f:
        token = f.read().rstrip("\n")
        return token

if __name__=="__main__":
    tkn = get_token()
    show_repos(MY_USERNAME, tkn)
    create_repo("learning_oauth", tkn)
