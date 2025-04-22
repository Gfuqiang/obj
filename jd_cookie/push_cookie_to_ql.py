import time

import requests, re, sys, logging


FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel("INFO")

# TODO
# authorization 参数获取功能还没有实现需要手动获取后填入


class QLToolBase:
    """
    上传ck 基类
    两步操作:
        1. 获取ck
        2. 实现 update_ql_ck 方法上传ck
    """

    def __init__(self, ip, port, client_id='-wboyY71sCbz', client_secret='AVfcS4lvyhQW7XcSxx-3p9CM'):
        self._ip = ip
        self._port = port
        self._client_id = client_id
        self._client_secret = client_secret
        self._uri_prefix = f"http://{self._ip}:{self._port}/open"
        self.ql_token = None
        self.headers = None

        self.session = requests.session()
        self.get_ql_token()

        # url
        self.update_ql_ck_url = self._uri_prefix + f'/envs?t={int(time.time())}'

    def get_ql_token(self):
        url = self._uri_prefix + f'/auth/token?client_id={self._client_id}&client_secret={self._client_secret}'
        rep_data = self._request_ql(url, method='get')
        rep_data = rep_data.get('data', {})
        token = rep_data.get('token')
        token_type = rep_data.get('token_type')
        if not all([token, token_type]):
            logger.error(f"获取token失败，缺少必要参数。token: {token}, token_type: {token_type}")
        if not self.ql_token:
            self.ql_token = token
        if not self.headers:
            self.headers = {
                "Authorization": f"{token_type} {token}"
            }
            self.session.headers.update(self.headers)

    def _request_ql(self, url, method, body=None):
        try:
            if method in ['post', 'put']:
                req_method = getattr(self.session, method)
                rep = req_method(url, json=body)
            # if method == 'post':
            #     _request = self.session.post(url, json=body, headers=self.headers)
            # elif method == 'put':
            #     rep = self.session.put(url, json=body, headers=self.headers)
            elif method in ['get', 'delete']:
                req_method = getattr(self.session, method)
                rep = req_method(url)
            else:
                logger.error(f"method 方法不合法！！！")
                self._error_exist()
        except Exception as e:
            print(f'请求失败。method: {method} url: {url}, body: {body}\n e: {e}')
            self._error_exist()
        if rep.status_code != 200:
            print(f'请求response 状态码不是200\n rep: {rep.json()}')
            self._error_exist()
        rep_code = rep.json().get('my_code')
        # 200 请求成功
        if rep_code == 200:
            return rep.json()
        else:
            print(f'接口返回code不是200')
            logger.error(f"接口返回code不是200, my_code is {rep_code}")
            self._error_exist()

    def run_task(self, run_id_list):
        url = self._uri_prefix + f'/crons/run?t={int(time.time())}'
        body = run_id_list
        self._request_ql(url, body=body, method='put')
        logger.info(f"任务运行成功")

    @staticmethod
    def _error_exist(code=0):
        sys.exit(code)

    def update_ql_ck(self):
        raise NotImplementedError()


