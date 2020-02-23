import requests


class HTTPConnection:
    def __init__(self, url: str, broker_code: int):
        self.url = url
        self.headers = {
            'device-type': '11',
            'broker-code': str(broker_code),
            'content-type': 'application/json'
        }
        self.session = requests.Session()

    def get(self, uri, params):
        get_url = self.url + uri
        return self.session.get(
            get_url,
            params=params,
            headers=self.headers,
        )

    def post(self, uri: str, data={}):
        post_url = self.url + uri
        print(post_url)
        print(data)
        return self.session.post(post_url, json=data, headers=self.headers)

    def put(self, uri: str, data={}):
        post_url = self.url + uri
        return self.session.put(post_url, data=data, headers=self.headers)

    def delete(self, uri: str):
        delete_url = self.url + uri
        return self.session.delete(delete_url)

    def set_token(self, authToken):
        self.headers['authToken'] = authToken


class RealtimeConnection:
    pass
