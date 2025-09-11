import requests

geturl = "https://jsonplaceholder.typicode.com/posts/1"

def main():
    resp =  requests.get(geturl).json()

    print(resp)


    print(f"The title of the post is --> {resp['title']}")




if __name__=="__main__":
    main()



