# Idealista client

## Client
The client needs to specify the **apiKey** and **secret** in the *config.toml* file located in *client/config*

## Digest pipeline
The `Pipeline` object represents a set of parameters for running a search query and managing the results. It consists of the following fields by default it reads the */digest/pipelines.yaml*:
### 1. **Pipeline**

- **`name`** (`str`):  
  The name of the pipeline.

- **`query`** (`SearchQuery`):  
  Contains the details of the search query. This field is optional.

- **`geo_query`** (`GeoQuery`):  
  Defines geographic constraints on the search. This field is optional.

- **`filters`** (`dict`):  
  A dictionary of additional filters to apply to the search query. Optional.

- **`store`** (`Store`):  
  Defines where the search results will be stored. This field is optional.

- **`limit`** (`int`):  
  Maximum number of items to fetch. Optional.

- **`run`** (`Command`):  
  A command that triggers the execution of the pipeline. Optional.

---

### 2. **SearchQuery**

The `SearchQuery` object defines the parameters for performing a search. Its fields are:

- **`country`** (`Country`):  
  The country where the search is performed. Must be one of the following: `es`, `it`, `pt`.

- **`operation`** (`Operation`):  
  The type of operation being performed: `sale` or `rent`.

- **`propertyType`** (`PropertyType`):  
  The type of property being searched: `homes`, `offices`, `premises`, `garages`, `bedrooms`.

- **`locale`** (`Locale`):  
  The locale for the search results, corresponding to the language code: `es`, `it`, `pt`, or `en`.

- **`maxItems`** (`int`, default = 50):  
  Maximum number of items to return per page of results.

- **`numPage`** (`int`, default = 1):  
  The page number to return in the results.

- **`order`** (`str):  
  Specifies the ordering of the results. Optional.

- **`sort`** (`str`):  
  Specifies the field by which to sort the results. Optional.

- **`hasMultimedia`** (`bool`):  
  Filters properties based on whether they have multimedia (images, videos, etc.). Optional.

---

### 3. **GeoQuery**

The `GeoQuery` object specifies geographic constraints for a search. It consists of the following fields:

- **`center`** (`GeoCoordinates`):  
  The geographical center for the search, defined by latitude and longitude.

- **`distance`** (`float`):  
  The search radius from the center in kilometers.

---

### 4. **GeoCoordinates**

The `GeoCoordinates` object defines geographical coordinates:

- **`latitude`** (`str`):  
  The latitude of the location.

- **`longitude`** (`str`):  
  The longitude of the location.

---

## Google drive interaction
You could use the function `store_drive` to persist the results as a file in drive (p.e for mysql or a plain text), for this you would need to place your api token in */digest/config/credentials.json*. The credentials is the generated json when you renew credentials for a given application.


## Docker image
The docker image uses a very simple approach, it creates an infinite loop that checks if the last_run file was generated and the periodicity has not expired. The periodicity for this could be changed in */anacron/config.toml*.

## Tableau book

This project (`data.twb`) uses **Tableau Desktop Professional Edition 2019.4.3**. To ensure compatibility when working with this file, you will need to use the same version of Tableau.

### Download Link for Tableau Desktop 2019.4.3

To download Tableau Desktop Professional Edition 2019.4.3, you can use the following [magnet link](https://tinyurl.com/2en3knzn): 

### You may run it on local

Doing the following you may run it on local

```
docker volume create idealista

docker build -t idealista-bot:latest .
docker run --restart unless-stopped  -v idealista:/idealista/output -d idealista-bot:latest
```