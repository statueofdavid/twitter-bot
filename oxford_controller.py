import json
import requests
import toml

config = toml.load("config.toml")

base_url = config['oxford']['base_url']
application_id = config['oxford']['application_id']
application_key = config['oxford']['application_keys']

language_code = config['oxford']['language_code']

# responds with the root of the word in the signature
def get_lemma_payload(word):
    end_point = config['oxford']['lemma_end_point']
    url = base_url + "/" + end_point + "/" + language_code + "/" + word
    header = {"application_id":application_id,"application_key":application_key}

    return url, header

def get_word_data_payload(word):
    end_point = config['oxford']['word_end_point']
    url = base_url + "/" + end_point + "/" + language_code + "/" + word
    header = {"application_id":application_id,"application_key":application_key}

    return url, header

def try_request_handler(payload):
    url = payload[0]
    header = payload[1]
    # some error handling with try-catch
    try:
        r = requests.get(url, header)
    except requests.exceptions.ConnectionError as errconn:
        return "well something at the network level is jacked"
    except requests.exceptions.HTTPError as errhttp:
        return "well http is jacked"
    except requests.exceptions.Timeout as errto:
    # Maybe set up for a retry, or continue in a retry loop
        return "well try again later"
    except requests.exceptions.TooManyRedirects as errtmr:
    # Tell the user their URL was bad and try a different one
        return "well that url is whack"
    except requests.exceptions.RequestException as errunkn:
    # catastrophic error. bail.
        return "shrug"
        raise SystemExit(e)
    return r
