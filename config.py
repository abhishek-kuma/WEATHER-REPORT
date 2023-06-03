#write a code that can write a text file in api folder and write the data in it for api key
#This file will be used to store the API key

# Solution:
import requests
import json
import sys
import os
import time
import datetime

# Take the input of API key
api_key=input("Enter the API key: ")

# Write the API key in a file
with open("api/api_key.txt", "w") as f:
    f.write(api_key)
    