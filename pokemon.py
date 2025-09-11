import requests
import argparse
import pandas


#itemurl = "http://pokeapi.co/api/v2/pokemon/"
itemurl = "http://pokeapi.co/api/v2/item"

def main():
   # pokemon = requests.get(itemurl)
    pokeman = request.get(f"{itemurl}?limit=1000")
    
    pokemon =pokemon.json()
    
    matchedworks =[]

    #print(pokemon.keys())
    #print(pokemon['count'])
"""
    for poke in pokemon["results"]:

        print(poke.get("name"))

    print(f"Total # of Pokemon returned: {len(pokemon['results'])}")
"""
for item in items.get("results"):
        if args.searchwords in item.get("name"):
            matchedwords.append(item.get("name"))
    
finishedlist = matchedwords.copy()

matchedwords = {}
matchedwords["matched"] = finishedlist

print(f"there are {len(finishedlist)} words that contain the work '{args.searchwords}' in the pokemon item api")
print(f"List of Pokeman items containing '{args.searchwords}':")

print(matchedwords)





if __name__=="__main__":
    main()
    