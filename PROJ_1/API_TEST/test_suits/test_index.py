
import pytest
from PROJ_1.API_TEST.utils.case_handler import *


class TestIndex(object):
    
    def test_mch_web_v1_login(self,login_session):
        api = "/mch_web/v1/login"
        playload = {'uname': 'fht20210621', 'passwd': 'fht20210621'}
        method = "POST"
        resp = req(api=api, session=login_session, data=playload,method=method)
        validate(resp,[['resp.status_code==200', '接口响应状态码不等于200']])

    def test_mch_web_v1_user(self,login_session):
        api = "/mch_web/v1/user"
        playload = {}
        method = "POST"
        resp = req(api=api, session=login_session, data=playload,method=method)
        validate(resp,[['resp.status_code==200', '接口响应状态码不等于200']])

    def test_mch_web_v1_mch_detail(self,login_session):
        api = "/mch_web/v1/mch_detail"
        playload = {}
        method = "POST"
        resp = req(api=api, session=login_session, data=playload,method=method)
        validate(resp,[['resp.status_code==200', '接口响应状态码不等于200']])

    def test_mch_web_v1_report_list_user_download(self,login_session):
        api = "/mch_web/v1/report/list_user_download"
        playload = {}
        method = "POST"
        resp = req(api=api, session=login_session, data=playload,method=method)
        validate(resp,[['resp.status_code==200', '接口响应状态码不等于200']])


if __name__ == '__main__':
    pytest.main(['-s'])
