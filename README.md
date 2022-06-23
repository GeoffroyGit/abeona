# What is this all about?

From a table containing location names (countries, cities, addresses, etc) and an indicator (a numerical value) for each location, this code creates a world map with each country colored according to the indicator.

# Special thanks to GeoPandas

This code uses [GeoPandas](https://geopandas.org) 🤩

# Run my code yourself

## Install

Clone the project:

```bash
git clone git@github.com:GeoffroyGit/abeona.git
```

I recommend you to create a fresh virtual environment

Create a python3 virtualenv and activate it:

```bash
cd abeona
pyenv virtualenv abeona
pyenv local abeona
```

Upgrade pip if needed:

```bash
pip install --upgrade pip
```

Install the dependancies:

```bash
pip install -r requirements.txt
```

## Run in a notebook

Create a Jupyter notebook

```bash
jupyter notebook
```

Inside your notebook, run the following python code

Import GeoLoc

```python
from geoloc import GeoLoc
```

Open your pandas dataframe

```python
df = pd.read_csv("/path/to/your/file.csv")
```

or create a dummy dataframe

```python
df = pd.DataFrame({
        "location" : ["Nantes", "Singapore", "Santiago", "New York", "Tokyo", "London", "Barcelona", "Nantes"],
        "indicator" : [7.0, 6.5, 5.5, 5.0, 4.7, 2.3, 1.0, 8.0]
    })
```

Create an instance of the class GeoLoc

```python
geo_locator = GeoLoc(df)
```

Finally, plot the world map

```python
geo_locator.plot();
```
