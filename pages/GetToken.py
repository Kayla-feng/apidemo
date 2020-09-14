from pages.BaseRequests import BaseRequests


class GetToken:

    base = BaseRequests()

    @classmethod
    def token(self,**kwargs):
        url = "/backend/login"
        method = "POST"
        dict = {"username":"test",
                "password":"123456"}

        r = self.base.runs(method=method, url=url, data=dict,headers = None)
        return r.json()["data"]["token"]

