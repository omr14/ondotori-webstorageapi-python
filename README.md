# ONDOTORI WebStorage API
Unofficial API wrapper for Ondotori WebStorageAPI

## How to Use

Get all device current data.
```
from web_storage.api_client import WebStorageAPIClient

auth = {
    "api-key": <api-key>,
    "login-id": <login-id>,
    "login-pass": <login-pass>
}

client = WebStorageAPIClient(auth)
res = client.get_current()
res.content
```

## Reference
おんどとり WebStorage API
https://ondotori.webstorage.jp/docs/api/index.html
