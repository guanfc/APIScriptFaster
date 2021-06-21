"""
func: run pytest
"""
import pytest

from PROJ_1.API_TEST.utils.generate_case_confLists import generate_case_list
from PROJ_1.API_TEST.utils.generate_case_pytest import generate_py_case

new_case_list = False  # 是否通过har文件重新生成测试用例列表case_list,并且生成pytest用例，然后运行。
har_file = "case_datas/case_har/index.har"  # eg.case_datas/xxx.har 当new_case_list为True时，必填
py_test_file = "test_suits/test_index.py"  # eg.test_api/test_xxx.py 当new_case_list为True时，必填

if __name__ == '__main__':
    if new_case_list:
        if not har_file:
            print("har_file 未指定，请核实...")
            exit()
        case_list_gen = generate_case_list(har_file)
        generate_py_case(py_test_file, case_list_gen)
        pytest.main([py_test_file, "-s", "--pytest_report", "reports/API_Report.html"])

    else:
        pytest.main(["-s", "--pytest_report", "reports/API_Report.html", "--pytest_title", "富慧通"])