class UpdateELMCookie(QLToolBase):

    def __init__(self, cookie, *args, **kwargs):
        self._elm_cookie = cookie
        super(UpdateELMCookie, self).__init__(*args, **kwargs)

    def _re_get_cookie(self, grabCoupon=False):
        """
        SID=MWE5NjVkM2RiZjMwMWM3ODIzNzU1OTMyNGE1ZWQwYzDzCnqCMugvI65Gfq-hSppr;
        USERID=322425834; UTUSER=322425834; _tb_token_=eb7356d6de369;
        cookie2=1a965d3dbf301c78237559324a5ed0c0; csg=fe7e7d3e; munb=2204778094634;
        sgcookie=W100MvWMhxbc3ValVZ7e3MGP4V2C00bSjFQwbv0xQDR5J6vsgTHEr7ZRauuLBPKIEX0aFtoQllbrPK5pRwhZvQ9uLWysA4adW234ZJ%2BCNIMLQUU%3D;
        t=00d3e8aa48213da2fe6d5eeeb52eebf5; unb=2204778094634; isg=BGBg3yCQEJHniavgCB5CxsaBO2oyaUQz7Z_-U9pxLnsO1QT_gnnIwYD3a_vV_vwL;
        l=fBL4hsy7TUCCKPnEBOfanurza77OSCdYYuPzaNbMi9fPO3CB5Iy5W1GTjnL6C31RFsCJR3-rRv19BeYBm3xonxvt-H3LzzkmndLHR35..; tfstk=ccEfBQ_E1O6q2bhy5j6PQMHnfCiOwwssEac3hsm9vbLmWv1D2BlI_8PXJqnoF; x5check_ele=KnMKKfMR5H9E17ciySX%2BRrNmyR3pUtJEzW2Y3MeyMSo%3D; track_id=1669439848|8f63d49df3f5d3c1c9ff4680b9925158f68929c954ce362a73|01ce2e9ac66f06c948af5eba9ec56d9b; ubt_ssid=510363b5-e50b-45ed-b2ba-288e09d22f5b_2022-12-08; cna=f3DOG84QVWsCAX0hUbVnJEdc
        :return:
        cookie2=1a965d3dbf301c78237559324a5ed0c0;
        SID=MWE5NjVkM2RiZjMwMWM3ODIzNzU1OTMyNGE1ZWQwYzDzCnqCMugvI65Gfq-hSppr;
        USERID=322425834;grabCoupon=1;
        """
        try:
            # SID_pattern = re.compile(r'SID=.*?;')
            # cookie2_pattern = re.compile(r'cookie2=.*?;')
            # USERID_pattern = re.compile(r'USERID=.*?;')
            # ret_cookie = f"{SID_pattern.search(self.el_cookie).group()}" \
            #              f"{cookie2_pattern.search(self.el_cookie).group()}" \
            #              f"{USERID_pattern.search(self.el_cookie).group()}"
            pattern = re.compile(r"SID=.*?;|USERID=.*?;|cookie2=.*?;")
            ret_cookie = ''.join(pattern.findall(self._elm_cookie))
        except Exception as e:
            logger.error(f"正则elm cookie 错误，e:{e}")
            self._error_exist()
        else:
            logger.info(f"elm cookie: {ret_cookie}")
        if grabCoupon:
            # 开启10点抢卷
            ret_cookie += f"grabCoupon=1;"
        return ret_cookie

    def update_ql_ck(self, id):
        ret_ck = self._re_get_cookie()
        url = self._uri_prefix + f'/envs?t={int(time.time())}'
        body = {"remarks": "饿了么", "id": id, "name": "elmCookie", "value": ret_ck}
        self._request_ql(url, method='put', body=body)
        logger.info(f"更新elm ck成功")


class UpdateJDCookie(QLToolBase):

    def __init__(self, ck_list, *args, **kwargs):
        self._jd_ck_list = ck_list
        self.update_cookie_mapping = {
            "fqgg6261": {"remarks": "small", "id": 3, "name": "JD_COOKIE", "value": ""},
            "jd_449f21fd65112": {"remarks": "bb", "id": 2, "name": "JD_COOKIE", "value": ""},
            "fuqiang6261": {"remarks": "fq", "id": 5, "name": "JD_COOKIE", "value": ""}
        }
        super(UpdateJDCookie, self).__init__(*args, **kwargs)

    def _re_get_cookie(self, ck):
        try:
            pattern = re.compile(r'pt_key=.*?;|pt_pin=.*?;')
            ck = ''.join(pattern.findall(ck))
            pin_pattern = re.compile(r'pt_pin=(.*?);')
            pt_pin = pin_pattern.search(ck).groups(1)
        except Exception as e:
            logger.error(f"{__class__.__name__} 正则匹配异常，e: {e}")
            self._error_exist()
        else:
            logger.info(f"jd ck: {ck}")
            return pt_pin[0], ck

    def update_ql_ck(self):
        for ck in self._jd_ck_list:
            pt_pin, ck = self._re_get_cookie(ck)
            body = self.update_cookie_mapping.get(pt_pin)
            if not body:
                logger.warning(f"京东账号: {pt_pin} 没有获取到ql body")
                continue
            body['value'] = ck
            self._request_ql(self.update_ql_ck_url, method='put', body=body)
            logger.info(f"京东账号: {pt_pin} 更新成功")

    def enable_ck(self):
        url = self._uri_prefix + f'/envs/enable?t={time.time()}'
        for ck in self._jd_ck_list:
            pt_pin, _ = self._re_get_cookie(ck)
            user_info = self.update_cookie_mapping.get(f'{pt_pin}')
            if not user_info:
                continue
            if not (id := user_info.get('id')):
                continue
            self._request_ql(url, body=[id], method='put')
            logger.info(f"京东账号: {pt_pin} 启用成功")

    def main(self):
        # 更新jd ck
        self.update_ql_ck()
        # 启用jd ck
        self.enable_ck()


