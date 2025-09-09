import urllib.request
import json

MAJORTON = "http://api.open-notify.org/astros.json"

def main():
    groundctrl = urllib.request.urlopen(MAJORTON)

    helmet =groundctrl.read()
    print(helmet)
    helmetson = json.loads(helmet.decode("utf-8"))


    print(type(helmet))
    print(type(helmetson))
    print(helmetson["number"])
    #person 2
    print(helmetson["people"][1])

    for astro in helmetson["people"]:
        print(astro)
    
    for astro in helmetson["people"]:
        print(astro["name"])

if __name__=="__main__":
    main()