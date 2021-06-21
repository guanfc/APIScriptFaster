"""
func:根据case_list用例列表，生成pytest用例脚本文件test_xx.py
"""
from pathlib import Path

import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

code_import = """
import pytest
from PROJ_1.API_TEST.utils.case_handler import *

"""

code_run = """

if __name__ == '__main__':
    pytest.main(['-s'])
"""


def generate_py_case(py_test_file, case_list):
    """
    根据用例配置列表，生成pytest用例文件
    :param py_test_file:
    :param case_list:
    :return:
    """
    print("生成pytest用例文件")
    file_prex = os.path.splitext(py_test_file)[-1]  # 后缀
    suit_name = Path(py_test_file).name.rstrip(file_prex)
    # 生成的pytest文件模板，重点！根据项目需要自行修改，特别是fixtures内容
    pytest_template = """
class {suit_name}(object):
    """.format(suit_name=suit_name.title().replace("_",""))
    for case in case_list:
        pytest_template = pytest_template + """
    def test_{name}(self,login_session):
        api = "{api}"
        playload = {playload}
        method = "{method}"
        resp = req(api=api, session=login_session, data=playload,method=method)
        validate(resp,{assert_list})
""".format(name=case.get("name"), api=case.get("api"), playload=case.get("playload"), method=case.get("method"),
           assert_list=case.get("assert_list"))

    pytest_template = code_import + pytest_template + code_run
    try:
        with open(py_test_file, "w", encoding="UTF-8") as fp:
            fp.write(pytest_template)
    except Exception as e:
        print("写入pytest用例文件失败:{}".format(py_test_file))
        print(str(e))
        exit()
    print("生成pytest用例文件-success :{}".format(py_test_file))
    return pytest_template


if __name__ == '__main__':
    case_list = []

    ########## 将指定的case_list生成pytest用例文件 ####################
    # from case_datas.index import case_list as index
    # case_list.extend(index)

    from PROJ_1.API_TEST.case_datas.case_py.index import case_list as index

    case_list.extend(index)
    py_test_file = "../test_suits/test_index.py"  # 定义pytest用例文件名称，如test_xxx.py
    generate_py_case(py_test_file, case_list)
