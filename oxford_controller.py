import json
import requests
import toml

config = toml.load("config.toml")

base_url = config['oxford']['base_url']
application_id = config['oxford']['application_id']
application_key = config['oxford']['application_keys']

language_code = config['oxford']['language_code']

# responds with the root of the word in the signature
def get_lemma_response(word):
    end_point = config['oxford']['lemma_end_point']
    url = base_url + "/" + end_point + "/" + language_code + "/" + word
    header = {"application_id":application_id,"application_key":application_key}
    r = requests.get(url, headers)
    return r
