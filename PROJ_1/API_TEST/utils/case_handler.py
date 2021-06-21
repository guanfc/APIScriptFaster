import json

from PROJ_1.API_TEST.settings import BASIC_URI
from PROJ_1.API_TEST.settings import logger


def req(api, session, data={}, method="GET"):
    """http requests"""
    if str(method).upper() == "GET":
        resp = session.get(BASIC_URI + api, data=data)
    else:
        resp = session.post(BASIC_URI + api, data=data)
    assert resp.status_code == 200
    logger.info("{} {} \n{}\n", method, api, json.dumps(resp.json(), indent=4, ensure_ascii=False))
    if resp.json().get("data"):
        assert len(resp.json().get("data")) > 0, "获取data失敗"
    return resp


def validate(resp, assert_list):
    """ http validate"""
    for item in assert_list:
        assert eval(item[0]), item[1]
