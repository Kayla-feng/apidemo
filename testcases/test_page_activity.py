
from pages.PageActivity import PageActivity


class TestPageActivity(PageActivity):


    def test_search(self,token):
        params={"page":1,
                "page_size":10}
        r = self.search(params, token).json()
        self.validate(self.extract(r,"$.data.items[0].title")[0],"测试")



