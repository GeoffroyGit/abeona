import pandas as pd
import requests as rq

class GeoLoc():
    '''
    Give it a list of locations (countries, cities, etc)
    and it will return a panda dataframe with your locations
    together with their longitude and latitude coordinates.
    '''
    def __init__(self):
        self.url = "https://nominatim.openstreetmap.org"

    def locate(self, locations):
        df = pd.DataFrame({"loc" : locations})
        # try to minimize the API calls in case locations are repeated
        unique_locations = list(df["loc"].unique())
        locations_found = []
        longitudes = []
        latitudes = []
        for location in unique_locations:
            # geoloc API call
            params = {"q": location, 'format': 'json'}
            response = rq.get(self.url, params=params)
            if response.status_code == 200:
                if len(response.json()) > 0:
                    response = response.json()[0]
                    longitudes.append(float(response.get("lon", 0.0)))
                    latitudes.append(float(response.get("lat", 0.0)))
                    locations_found.append(location)
        # store longitudes and latitudes in a dataframe
        df_lon_lat = pd.DataFrame({
            "loc" : locations_found,
            "lon" : longitudes,
            "lat" : latitudes
        })
        return df.merge(df_lon_lat, how="left", on="loc")


if __name__ == '__main__':
    countries = ["France", "Singapore", "Santiago"]
    geo_locator = GeoLoc()
    print(geo_locator.locate(countries))
