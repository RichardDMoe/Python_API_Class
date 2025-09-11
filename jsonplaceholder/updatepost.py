import requests

puturl = "https://jsonplaceholder.typicode.com/posts/1"

def main():

    updated_data = {
            "id": 1,
            "title":"updated title",
            "body":"This is the update",
            "userId":1
            }

    resp = requests.put(puturl,json=updated_data).json()

    print(resp.keys())
    print(f"udated post: {resp['title']}")

if __name__=="__main__":
    main()
