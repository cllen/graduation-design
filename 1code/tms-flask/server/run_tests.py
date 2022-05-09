import requests

proxies = { "http": None, "https": None}
resp2 = requests.post(
    "http://127.0.0.1:5001/oauth2/authorization/authorize",
    # data=json.dumps(payload),
    data={
        'response_type': 'code', 
        'client_id': '1', 
        'redirect_uri': 'http://localhost:5000/tms/code_callback', 
        'scope': 'snsapi_base', 
        'account': '20203712062', 
        'password': '123'},
    allow_redirects=False
    
)

print(resp2.headers['Location'])