COOLPAD_GET_CRUMB = 'http://jenkins.yulong.com:8080/crumbIssuer/api/json'
COOLPAD_UPLOAD_TBOARD_DATA = 'http://jenkins.yulong.com:8080/job/ODVB_cloud_TMach_result/buildWithParameters'


import requests, logging


class ReefLogger:

    def __init__(self, loggers):
        self.logger = logging.getLogger(loggers)

    def debug(self, log_content):
        self.logger.debug(log_content)

    def error(self, log_content):
        self.logger.error(log_content)


def try_ex_decorator(func):
    def wrapper(obj, log_info):
        try:
            return func(obj, log_info)
        except Exception as e:
            reef_logger = ReefLogger('debug')
            reef_logger.debug(
                f"\n"
                f"{'-' * 50}\n"
                f"Info: {log_info}\n"
                f"Exception info: {e}\n"
            )
    return wrapper


class Empty:

    pass


class ReefRequest:
    """
    封装请求，使用decorator捕获请求错误，写入debug log中。
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_singleton"):
            setattr(ReefRequest, "_singleton", super().__new__(cls))
        return cls._singleton

    def __init__(self, url, **kwargs):
        self.url = url
        self.kwargs = kwargs

    @try_ex_decorator
    def post(self, log_info):
        rep = requests.post(self.url, **self.kwargs)
        return rep

    @try_ex_decorator
    def get(self, log_info):
        rep = requests.get(self.url, self.kwargs)
        return rep


class CoolPadObj:

    def __int__(self):
        pass

    def end_tboard_upload_data(self, tboard):
        crumb, crumb_request_field = self.get_crumb_value()
        if (crumb or crumb_request_field) is None:
            return
        url = COOLPAD_UPLOAD_TBOARD_DATA
        # rds = Rds.objects.filter(tboard=tboard).first()
        body = {
            "file_path": "/dailybuild-nj/odvb/cp07_project/2022-09-27_3_cp07_r_ta/cp07_user_all_nonta/flash",
            "phones":
            [
                {
                    "FC": 0,
                    "ANR": 0,
                    "UFT": 3,
                    "status": "fail",
                    "number": 1,
                    "power_last_time": 34405
                },
                {
                    "FC": 2,
                    "ANR": 1,
                    "UFT": 3,
                    "status": "success",
                    "number": 2,
                    "power_last_time": 34405
                },
            ]
        }
        import json
        headers = {crumb_request_field: crumb}
        req = ReefRequest(url, **{'data': {"Message": json.dumps(body)}, 'headers': headers})
        res = req.post({'url': COOLPAD_UPLOAD_TBOARD_DATA})
        print(f'res: {res.text}')
        print(f'res status_code：{res.status_code}')

    def get_crumb_value(self):
        url = COOLPAD_GET_CRUMB
        crumb = None
        crumb_request_field = None
        reef_request = ReefRequest(url)
        res = reef_request.get({'url': COOLPAD_GET_CRUMB})
        print(res.text)
        try:
            crumb = res.json().get('crumb', None)
            crumb_request_field = res.json().get('crumbRequestField', None)
        except Exception as e:
            # logger = ReefLogger('backend')
            # logger.error(f'get CoolPad crumb parameter fail: \n'
            #              f'response: {res.content()} \n'
            #              f'e:{e}')
            print(f'get crumb val, e:{e}')
        return crumb, crumb_request_field


def init_open_module_factory(module_name):
    if module_name == 'coolpad':
        obj = CoolPadObj()
        print(f"{module_name} id: {id(module_name)}")
    return obj


if __name__ == '__main__':
    obj = init_open_module_factory('coolpad')
    obj.end_tboard_upload_data(1)

    # 模拟coolpad调用接口
    # url = 'http://127.0.0.1:8000/api/v1/open/insert_tboard/'
    # body = {
    #     "owner_label": 1,
    #     "repeat_time": 1,
    #     "board_name": "string1",
    #     "device_label_list": [
    #         "chiron---msm8998---86ac7cef"
    #     ],
    #     "job_label_list": [
    #         "job-396403ce-4b82-9d66-683c-0c2faa88341a"
    #     ],
    #     "belong": "coolpad"
    # }
    # req = ReefRequest(url, **{"json": body})
    # res = req.post({'url': url})
    # print(res.text)
