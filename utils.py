import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.geocoders import Nominatim
import streamlit as st

# calling the Nominatim tool and create Nominatim class
loc = Nominatim(user_agent="Geopy Library")



def save_uploaded_file(uploaded_file, destination_path):
    with open(destination_path, "wb") as f:
        f.write(uploaded_file.read())
    return destination_path

def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    st.write(f"IP Address: {res.ip_address}")
    #st.write(f"Location: {res.city}, {res.region}, {res.country}")
    #st.write(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")
    
    # entering the location name
    getLoc = loc.geocode({res.city})

    # printing address
    #st.write(getLoc.address)

    # printing latitude and longitude
    #st.write("Latitude = ", getLoc.latitude, "\n")
    #st.write("Longitude = ", getLoc.longitude)
    
    return res, getLoc
    