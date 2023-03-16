import pandas as pd
import numpy as np
import xgboost as xgb
import time
import urllib
import concurrent.futures
import requests
import geopy.distance

def get_coordinates(address_name):
    """Searches for address's geocoordinates (lat, long) on OneMap's Search API

    Parameters:
    addresses (list(string)): list of addresses to search 

    Returns:
    input (list(string)): list of input addresses by order of request completion
    latitudes (list(string)): list of latitudes by order of address in input
    longitudes (list(string)): list of longitudes by order of address in input
    not_found (list(string)): list of addresses with no results in OneMap Search API

    """

    input = []
    latitudes = []
    longitudes = []
    not_found = []
    CONNECTIONS = 100
    TIMEOUT = 5

    time1 = time.time()
    queries = [urllib.parse.quote(address_name).replace(".","")] 
    print(queries)#special char replacement for url
    print(f"len = {len(queries)}")

    url1 = "https://developers.onemap.sg/commonapi/search?searchVal="
    url2 = "&returnGeom=Y&getAddrDetails=N&pageNum=1"
    urls = [ url1+query+url2 for query in queries]
    print(urls)

    address_url_map = dict(zip(urls, address_name)) 

    def load_url(url,timeout):
        r = requests.get(url)
        return r.json()
    

    with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
        future_to_url = dict((executor.submit(load_url, url, TIMEOUT), address_url_map[url]) for url in urls)
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
            except Exception as exc:
                data = str(type(exc))
            finally:
                print(data)
                if(data['found']==0): #store address of notfounds in separate list
                    not_found.append(future_to_url[future])
                    print(future_to_url[future])
                    print(data)
                else: #only append those found in input,latitudes, longitudes lists
                    # input.append(future_to_url[future])
                    input.append(data['results'][0]['SEARCHVAL'])
                    latitudes.append(data['results'][0]['LATITUDE'])
                    longitudes.append(data['results'][0]['LONGITUDE'])
    time2 = time.time()
    print(f"Search took {time2-time1:.2f} s")
    print(f'Fetch completed for {len(urls)} urls, {len(input)} urls were located, {len(not_found)} urls could not be found.')
    return input, latitudes, longitudes, not_found

def calculate_distance(df_geo,mrt_data):
  time_1 = time.time()
  min_distance = []
  for i in range(len(df_geo)):
    coords_1 = [df_geo.iloc[i]['latitude'],df_geo.iloc[i]['longitude']]
    mrt_distance = []
    for j in range(len(mrt_data)):
      coords_2 = [mrt_data.iloc[j]['latitude'],mrt_data.iloc[j]['longitude']]
      mrt_distance.append(geopy.distance.geodesic(coords_1, coords_2).km)
    min_distance.append(min(mrt_distance))
  time_2 = time.time()
  print(f"calculating distance took {time_2-time_1:.2f} s")
  return min_distance  

def get_shortest_distance(address_name):
    input, latitude, longitude, not_found = get_coordinates(address_name)
    df_geo = pd.DataFrame()
    df_geo['address'] = pd.Series(input)
    df_geo['latitude'] = pd.Series(latitude)
    df_geo['longitude'] = pd.Series(longitude)

    #load primary pickle
    input, latitude, longitude, not_found = pd.read_pickle('dataPackage/primary_hdb.pickle')
    df_geo_primary = pd.DataFrame()
    df_geo_primary['address'] = pd.Series(input)
    df_geo_primary['latitude'] = pd.Series(latitude)
    df_geo_primary['longitude'] = pd.Series(longitude)

    #load mrt_lrt_data
    #data taken from https://github.com/xkjyeah/MRT-and-LRT-Stations/blob/master/mrt_lrt.csv
    df_geo_mrt = pd.read_csv("dataPackage/final_mrt_list.csv")

    #load cbd_data
    df_geo_cbd = df_geo_mrt[df_geo_mrt.station_name == "RAFFLES PLACE MRT STATION"]

    # get shortest distance for all
    shortest_cbd_area = calculate_distance(df_geo,df_geo_cbd)
    shortest_primary_distance = calculate_distance(df_geo, df_geo_primary)
    shortest_mrt_distance = calculate_distance(df_geo,df_geo_mrt)
    return shortest_cbd_area, shortest_primary_distance, shortest_mrt_distance
    

def transform(items,shortest_cbd_distance, shortest_primary_distance, shortest_mrt_distance):
    df = pd.DataFrame(items, index=[0])
    dummies_frame = pd.read_csv("dataPackage/final_columns.csv")
    df["shortest_mrt_distance"] = shortest_mrt_distance
    df["shortest_primary_distance"] = shortest_primary_distance
    df["shortest_cbd_distance"] = shortest_cbd_distance
    # print(df.reindex(columns = dummies_frame.columns, fill_value=0))
    new_item = pd.get_dummies(df).reindex(columns=dummies_frame.columns,fill_value=0)
    xgb_model = xgb.Booster()
    xgb_model.load_model("dataPackage/hdb_model.bst")
    xginput = xgb.DMatrix(new_item.values)
    print(xgb_model.predict(xginput))
    price_pred = xgb_model.predict(xginput)
    return price_pred