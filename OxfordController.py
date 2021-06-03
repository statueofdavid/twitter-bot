import json
import requests
import toml

config = toml.load("config.toml")

base_url = config['oxford']['base_url']
application_id = config['oxford']['application_id']
application_key = config['oxford']['application_keys']
