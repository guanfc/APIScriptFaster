import pytest
import requests

from PROJ_1.API_TEST.settings import BASIC_URI


@pytest.fixture(scope="session")
def login_session():
    """获取账号登录session """
    session = requests.Session()
    api = "/mch_web/v1/login"
    playload = {
        "uname": "fht20210621",
        "passwd": "fht20210621"
    }
    # 登录
    resp = session.post(BASIC_URI + api, playload, verify=False)
    print("登录结果:", resp.json())
    return session
