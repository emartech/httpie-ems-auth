"""
EmsAuth auth plugin for HTTPie.

"""
from httpie.plugins import AuthPlugin
import escherauth
import datetime
from urlparse import urlparse

__version__ = '0.1.0'
__author__ = 'Andras Barthazi'
__licence__ = 'MIT'

class EmsAuth:
    def __init__(self, access_id, secret_key):
        options = {
            'algo_prefix': 'EMS',
            'vendor_key': 'EMS',
            'hash_algo': 'SHA256',
            'auth_header_name': 'X-Ems-Auth',
            'date_header_name': 'X-Ems-Date'
        }
        self.client = {'api_key': access_id, 'api_secret': secret_key}
        self.escher = escherauth.Escher("eu/suite/ems_request", options)

    def __call__(self, r):
        now = datetime.datetime.utcnow()
        r.headers['X-Ems-Date'] = now.strftime('%Y%m%dT%H%M%SZ')
        parsed_uri = urlparse(r.url)
        r.headers['Host'] = parsed_uri.netloc
        return self.escher.sign(r, self.client)

class EmsAuthPlugin(AuthPlugin):

    name = 'EmsAuth auth'
    auth_type = 'ems-auth'
    description = 'Sign Emarsys API requests using the Escher authentication method'

    def get_auth(self, access_id, secret_key):
        return EmsAuth(access_id, secret_key)
