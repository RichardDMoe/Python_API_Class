import requests
import pprint

MAJORTON = 'http://api.open-notify.org/astros.json'

def main():
    grounctrl = requests.get(MAJORTON)
    helmetson = grounctrl.json()

    print("\n\nConverted Pyton Data")
    print (helmetson)

    print('\n\nPeople in space: ', helmetson['number'])
    people = helmetson['people']
    pprint(helmetson['name'])

if __name__=="__main__":
    main()
