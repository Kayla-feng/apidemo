from pages.BaseRequests import BaseRequests


class PageKind(BaseRequests):

    def create(self,token,data,**kwargs):
        url = "/backend/integral-classify"
        headers = self.get_headers(token)
        method = 'post'
        r = self.runs(method=method,url=url,data=data,headers=headers)
        return r


    def change_state(self, token, value,key):
        url = '/backend/integral-classify/state/'+key
        method = 'PUT'
        headers = self.get_headers(token)
        if value == "0":
            data =  {"state":1}
        else:
            data = {"state":0}
        r = self.runs(method=method,url=url,headers=headers,data=data)
        return r



    def search(self,token,params):
        url = '/backend/integral-classify/search'
        method = 'get'
        params=params
        headers = self.get_headers(token)
        r = self.runs(method=method,url=url,params=params,headers=headers)
        return r


    def move(self,token):
        url = '/backend/integral-classify/moveClassify'
        method= 'get'
        headers = self.get_headers(token)
        r = self.runs(method,url,headers=headers)
        return r