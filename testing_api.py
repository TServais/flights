import numpy as np 
import pandas as pd 
import urllib
import requests
from pprint import pprint

date = '2019-02-01'
departure_airport = 'ORD'
final_airport = 'JFK'

query_string = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/US/USD/en-US/"+departure_airport+"-sky/"+final_airport+"-sky/"+date+"?inboundpartialdate=2019-02-01"

r = requests.get(query_string,
  headers={
    "X-RapidAPI-Key": "863928ac98msh92375cb362edbadp19fffbjsn3f22e03123fa"
  }
)

pprint(r.json())