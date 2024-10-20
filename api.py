import requests
import time


class API(object):
    '''Base class for Sportradar API wrappers. Handles the connection to the API and provides a method for making requests'''

    # Create a session to persist cookies and headers
    session = requests.Session()
    session.headers = {'application': 'PythonWrapper'}

    def __init__(self, api_key, format_='json', timeout=5, sleep_time=2):
        '''Initialize the API wrapper with the API key and format. 
        Optionally set the timeout and sleep time between requests. 
        The sleep time is used to avoid rate limiting.'''
        self.api_key = {'api_key': api_key}
        self.api_root = 'http://api.sportradar.us/'
        self.FORMAT = "." + format_.strip(".")
        self.timeout = timeout
        self._sleep_time = sleep_time

    def _make_request(self, path, method='GET'):
        '''Make a request to the API.'''
        time.sleep(self._sleep_time)
        url = self.api_root + path + self.FORMAT
        response = self.session.request(method,
                                        url,
                                        timeout=self.timeout,
                                        params=self.api_key)
        return response