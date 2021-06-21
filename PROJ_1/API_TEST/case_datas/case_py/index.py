case_list=[
    {
        "name": "mch_web_v1_login",
        "method": "POST",
        "api": "/mch_web/v1/login",
        "playload": {
            "uname": "fht20210621",
            "passwd": "fht20210621"
        },
        "assert_list": [
            [
                "resp.status_code==200",
                "接口响应状态码不等于200"
            ]
        ]
    },
    {
        "name": "mch_web_v1_user",
        "method": "POST",
        "api": "/mch_web/v1/user",
        "playload": {},
        "assert_list": [
            [
                "resp.status_code==200",
                "接口响应状态码不等于200"
            ]
        ]
    },
    {
        "name": "mch_web_v1_mch_detail",
        "method": "POST",
        "api": "/mch_web/v1/mch_detail",
        "playload": {},
        "assert_list": [
            [
                "resp.status_code==200",
                "接口响应状态码不等于200"
            ]
        ]
    },
    {
        "name": "mch_web_v1_report_list_user_download",
        "method": "POST",
        "api": "/mch_web/v1/report/list_user_download",
        "playload": {},
        "assert_list": [
            [
                "resp.status_code==200",
                "接口响应状态码不等于200"
            ]
        ]
    }
]