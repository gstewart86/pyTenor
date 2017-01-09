#!/usr/bin/python

import requests
import json
import Tenor

API_KEY = '<insert_your_api_key>'
ten = Tenor.Tenor()

print ten.random("Testing")
