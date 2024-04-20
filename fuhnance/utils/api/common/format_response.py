import json

def format_response(response):
    res = json.loads(response.text)
    if response.status_code != 200:
        raise ConnectionError(f'Trouble accessing API. See here:\n{response.status_code}\n{response.text}')
    return res

def format_kraken_response(res):
    res = format_response(res)
    return res['result']
