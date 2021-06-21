"""
func:根据xx.har文件，生成用例列表文件xx.py,case_list=[{},{}...]
"""

import json
import os
from pathlib import Path
from urllib import parse

from PROJ_1.API_TEST.settings import BASE_DIR


def load_har2_json(har_file):
    """
    将HAR文件内容解析成字典对象
    :param har_file:
    :return:
    """
    print("将har文件解析成字典")
    har_dict = {}
    try:
        with open(har_file, "r", encoding='utf-8-sig') as fp:
            har_dict = json.load(fp)
    except Exception as e:
        print("har 文件解析失败")
        print(str(e))
        exit()
    print("将har文件解析成字典 - success")
    return har_dict


def parse2caseList(har_dict):
    """
    将HAR字典对象解析，生成用例配置列表
    :param har_dict:
    :return:
    """
    print("解析har初始字典成用例列表")
    cases_list = []
    entries = har_dict.get("log").get("entries")
    for entry in entries:
        request = entry.get("request")
        url = parse.unquote(request.get("url"))
        api = parse.urlparse(url).path
        name = "_".join(str(api).lstrip("/").split("/"))
        method = request.get("method")
        if str(method).upper() == "GET":
            playload = queryString_dict(request.get("queryString", []))
        else:
            playload = postData_dict(request.get("postData", {}))
        case_dict = {
            "name": name,
            "method": method,
            "api": api,
            "playload": playload,
            "assert_list": [
                ["resp.status_code==200", "接口响应状态码不等于200"]
            ]
        }
        cases_list.append(case_dict)
    print("解析har初始字典成用例列表 - success")
    return cases_list


def postData_dict(postData):
    params = postData.get("params", [])
    playload = {}
    for item in params:
        playload[item.get("name")] = item.get("value")
    return playload


def queryString_dict(queryString):
    playload = {}
    for item in queryString:
        playload[item.get("name")] = item.get("value")
    return playload


def writeCasePyList(har_file, case_list):
    """
    将case 配置列表对象写入到py文件中
    :param har_file:
    :param case_list:
    :return:
    """
    py_file_name = os.path.join(BASE_DIR, "case_datas/case_py", Path(har_file).name.replace(".har", ".py"))
    print("用例列表写入py文件")
    try:
        with open(py_file_name, "w", encoding="UTF-8") as fp:
            fp.write("""case_list={}""".format(json.dumps(case_list, indent=4, ensure_ascii=False)))
    except Exception as e:
        print("用例列表写入py文件失败！{}".format(py_file_name))
        print(str(e))
    print("用例列表写入py文件 - success:{}".format(py_file_name))


def generate_case_list(har_file):
    """
    将HAR文件解析，生成用例配置文件
    :param har_file:
    :return:
    """
    case_list_parse = parse2caseList(load_har2_json(har_file))
    # case_list_parse去重
    api_list = []
    case_list = []
    for case in case_list_parse:
        api = case.get("api")
        if api not in api_list:
            case_list.append(case)
            api_list.append(api)
    writeCasePyList(har_file, case_list)
    return case_list


if __name__ == '__main__':
    har_file = "../case_datas/case_har/index.har"
    generate_case_list(har_file)

    # with open("tt.json","r",encoding="UTF-8") as fp:
    #     case_list = json.load(fp)
    # print(case_list)
    # print(type(case_list))
