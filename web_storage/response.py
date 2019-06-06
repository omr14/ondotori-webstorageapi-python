"""
Pyhton Client for ONDOTORI WebStorage API
TR-7wf/nw series
API reference
https://ondotori.webstorage.jp/docs/api/index.html
"""

class WebStorageAPIResponse:

    def __init__(self, response):
        self.headers = response.headers

        if 'application/json' in self.headers['Content-Type']:
            self.res_content = response.json()
        elif 'text/csv' in self.headers['Content-Type']:
            self.res_content = response.content

    @property
    def retelimit_limit(self):
        return self.headers['X-RateLimit-Limit']

    @property
    def ratelimit_reset(self):
        return self.headers['X-RateLimit-Reset']

    @property
    def retelimit_remaining(self):
        return self.headers['X-RateLimit-Remaining']

    @property
    def content(self):
        return self.res_content
