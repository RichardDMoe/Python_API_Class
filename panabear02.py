
import pandas as pd

def main():
    ciscocsv = pd.read_csv("ciscodata.csv")
    ciscojson = pd.read_json("ciscodata2.json")


    print(ciscocsv.head())
    print ("BREAK")
    print(ciscojson.head())
    

    ciscodf = pd.concat([ciscocsv,ciscojson])
    print("FINAL")
    print(ciscodf)

if __name__=="__main__":
    main()


