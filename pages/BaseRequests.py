import requests
from jsonpath import jsonpath


class BaseRequests:

    __host = 'http://test.wxapi.galaxy-immi.com'



    def get_headers(self,token,headers=None):
        if headers == None:
            headers ={"Content-Type":"application/x-www-form-urlencoded"}
        else:
            headers = headers
        headers.update({"token":token})
        return headers


    def runs(self, method, url, headers, json=None, data=None, params=None, **kwargs):

        self.response = requests.request(method=method,
                                         url=self.__host + url,
                                         headers=headers,
                                         json=json,
                                         data=data,
                                         params=params)
        return self.response



    def extract(self, field, key):

        r =jsonpath(field,key)
        return r


    def validate(self, re_value, ex_value):
        assert re_value == ex_value
        return self


    def contentIn(self,re_value,ex_value):
        assert ex_value in re_value
        return self