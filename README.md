# What is this all about?

So far this code simply fetches longitude and latitude from OpenStreeMap API.

It can be used to easily place data on map when we just have a list of names.

For example if I only have a list of country names, I can now easily display them according to their location on the planet.

# Further development

The more general idea is to also generate the map itself.

From a list of country names, I'd like to create a world map highlighting these countries.

Furthermore, from a pandas dataframe containing country names and a value for each country, let's say population size, I'd like to return a world map with each country colored according to the population size.

I'd like this to work for any name (country name, city name, etc) and any value.

It seems that I could make use of GeoPandas 🤩
