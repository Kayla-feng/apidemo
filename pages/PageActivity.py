from pages.BaseRequests import BaseRequests


class PageActivity(BaseRequests):


    def search(self,params,token,**kwargs):
        headers = self.get_headers(token)
        r = self.runs(method="get",
                      url="/backend/activity/search",
                      params=params,
                      headers=headers)
        return r


    def upload(self,token):
        url = "/backend/activity-file"

        headers={
                "Content-Type":"multipart/form-data; boundary=----WebKitFormBoundaryDFe5WkGiCGJXA8FZ",
                 "token":token
        }


        # with open(r"D:/CrmApiProject/timg.jpg", "rb")as f_abs:
        #     body = {'Size':"21.90 KB (22,422 bytes)",
        #             'Content-Type': "image/jpeg",
        #             "Client Path":f_abs}

        # file_data={'file':("timg.jpg",open(r"D:/CrmApiProject/timg.jpg",'rb'),'image/jpeg')}

        file_data = {'file': open(r"D:/CrmApiProject/timg.jpg", 'rb')}

        r = self.runs("post",
                      url,
                      headers=headers,
                      files=file_data
                      )
        return r







