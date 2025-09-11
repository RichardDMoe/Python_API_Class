import requests
import pprint

AOIF = "https://www.anapioficeandfire.com/api/books"
AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():

    #pick numb for char
    got_char=input("pick num from 1-1000 to return info on")
    gotresp = requests.get(AOIF)
    gotresp1 = requests.get(AOIF_CHAR +got_char)


    got_dj = gotresp.json()
    got_dj1= gotresp1.json()
#    print(got_dj)

    pprint.pprint(got_dj1)
""""
    for singlebook in got_dj:

        print(f"{singlebook['name']},pages - {singlebook['numberOfPages']}")
        print(f"\tAPI URL -> {singlebook['url']}\n")
        print(f"\tPUBLISHER -> {singlebook['publisher']}\n")
        print(f"\tNo. of characters ->{len(singlebook['characters'])}\n")
"""


if __name__=="__main__":
    main()

