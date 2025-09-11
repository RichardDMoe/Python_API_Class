import requests

posturl = "https://jsonplaceholder.typicode.com/posts"


def main():
    mydata = {
            "title": "foe",
            "body": "bar",
            "userId": 1
            }

    resp = requests.post(posturl,json=mydata).json()

    print(resp.keys())
    print(f"Newly created post id: {resp['id']}")

if __name__=="__main__":
    main()

