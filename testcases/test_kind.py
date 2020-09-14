import pytest

from common.GetYaml import GetYaml
from common.log import Log
from config import setting
from pages.PageKind import PageKind


testData = GetYaml().get_yaml(setting.Test_Data+'/'+'kind.yml')
gift_data = testData["change_state"]["create"]
search_data = testData["change_state"]["search"]


log = Log()

class TestKind:

    kind = PageKind()

    data = testData["create_kind"]

    @pytest.fixture(params=data)
    def param(self,request):
        return request.param


    def test_create_kind(self,token,param):

        data = {
            "classify_name":param["classify_name"],
            "classify_describe":param["classify_describe"],
        }

        r = self.kind.create(token,data=data).json()

        self.kind.validate(self.kind.extract(r,"$.code")[0],200)
        self.kind.validate(self.kind.extract(r,"$.msg")[0],param["msg"])



    @pytest.mark.parametrize("page,page_size",[(1,10),
                                               (1,5)])
    def test_get_list(self, token, page, page_size):
        params = {
            "page":page,
            "page_size":page_size
        }

        r = self.kind.search(token,params=params).json()
        self.kind.validate(self.kind.extract(r,"$.data[0].classify_name")[0],"测试")


    def test_create(self,token):


        #todo:完成创建-查询-开启状态，上下文响应

        self.kind.create(token,data=gift_data)

        r = self.kind.search(token,params=search_data).json()

        return r


    def test_change_state(self, token):

        r = self.test_create(token)
        # 获取刚创建的类别的状态
        state = str(self.kind.extract(
                r,"$.data[?(@.classify_name=='%s').state]" % (gift_data["classify_name"]))[0])
        
        # 获取刚创建的类别的id
        key = str(self.kind.extract(r,"$.data[?(@.classify_name=='%s').id]" % (gift_data["classify_name"]))[0])
        
        r = self.kind.change_state(token,value=state,key=key)
        self.kind.contentIn(self.kind.extract(r.json(),"$.msg")[0],"成功")
