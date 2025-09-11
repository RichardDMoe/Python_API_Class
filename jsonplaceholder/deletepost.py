import requests

deleteurl = "https://jsonplaceholder.typicode.com/posts/1"

def main():
    resp = requests.delete(deleteurl)

    if resp.status_code == 200 or resp.status_code == 204:
        print("post deleted")
    else:
        print(f" failed to delete post with status code : {resp.status_code}")

if __name__=="__main__":
    main()