class PushCookieToQL:

    def __init__(self, update_url, enable_url):
        self.update_url = update_url
        self.enable_url = enable_url
        self.update_cookie_mapping = {
            "fqgg6261": {"remarks": "small", "id": 3, "name": "JD_COOKIE", "value": ""},
            "jd_449f21fd65112": {"remarks": "bb", "id": 2, "name": "JD_COOKIE", "value": ""}
        }
        self.headers = {
            'Authorization': self.get_authorization()
        }

    @staticmethod
    def _error_exist(code=0):
        sys.exit(code)

    def get_key_and_pin(self, cookie):
        pattern = re.compile(r'pt_key=.*; pt_pin=(.*?);')
        pt_v = pattern.search(cookie)
        if pt_v:
            if 'pt_key' and 'pt_pin' in pt_v.group():
                logger.info(f"pt_v: {pt_v.group()} pt_pin: {pt_v.group(1)}")
                return pt_v.group(), pt_v.group(1)
            else:
                print("pt_key 或 pt_pin 缺失")
                self._error_exist()
        else:
            print("没有匹配到pt_key 和 pt_pin")
            self._error_exist()

    def update_cookie(self, pt_pin, cookie):
        body = self.update_cookie_mapping.get(pt_pin)
        if not body:
            print('没有找到pt_pin!!!')
            self._error_exist()
        body['value'] = cookie
        if self._request_put(self.update_url, body=body):
            logger.info(f"账号{pt_pin}  上传cookie成功")
            return True
        else:
            return False

    def enable_cookie(self, pt_pin):
        user_info = self.update_cookie_mapping.get(pt_pin)
        if not user_info:
            print('没有找到pt_pin!!!')
            self._error_exist()
        id = user_info.get('id')
        if self._request_put(self.enable_url, body=[id]):
            logger.info(f"账号{pt_pin}  已启用")
            return True
        else:
            return False

    def get_authorization(self):
        authorization = 'Bearer eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoieUFXRlhnd1NXWVo5MVFDdW5uNmNoTDc4b0tvSGplc1JnX2NWWHBYY0dfclJTSHhTZVgwUXdDY1huNWk1NGRmWmt5V0JZQ2JCS2ZhR1ZGV3gxNXVWMGdITnAiLCJpYXQiOjE2Nzk4MTk2NjMsImV4cCI6MTY4MTU0NzY2M30.-_gJrKV7scbqZ5hHh5A_lSJgj52uJpRZMsBW3UfjRc-PPY6Fm0CPHjHDEDKkiqnU'
        return authorization

    def _request_put(self, url, body):
        try:
            rep = requests.put(url, json=body, headers=self.headers)
        except Exception as e:
            print(f'请求失败， url: {url}, body: {body}, e: {e}')
            self._error_exist()
        if rep.status_code != 200:
            print(f'请求response 状态码不是200')
            self._error_exist()
        rep = rep.json().get('my_code')
        # 200 请求成功
        if rep == 200:
            return True
        else:
            print(f'接口返回code不是200')
            self._error_exist()
        return True

    def main(self):
        cookie = """
        __jdu=16417872177981397062251; shshshfpa=4188198f-221f-cf20-86ea-770d8fa4451d-1641815589; shshshfpb=tqqOwKzRzi47T2v1EPETJdA; whwswswws=; TrackID=1vN0cdqVL0FHWhouv30oU2hR2h8yHJ5mMXuc5wR1B67y8p7SJKR6RmAROh5QRX_Z6PWhkj_L6RNm7Mw44uC2ia3xNGqMhsn6XEvumWCHv3siQyM8ELFkdSTF-KYLV4afA; pinId=pkLAatISw-C1ffsfn98I-w; jcap_dvzw_fp=P6gYrhSjPdocwFUXWsCCc1H_RP1WeM8Ko296i8cOXow12n_DPdnyGuQlPtj4Vdc2E4wy9Q==; commonAddress=4551928385; regionAddress=1%2C72%2C2819%2C0; shshshfpx=4188198f-221f-cf20-86ea-770d8fa4451d-1641815589; areaId=1; ipLoc-djd=1-2901-0-0; PCSYCityID=CN_110000_110100_0; __jda=76161171.16417872177981397062251.1641787217.1680942330.1680947415.73; CA1AN5BV0CA8DS2EPC=f7912810c8147dc3662188e64c9acc21; PCA9D23F7A4B3CSS=d2c03f3c3bfa7d05f6e9d135b81e543d; 3AB9D23F7A4B3CSS=jdd03IBKTXESLOIHJFABGIHHKLOMMYY4ZC7ORIUO5AWJFP7LJDQLZYOMVJTVZ4XHFIX5IZWYKEVDV4NFQ6RKDII5KIDLUQ4AAAAMHMBGB5RIAAAAADVIAMCKA3QKUNUX; _gia_d=1; unpl=JF8EAMlnNSttCxlQB0sKEhUYSQ5cWwoLTEcFZjJVBlRQHlINT1FJFkR7XlVdXxRKEh9ubhRUW1NPUg4ZCisSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwXEE1UUl1dDk0fCm9lDVJcX0hXARsyGiIXe21kW1gAShUKX2Y1VW0aHwgGGAQSE11LWlFeWwFNFANpYQ1dXVpDUgQcARgWEHtcZF0; __jdc=76161171; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_bc53a98693b94f26a78dac89d79ebc5e|1680947859631; 3AB9D23F7A4B3C9B=IBKTXESLOIHJFABGIHHKLOMMYY4ZC7ORIUO5AWJFP7LJDQLZYOMVJTVZ4XHFIX5IZWYKEVDV4NFQ6RKDII5KIDLUQ4; wxa_level=1; retina=1; cid=9; jxsid=16809478689491854213; appCode=ms0ca95114; visitkey=8069746892876717351; webp=1; mba_muid=16417872177981397062251; cd_eid=jdd03IBKTXESLOIHJFABGIHHKLOMMYY4ZC7ORIUO5AWJFP7LJDQLZYOMVJTVZ4XHFIX5IZWYKEVDV4NFQ6RKDII5KIDLUQ4AAAAMHMBGB5RIAAAAADVIAMCKA3QKUNUX; autoOpenApp_downCloseDate_jd_homePage=1680947869600_1; __wga=1680947871863.1680947871863.1680947871863.1680947871863.1.1; PPRD_P=UUID.16417872177981397062251; jxsid_s_t=1680947871914; jxsid_s_u=https%3A//home.m.jd.com/myJd/home.action; sc_width=390; _gia_s_local_fingerprint=09bd26fd47cbd08b4ffbecb87948d64d; equipmentId=IBKTXESLOIHJFABGIHHKLOMMYY4ZC7ORIUO5AWJFP7LJDQLZYOMVJTVZ4XHFIX5IZWYKEVDV4NFQ6RKDII5KIDLUQ4; fingerprint=09bd26fd47cbd08b4ffbecb87948d64d; deviceVersion=604.1; deviceOS=ios; deviceOSVersion=13.2.3; deviceName=Safari; _gia_s_e_joint={"eid":"IBKTXESLOIHJFABGIHHKLOMMYY4ZC7ORIUO5AWJFP7LJDQLZYOMVJTVZ4XHFIX5IZWYKEVDV4NFQ6RKDII5KIDLUQ4","ma":"","im":"","os":"Mac OS X (iPhone)","ip":"123.112.19.62","ia":"","uu":"","at":"6"}; shshshfp=14849c9b6aa4530e6ccb1ea1b407e0af; shshshsID=ef14b72c27df69424d6721faccb2beba_7_1680947872795; mba_sid=16809478690817012233667794299.4; TrackerID=CYgPjmipbl9_1pt50A5cwNMxTPcUCh5rjMVjWISX7ClZNFcCc8a4AXgxiBO9c0odBkYyTe4iaeUne2oawcxJ-s8TRW8mxGPVyvdSHzr8TuxB0-yQIIMnDCVcMS0KnVAE0ah6_RerE1Hy-mlOE0Afyw; pt_key=AAJkMTq0ADCluDQlh-1WA6wTxE-d07iFLYVH0fpTdCTe8p5Qr1XerIAftH7rqF2uqcmA3W4_AIw; pt_pin=jd_449f21fd65112; pt_token=jikrrtqo; pwdt_id=jd_449f21fd65112; sfstoken=tk01mbd1a1c42a8sMXgzKzIrM3k3gTdKnihDjj3TD5IlI6NyYydBKFBn8aw2OPpeg2dH9jbPl73Gp3KerwI8yqXs97/q; __jd_ref_cls=MLoginRegister_LoginSuccess; wqmnx1=MDEyNjM4Ny9qeS44ODdsKCBvM2tTbC81LGVyLmk0aTNZbkIxVUYhSA%3D%3D; __jdb=76161171.13.16417872177981397062251|73.1680947415
        """
        cookie, pt_pin = self.get_key_and_pin(cookie)
        if not self.update_cookie(pt_pin, cookie):
            logger.error(f"上传cookie失败")
            self._error_exist()
        if not self.enable_cookie(pt_pin):
            logger.error(f"启用cookie失败")
            self._error_exist()
        logger.info(f"账号 {pt_pin} 更新成功")


