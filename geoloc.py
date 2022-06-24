import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

class GeoLoc():
    '''
    Takes a pandas dataframe with at least two columns:
    - location
    - indicator
    Returns a geopandas geodataframe with four columns:
    - location
    - mean(indicator)
    - country
    - geometry
    Use the .plot() method to plot the world map
    '''
    def __init__(self, df_data):
        self.df_data = df_data[["location", "indicator"]]\
            .groupby("location", as_index=False)\
                .mean()\
                    .reset_index()
        self.df_world = gpd.read_file(gpd.datasets\
            .get_path('naturalearth_lowres'))[["name", "geometry"]]\
                .rename(columns={"name" : "country"})
        self.df_world = self.df_world[self.df_world["country"] != "Antarctica"]

    def locate(self):
        # geocoding (API call)
        df_geocode = gpd.tools.geocode(
            self.df_data["location"],
            provider="nominatim",
            user_agent="wagon"
            )[["geometry"]].reset_index()
        # merge with self.df_data
        df_data_code = df_geocode.merge(
            self.df_data,
            how="inner",
            on="index"
            ).drop(columns="index")
        # merge data with world map
        return self.df_world.sjoin(
            df_data_code,
            how="left",
            predicate="intersects"
            ).drop(columns="index_right")

    def plot(self):
        df = self.locate()
        # plot the world map
        ax = df.plot("indicator",
                    legend=True,
                    missing_kwds={"color" : "lightgrey"},
                    figsize=(14, 14),
                    cmap="autumn",
                    scheme="quantiles")
        ax.set_axis_off()
        df_clean = df[~df["location"].isnull()]
        return df_clean, ax


if __name__ == '__main__':
    df = pd.DataFrame({
        "location" : ["Nantes", "Singapore", "Santiago", "New York", "Tokyo", "London", "Barcelona", "Nantes"],
        "indicator" : [7.0, 6.5, 5.5, 5.0, 4.7, 2.3, 1.0, 8.0]
    })
    geo_locator = GeoLoc(df)
    print(geo_locator.locate()) # if not for debug, you can directly call geo_locator.plot()
