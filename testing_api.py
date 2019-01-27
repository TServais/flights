import numpy as np 
import pandas as pd 
import unirest

response = unirest.get("https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/USD/en-US/SFO-sky/JFK-sky/2019-01-01?inboundpartialdate=2019-01-01",
  headers={
    "X-RapidAPI-Key": "863928ac98msh92375cb362edbadp19fffbjsn3f22e03123fa"
  }
)