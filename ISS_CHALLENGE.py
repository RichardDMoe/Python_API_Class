import requests
from datetime import datetime 


url = "http://api.open-notify.org/iss-now.json"


def main():

    iss_loc = requests.get(url)

    iss_loc = iss_loc.json()

    timetaken = datetime.fromtimestamp(iss_loc['timestamp'])
    
    print(timetaken)
    print(iss_loc)
    print(f"""Current Location of the ISS:
            Time is currently: {timetaken}
            Lat: {iss_loc['iss_position']['latitude']} 
            Lon{iss_loc['iss_position']['longitude']}""")

if __name__=="__main__":
    main()
