import json
import logging
import pytest
import requests


class TestCreateClient:

    def test_get_user(self,cookie):
        logging.debug(cookie)
        r = requests.post("http://test.galaxy-immi.com/user/users-details-ajax",
                          data={"id":474},
                          cookies=cookie,
                          headers={
                              "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
                          )
        logging.debug(r.json())

    def test_get_provice(self,cookie):
        logging.debug(cookie)
        r = requests.get("http://test.galaxy-immi.com/client/check-phone",
                         params={"phone":"18566672715"},
                         headers={
                             "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"},
                         cookies=cookie
                         )

        logging.debug(r.json())
        assert r.status_code == 200
        # assert jsonpath.jsonpath(r.json(),"$.data.city") == "深圳"

    @pytest.mark.skip
    def test_create_client(self):
        r = requests.post("http://test.galaxy-immi.com/client/client-add-ajax",
                          data={"username":"测试",
                                  "mobile":"13855511111",
                                  "sex":"女",
                                  "location":"安徽-马鞍山",
                                  "background":"1",
                                  "customers":"非介绍客户",
                                  "recommend_name":"",
                                  "projectid":"1",
                                  "score":"25",
                                  "source":"400",
                                  "intention":"未联系",
                                  "wechat_invited":"0",
                                  "project":"香港优秀人才入境计划",
                                  "group_type":"0",
                                  "type":"client",
                                  "platform":"银河PC官网",
                                  "channel":"sem"},
                          headers={
                                   "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
                          ).json()
        logging.debug(json.dumps(r,indent=2,ensure_ascii=False))
        assert r["msg"] == "新增成功"