if __name__ == '__main__':
    # update_url = f'http://39.107.118.84:5881/api/envs?t={time.time()}'
    # enable_url = f'http://39.107.118.84:5881/api/envs/enable?t={time.time()}'
    #
    # push_c = PushCookieToQL(update_url=update_url, enable_url=enable_url)
    # push_c.main()

    # server = 'local'
    server = 'ali_cloud'
    if server == 'local':
        ip = '192.168.1.8'
        port = '5700'
        client_id = 'YfA_R-b9gJbN'
        client_secret = 'IXQLnZbLTjk8ygo-Sg8w-puc'
        ql_elm_id = 2
    elif server == 'ali_cloud':
        ip = '39.107.118.84'
        client_id = '-wboyY71sCbz'
        port = '5881'
        client_secret = 'AVfcS4lvyhQW7XcSxx-3p9CM'
        ql_elm_id = 5
    else:
        logger.error("没有对应的服务")
        sys.exit(0)


    # 更新jd
    jd_ck_lsit = [
        "muid=16883963068511080147485.919.1688799712041; shshshfpa=7ff5bfc5-e738-3a06-ae2c-a3d8a38815a0-1648685830; shshshfpb=pxkRf3P6vPjeO1rFoJuu1gL23818oIYP82uvdzkZHApWHSyDx5bEm3Dl0bUsIiV0kUiRkvUOEYMDltV62phMYuzYjIH_nUC2z8ypDCkQpXcF1xUfDKNC4iA8Ha3W4_1c-6sqWiAO90ABmjZWPFpC7LM94RUJ12Qvz8M73nHPf-Zl-sdlRSkSvnfYA7BN09qOn; unionwsws=%7B%22devicefinger%22%3A%22eidId4bb8121cbscsdbqN1GOR%2Ba7XlFxO2fswbHW67Y%2FX5SsKeG5nWoFxj8mKbsAbI%2F5wzhWPFp4AhADiE5L9kTEAFH3UMGRaimaahFwnAadOJvJrO1I%22%7D; __jda=122270672.16883963068511080147485.1688396306.1688622775.1688799699.7; unpl=V2_ZzNsbRZQQRUgAURWZ01cB2IfF1QRBV8ccQpDSClLWgdnUBVeEABLQGlJKFRzEVQZJkB8XUNWQRV0FBYRFR1dBWIEFUEDCi0XcwpBSD9GGWtkBxBbSksRUBsAQVx4HlsZIlV8CQsSLRVpDE9IeQUZUy4fFlxCX0EScBRGUngaQAZmABBcRVZBJXYJRVZnGFsZZgEDXkJcQRB%2BC0BkeylcBGYCE15AVUoQRTh2VHkpXTVnBBRbRlBHEH0IQ1d%2FGVgCZwASWktecxJxDkdSLB9UGWULElxeUkIRdBQWAStLQAAwVxMJElAXECUBEWR9Hw%3D%3D%7CJF8EAN5nNSttCkIDBE8CGRRHTF9QWwoLSkQDbzcBVglcTVwEEwZIG0B7XlVdXxRKER9uYhRXXlNKUg4fAisSFHtdVV9eAU4TAWduNVddWUJdDR8GKxITSjNWVl8ASRUHZ2ZrVF02JVFrKwEbIhF7VAdaXgxCHlQ9ZwAGDVofV1FIVhkXQk0JAQxUWh9EAWk0VQEPX0JcBysDKxsRe11VX18OSR8Db24HUlxfe2QEKwMrEyAAM1UTVFtPFAdmblIGXV0ZBAdPAU9BRElYBlgJXRkeUTs0B1IOCB4GAhIKGSIRe10; pt_key=app_openAAJkqQmnADCceBPgBdzbyLPQ3tODwBbDeytHDjk5H5tRJXNa76ptxCAYkN1I5aiiS0LRO43V1mk; pt_pin=fuqiang6261; pwdt_id=fuqiang6261; sid=8592ed4d808128d128eb4e9aa62618ew; 3AB9D23F7A4B3C9B=CPXPPKCCAAMXBQWCBJEX6H4HA5XYLDLBK5HYHI6KPAOKHURNOFCBEOK5JM7CE2GJCTQW6YVNSJJ3TUZSVBG3OUP3VE; 3AB9D23F7A4B3CSS=jdd03CPXPPKCCAAMXBQWCBJEX6H4HA5XYLDLBK5HYHI6KPAOKHURNOFCBEOK5JM7CE2GJCTQW6YVNSJJ3TUZSVBG3OUP3VEAAAAMJFHCR5XYAAAAADIBHBPQUKDSKHIX; shshshfpx=7ff5bfc5-e738-3a06-ae2c-a3d8a38815a0-1648685830"
        # "__jdu=16417872177981397062251; shshshfpa=4188198f-221f-cf20-86ea-770d8fa4451d-1641815589; shshshfpb=tqqOwKzRzi47T2v1EPETJdA; whwswswws=; TrackID=1vN0cdqVL0FHWhouv30oU2hR2h8yHJ5mMXuc5wR1B67y8p7SJKR6RmAROh5QRX_Z6PWhkj_L6RNm7Mw44uC2ia3xNGqMhsn6XEvumWCHv3siQyM8ELFkdSTF-KYLV4afA; pinId=pkLAatISw-C1ffsfn98I-w; jcap_dvzw_fp=P6gYrhSjPdocwFUXWsCCc1H_RP1WeM8Ko296i8cOXow12n_DPdnyGuQlPtj4Vdc2E4wy9Q==; commonAddress=4551928385; regionAddress=1%2C72%2C2819%2C0; shshshfpx=4188198f-221f-cf20-86ea-770d8fa4451d-1641815589; shshshfp=7a39bb7c43bdc281df04e68bceced518; unpl=JF8EAMpnNSttDUIEBkwLEhoSSVoGW1sNH0cGamEMB1tcGVVRHQMeGhR7XlVdXxRKER9vZhRUWFNKVA4YASsSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwXEE1UUl1dDk0fCm9lDVJcX0hXARsyGiIXe21kXVgMSRQCX2Y1VW0aHwgAEgcfExcGXVNbXQ5CEQBvYQNcVFhJXAMaBRgRFEttVW5e; __jda=76161171.16417872177981397062251.1641787217.1686988066.1688968884.80; __jdc=76161171; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_d8a2f889336c474ea4478b75c0e70495|1688968883760; areaId=1; ipLoc-djd=1-2800-0-0; 3AB9D23F7A4B3CSS=jdd03IBKTXESLOIHJFABGIHHKLOMMYY4ZC7ORIUO5AWJFP7LJDQLZYOMVJTVZ4XHFIX5IZWYKEVDV4NFQ6RKDII5KIDLUQ4AAAAMJHZR7ETQAAAAACKT6LA2LZH6AAYX; _gia_d=1; PCSYCityID=CN_110000_110100_0; 3AB9D23F7A4B3C9B=IBKTXESLOIHJFABGIHHKLOMMYY4ZC7ORIUO5AWJFP7LJDQLZYOMVJTVZ4XHFIX5IZWYKEVDV4NFQ6RKDII5KIDLUQ4; wxa_level=1; retina=1; cid=9; jxsid=16889688910230992581; appCode=ms0ca95114; webp=1; visitkey=6162957801223011175; mba_muid=16417872177981397062251; autoOpenApp_downCloseDate_jd_homePage=1688968891949_1; cd_eid=jdd03IBKTXESLOIHJFABGIHHKLOMMYY4ZC7ORIUO5AWJFP7LJDQLZYOMVJTVZ4XHFIX5IZWYKEVDV4NFQ6RKDII5KIDLUQ4AAAAMJHZR7ETQAAAAACKT6LA2LZH6AAYX; PPRD_P=UUID.16417872177981397062251; jxsid_s_u=https%3A//home.m.jd.com/myJd/home.action; equipmentId=IBKTXESLOIHJFABGIHHKLOMMYY4ZC7ORIUO5AWJFP7LJDQLZYOMVJTVZ4XHFIX5IZWYKEVDV4NFQ6RKDII5KIDLUQ4; fingerprint=b4a4564fc4d1e3fe92f0591d9a81c487; deviceVersion=604.1; deviceOS=ios; deviceOSVersion=13.2.3; deviceName=Safari; sc_width=414; shshshsID=53ba00d57ac6d5672632030d3a66c479_1_1688968895956; TrackerID=KT7h61kWDnYRcC1gZkqRzl9hSpb2zkpkiwFak1sWtM2cfvNDc0zZd_wn-2MsJdWZRFhfRisxr_iZOxiKoaGbBLba37UM_P2baSyyxKYZiVD6b6hwaLlylT94KgnKbJuYYAYNmeDa5eXrTc4QsuzxJg; pt_key=AAJkq57hADCyjsfjHQfLsurFFGltYrUj0l0iqwvyjT0l3ya1dKLtvJ4p5Uacov7YfnMlUpONUrE; pt_pin=jd_449f21fd65112; pt_token=762h2baf; pwdt_id=jd_449f21fd65112; sfstoken=tk01mbbf11c3ba8sMisydlFwRW9yI0jmQHYZ60gQiT4NMVEBq6vMyuHjGvuH71qjVG58z32j4DyNaEqF9BaFUxU7Vhtq; wqmnx1=MDEyNjM1MGg6bWptZGVpNjUyMW9hIG9DUCAzICBPIGVpNTVUbEcpczEzaTUgcjQ5ZjduMjQyWU9PVSFIJQ%3D%3D; __jdb=76161171.7.16417872177981397062251|80.1688968884; mba_sid=16889688914054778637548309455.4; __wga=1688968930469.1688968894111.1688968894111.1688968894111.2.1; jxsid_s_t=1688968930506"
    ]
    if jd_ck_lsit:
        jd = UpdateJDCookie(ip=ip, port=port,  client_id=client_id, client_secret=client_secret, ck_list=jd_ck_lsit)
        jd.main()

    # 更新elm
    elm_ck = ''
    if elm_ck:
        elm = UpdateELMCookie(ip=ip, port=port, client_id=client_id, client_secret=client_secret, cookie=elm_ck)
        elm.update_ql_ck(ql_elm_id)
    # elm.run_task([296])
