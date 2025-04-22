import json
import logging
import pathlib
import pprint
import random
import sys
import time

import pandas as pd
from html.parser import HTMLParser

import requests



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 创建控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 创建格式化器
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# 将格式化器添加到处理器
console_handler.setFormatter(formatter)

# 将处理器添加到logger对象
logger.addHandler(console_handler)

"""
微步漏洞爬取
"""


class MyHTMLParser(HTMLParser):
    def __init__(self, tag):
        self.tag = tag
        self.is_target_tag = False
        self.data = []
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag == self.tag:
            self.is_target_tag = True

    def handle_endtag(self, tag):
        if tag == self.tag:
            self.is_target_tag = False

    def handle_data(self, data):
        if self.is_target_tag:
            self.data.append(data.strip())


class FormatHtmlData:

    def __init__(self):
        self.parser = MyHTMLParser('script')

    def extract_vuln_data(self, html_content):
        self.parser.feed(str(html_content))
        for item in self.parser.data:
            start_flag = 'window.__INITIAL_STATE__='
            if item and item.startswith(start_flag):
                vuln_info = item[len(start_flag):]
                vuln_info = vuln_info.strip(';')
                vuln_info = vuln_info.replace('\n', '')
                try:
                    vuln_info_dict = json.loads(vuln_info)
                except Exception:
                    logger.error(f'{vuln_info} 序列化失败')
                    continue
                ret_vuln_data = self.cleanse_data(vuln_info_dict)
                if not ret_vuln_data:
                    logger.error(f'{vuln_info_dict} 清洗结果为空')
                    continue
                return ret_vuln_data
                # print(vuln_info)
                # pprint.pprint(json.loads(vuln_info))

    def cleanse_data(self, vuln_info_dict):
        ret_data = {}
        if vuln_info_dict.get('title') == '查询提示':
            logger.error(f'触发人机检查')
            sys.exit(1)
        data = vuln_info_dict.get('data', {})
        summaryInfo = data.get('summaryInfo', {})
        ret_data['title'] = data.get('resourceName', '')
        ret_data['vulnOpenTime'] = summaryInfo.get('hole_publish_time', '')
        ret_data['vulnUpdateTime'] = summaryInfo.get('hole_update_time', '')
        ret_data['cveId'] = summaryInfo.get('cve_id', '')
        ret_data['vulnType'] = summaryInfo.get('hole_class', '')
        ret_data['overallRating'] = summaryInfo.get('hole_grade_zh', '')
        ret_data['vulnPlatform'] = hole_platform_list[0] if\
            (hole_platform_list := summaryInfo.get('hole_platform_list', [])) else ''
        ret_data['cnnvdId'] = cnnvd_id[0] if (cnnvd_id := summaryInfo.get('_cnnvd_id', [])) else ''
        ret_data['cnvId'] = cnvd_id[0] if (cnvd_id := summaryInfo.get('_cnvd_id', [])) else ''
        ret_data['xveId'] = data.get('resource', '')
        # ret_data['cvss3'] =
        # ret_data['cvss2'] =
        ret_data['vulnDescription'] = summaryInfo.get('hole_description', '')
        # ret_data['timeLine'] =
        ret_data['affectManufacturers'] = affect_vendors[0] \
            if (affect_vendors := summaryInfo.get('affect_vendors', [])) else ''
        ret_data['productAffected'] = affect_products[0] \
            if (affect_products := summaryInfo.get('affect_products', [])) else ''
        return ret_data


class WBRequest:
    def __init__(self):
        self.search_headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "day_first_activity=true; csrfToken=04MVajLRdcE94YdjQAggA2l0; day_first=true; rememberme=65096802eb69a095406c89015e56c90da0b846b6|7c0cb3e8d4434ff89689181637f0df63|1704770642752|public|w; xx-csrf=65096802eb69a095406c89015e56c90da0b846b6; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%227c0cb3e8d4434ff89689181637f0df63%22%2C%22first_id%22%3A%2218ce7e928f7eca-0ad8637340af4d8-1f525637-3686400-18ce7e928f82c78%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fpassport.threatbook.cn%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThjZTdlOTI4ZjdlY2EtMGFkODYzNzM0MGFmNGQ4LTFmNTI1NjM3LTM2ODY0MDAtMThjZTdlOTI4ZjgyYzc4IiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiN2MwY2IzZThkNDQzNGZmODk2ODkxODE2MzdmMGRmNjMifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%227c0cb3e8d4434ff89689181637f0df63%22%7D%2C%22%24device_id%22%3A%2218ce7e928f7eca-0ad8637340af4d8-1f525637-3686400-18ce7e928f82c78%22%7D",
            "Dnt": "1",
            "Referer": "https://x.threatbook.com/v5/vul/keyword/search?q=Smartbi",
            "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"macOS\"",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        self.resource_headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Content-Type": "application/json",
            "Cookie": "day_first_activity=true; csrfToken=04MVajLRdcE94YdjQAggA2l0; day_first=true; rememberme=65096802eb69a095406c89015e56c90da0b846b6|7c0cb3e8d4434ff89689181637f0df63|1704770642752|public|w; xx-csrf=65096802eb69a095406c89015e56c90da0b846b6; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%227c0cb3e8d4434ff89689181637f0df63%22%2C%22first_id%22%3A%2218ce7e928f7eca-0ad8637340af4d8-1f525637-3686400-18ce7e928f82c78%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fpassport.threatbook.cn%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThjZTdlOTI4ZjdlY2EtMGFkODYzNzM0MGFmNGQ4LTFmNTI1NjM3LTM2ODY0MDAtMThjZTdlOTI4ZjgyYzc4IiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiN2MwY2IzZThkNDQzNGZmODk2ODkxODE2MzdmMGRmNjMifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%227c0cb3e8d4434ff89689181637f0df63%22%7D%2C%22%24device_id%22%3A%2218ce7e928f7eca-0ad8637340af4d8-1f525637-3686400-18ce7e928f82c78%22%7D",
            "Dnt": "1",
            "Referer": "https://x.threatbook.com/v5/vul/XVE-2023-4875?searchStr=CVE-2023-23397",
            "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"macOS\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "X-Csrf-Token": "04MVajLRdcE94YdjQAggA2l0",
            "Xx-Csrf": "65096802eb69a095406c89015e56c90da0b846b6"
        }
        self.search_url = 'https://x.threatbook.com/v5/vul/'
        self.resource_url = 'https://x.threatbook.com/v5/node/query/vul/resource?resource='

    def get_request(self, url, headers):
        time.sleep(random.randint(30, 60))
        rep = requests.get(url=url, headers=headers)
        if rep.status_code != 200:
            print(f'rep 返回值不是 200， {rep.status_code}')
            return
        return rep

    def get_vuln_detail(self, xve_code):
        resource = self.get_vuln_resource(xve_code)
        if not resource:
            logger.error(f'resource 没有获取到')
            return
        req_url = self.search_url + resource + '?searchStr=' + xve_code
        print(req_url)
        rep = self.get_request(req_url, self.search_headers)
        if not rep:
            return
        return rep.text

    def get_vuln_resource(self, code):
        req_url = self.resource_url + code
        rep = self.get_request(req_url, self.resource_headers)
        if not rep:
            return
        rep_data = rep.json()
        if rep_data.get('response_code') != 0:
            logger.error(f'rep my_code 不为0')
            return
        return rep_data.get('data')


def write_excel(vuln_data):
    column_mapping = {
        '_id': '主键ID',
        '_guid': '数据全局ID',
        '_adapters': '适配器',
        '_adapters_data': '适配器数据',
        'id': '数据ID',
        'assetDisplayName': '显示名称',
        'status': '状态',
        'updateTime': '最后更新时间',
        'lastSeenTime': '最后发现时间',
        'firstSeenTime': '首次发现时间',
        'tags': '标签',
        'ownerId': '负责人ID',
        'ascriptionDepartmentId': '所属部门ID',
        'businessSystemId': '业务系统ID',
        'cveId': 'CVE编号',
        'cvss2': 'CVSS 2.X',
        'cvss3': 'CVSS 3.X',
        'solution': '公开程度',
        'title': '标题',
        'overallRating': '综合评级',
        'vulnOpenTime': '漏洞公开时间',
        'vulnUpdateTime': '漏洞更新时间',
        'cnnvdId': 'CNNVD编号',
        'cnvId': 'CNVD编号',
        'xveId': 'XVE编号',
        'reportId': '报告编号',
        'vulnType': '漏洞类型',
        'usage_method': '利用方式',
        'vulnPlatform': '漏洞平台',
        'affectManufacturers': '影响厂商',
        'productAffected': '影响产品',
        'magnitude_of_impact': '影响量级',
        'threat_type': '威胁类型',
        'technology_type': '技术类型',
        'technical_details': '技术细节',
        'attack_path': '攻击路径',
        'attack_complexity': '攻击复杂度',
        'exp_maturity': 'EXP成熟度',
        'data_confidentiality': '数据保密性',
        'data_integrity': '数据完整性',
        'permission_requirement': '权限要求',
        'influence_scope': '影响范围',
        'vulnDescription': '漏洞描述',
        'eligibility': '利用条件',
        'interaction_requirements': '交互要求',
        'qvdId': '解决方案',
        'poc': 'PoC',
        'patch': '补丁列表',
        'reference_information': '参考信息',
        'time_line': '时间线',
        'related_content': '相关内容',
        'detection_rules': '检测规则',
        'isCPE': 'CPE',
        'url': '网址'}
    path = pathlib.Path('./微步漏洞数据1.xlsx')
    df = pd.DataFrame(vuln_data)
    df.rename(columns=column_mapping, inplace=True)
    df.to_excel(path)


def main():
    copy = [
        'CVE-2023-2825', 'CVE-2023-28432', 'CVE-2023-23397', 'CVE-2023-21839', 'CNVD-2023-45001',
        'CVE-2023-33246', 'CVE-2023-27363', 'CVE-2023-31039', 'CVE-2023-38646', 'CVE-2023-20860',
        '暂无', 'CNVD-2023-02709', 'CVE-2022-33891', 'CVE-2022-26134', 'CVE-2022-23131',
    ]
    code_list = [
                    'CVE-2022-1388', 'CNVD-2022-86535', 'CVE-2022-24706', 'CVE-2022-0543', 'CVE-2022-0847',
                    'CVE-2021-21972', '暂无', 'CVE-2021-44228', '暂无', 'CVE-2023-32315']
    # code_list = ['CVE-2023-28432', 'CNVD-2023-45001']
    wb_request = WBRequest()
    vuln_data = []
    for item_code in code_list:
        print(item_code)
        if item_code == '暂无':
            continue
        rep_content = wb_request.get_vuln_detail(item_code)
        print(f'{rep_content=}')
        if not rep_content:
            logger.error(f'{item_code} 没有获取到详情, 跳过')
            continue
        format_html = FormatHtmlData()
        vuln_info_dict = format_html.extract_vuln_data(rep_content)
        if vuln_info_dict:
            print(f'{item_code} 获取数据成功, {vuln_info_dict=}')
            vuln_data.append(vuln_info_dict)
            print(vuln_data)
    # write data to excel
    if not vuln_data:
        logger.error(f'数据为空，不写入excel文件')
        return
    write_excel(vuln_data)


def html_parser():
    # 创建解析器实例并解析HTML
    html_content = """
rep_content='<!doctype html><!DOCTYPE html>\n<html lang="zh-CN">\n\n<head>\n  <title>微步在线X情报社区-威胁情报查询_威胁分析平台_开放社区</title>\n  <meta name="keywords" content="威胁情报,情报查询,开放社区,威胁分析平台,X情报社区">\n  <meta name="description" content="微步在线X情报社区是国内首个综合性威胁分析平台和威胁情报共享的开放社区，同时提供威胁情报查询、域名反查、IP反查，行业情报等服务，辅助个人及企业快速定位及排除安全隐患">\n  <meta http-equiv="content-type" content="text/html;charset=utf-8">\n  <meta name="viewport" content="initial-scale=1, maximum-scale=5, minimal-ui">\n  <link rel="shortcut icon" href="/public/asset/img/favicon.ico?t=1" type="image/x-icon" />\n  <script>\n    function _xImportStyle(str){\n      var styleEl = document.createElement("style");\n      var _doc = document;\n      _doc.getElementsByTagName("head")[0].appendChild(styleEl);\n      if(styleEl.styleSheet){\n        styleEl.styleSheet.cssText = str\n      } else {\n        styleEl.appendChild(_doc.createTextNode(str))\n      }\n    };\n    function winInsertScrollbar(){\n      var isMac = /macintosh|mac os x/i.test(navigator.userAgent);\n      if(!isMac) {\n        _xImportStyle(\'* {scrollbar-width: thin;}::-webkit-scrollbar{width:4px;height:4px;}::-webkit-scrollbar-thumb{border-radius:4px;background-color:#ccc;}::-webkit-scrollbar-track{border-radius:1px;background-color:#f0f0f0;}\')\n      }\n    }\n    winInsertScrollbar()\n  </script>\n  <script>\n    (function () {\n      var emptyFun = function () {};\n      if (Object && Object.defineProperty && typeof Object.defineProperty === \'function\') {\n        [\'alert\', \'confirm\', \'prompt\'].forEach(function (curr) {\n          Object.defineProperty(window, curr, {\n            configurable: false,\n            enumerable: false,\n            value: emptyFun,\n            writable: false\n          })\n        })\n      }\n      try {\n        window.alert = emptyFun;\n        window.confirm = emptyFun;\n        window.prompt = emptyFun;\n      } catch (err) {}\n    })()\n  </script>\n<link rel="stylesheet" href="/public/css/common.852e5888.css"><link rel="stylesheet" href="/public/css/result/vul.42a30ae5.css"></head>\n\n<body>\n  <script src="/public/asset/file/sensorsdata.min.js?t=1"></script>\n  <div id="app"></div>\n  <script src="/public/asset/js/gt4.js"></script>\n  <script src="/public/asset/js/wxLogin.js"></script>\n<script> window.__INITIAL_STATE__= {"csrf":"E7tt1yj0-GXS81yencD8rFg3x0d4jXbbbM5s","title":"Nacos Jraft Hessian反序列漏洞 -漏洞详情 - X情报社区","data":{"userInfo":{"graphDisable":false,"userId":"7c0cb3e8d4434ff89689181637f0df63","isLogin":true,"id":"7c0cb3e8d4434ff89689181637f0df63","userImg":"https:\\u002F\\u002Fimg.threatbook.com\\u002F5f2125cea3a553edaf04ca0f8d3964ceefb1b266f1ebcba74a2781d7daba0a86.png","nickName":"6ce52fc346f14","email":"8dfade06004a4e71a8abd374135257df","bindWx":false,"company":false},"searchStr":"CNVD-2023-45001","resource":"XVE-2023-17768","resourceName":"Nacos Jraft Hessian反序列漏洞","resourceType":"vul","summaryInfo":{"count":2,"holeResource":"62389806630370ec6556b07c9fa3bc6bcc634a0e530950b19184724abeaaaa7d","thrType":{"my_code":"5","en":"Unknown","zh":"未知"},"solutionsList":[],"solutionsListZh":[{"source":"CNVD","text":"用户可参考如下供应商提供的安全公告获得补丁信息：https:\\u002F\\u002Fgithub.com\\u002Falibaba\\u002Fnacos\\u002Freleases\\u002Ftag\\u002F1.4.6https:\\u002F\\u002Fgithub.com\\u002Falibaba\\u002Fnacos\\u002Freleases\\u002Ftag\\u002F2.2.3","url":"https:\\u002F\\u002Fgithub.com\\u002Falibaba\\u002Fnacos\\u002Freleases\\u002Ftag\\u002F1.4.6https:\\u002F\\u002Fgithub.com\\u002Falibaba\\u002Fnacos\\u002Freleases\\u002Ftag\\u002F2.2.3"}],"id":"XVE-2023-17768","cve_id":"","_cnvd_id":["CNVD-2023-45001"],"_cnnvd_id":[],"hole_name":"Nacos Jraft Hessian反序列漏洞","hole_class":"通用型漏洞","hole_grade":"HIGH","hole_grade_zh":"高危","hole_publish_time":"2023-06-08","hole_update_time":"2023-06-08","thr_type_zh":"未知","is_solution":true,"is_poc":false,"is_exp":false,"poc_exist":false,"poc_details":[],"exp_exist":false,"is_rce":false,"is_safeguard":false,"is_oppose":false,"hole_description":"Nacos是Dynamic Naming and Configuration Service的首字母简称，一个更易于构建云原生应用的动态服务发现，配置管理和服务管理平台。Nacos Jraft Hessian存在反序列漏洞，攻击者可利用该漏洞远程执行代码。","affect_vendors":[],"affect_products":["Alibaba Nacos \\u003E= 1.4.0，\\u003C 1.4.6","Alibaba Nacos \\u003E= 2.0.0，\\u003C 2.2.3"],"x_exp_details":[],"reference_info_count":"0","hole_reference_infos":[]},"query":{"searchStr":"CNVD-2023-45001"}}};</script><script type="text/javascript" src="/public/js/vendor.b8a65747.js"></script><script type="text/javascript" src="/public/js/runtime.00de9a33.js"></script><script type="text/javascript" src="/public/js/chunk/common.8c32f78d.js"></script><script type="text/javascript" src="/public/js/chunk/result/vul.330f09df.js"></script></body>\n\n</html>\n'

    """
    html_content_two = """
    <!doctype html>
   <!DOCTYPE html>
      <html lang="zh-CN">
         <head>
            <title>
               微步在线X情报社区-威胁情报查询_威胁分析平台_开放社区
            </title>
            <meta name="keywords" content="威胁情报,情报查询,开放社区,威胁分析平台,X情报社区">
            <meta name="description" content="微步在线X情报社区是国内首个综合性威胁分析平台和威胁情报共享的开放社区，同时提供威胁情报查询、域名反查、IP反查，行业情报等服务，辅助个人及企业快速定位及排除安全隐患">
            <meta http-equiv="content-type" content="text/html;charset=utf-8">
            <meta name="viewport" content="initial-scale=1, maximum-scale=5, minimal-ui">            <link rel="shortcut icon" href="/public/asset/img/favicon.ico?t=1" type="image/x-icon" />
            <script>    function _xImportStyle(str){      var styleEl = document.createElement("style");      var _doc = document;      _doc.getElementsByTagName("head")[0].appendChild(styleEl);      if(styleEl.styleSheet){        styleEl.styleSheet.cssText = str      } else {        styleEl.appendChild(_doc.createTextNode(str))      }    };    function winInsertScrollbar(){      var isMac = /macintosh|mac os x/i.test(navigator.userAgent);      if(!isMac) {        _xImportStyle('* {scrollbar-width: thin;}::-webkit-scrollbar{width:4px;height:4px;}::-webkit-scrollbar-thumb{border-radius:4px;background-color:#ccc;}::-webkit-scrollbar-track{border-radius:1px;background-color:#f0f0f0;}')      }    }    winInsertScrollbar()  </script><script>    (function () {      var emptyFun = function () {};      if (Object && Object.defineProperty && typeof Object.defineProperty === 'function') {        ['alert', 'confirm', 'prompt'].forEach(function (curr) {          Object.defineProperty(window, curr, {            configurable: false,            enumerable: false,            value: emptyFun,            writable: false          })        })      }      try {        window.alert = emptyFun;        window.confirm = emptyFun;        window.prompt = emptyFun;      } catch (err) {}    })()  </script>
         <link rel="stylesheet" href="/public/css/common.852e5888.css">
         <link rel="stylesheet" href="/public/css/result/vul.42a30ae5.css"></head>
         <body>
            <script src="/public/asset/file/sensorsdata.min.js?t=1"></script>
            <div id="app"></div>
            <script src="/public/asset/js/gt4.js"></script><script src="/public/asset/js/wxLogin.js"></script><script> window.__INITIAL_STATE__= {"csrf":"ij3nsynQ-huPge5y9aV9_EpNvnQeb_Qq6r2Q","title":"Apache Dubbo 反序列化远程代码执行漏洞 -漏洞详情 - X情报社区","data":{"userInfo":{"graphDisable":false,"userId":"7c0cb3e8d4434ff89689181637f0df63","isLogin":true,"id":"7c0cb3e8d4434ff89689181637f0df63","userImg":"https:\u002F\u002Fimg.threatbook.com\u002F5f2125cea3a553edaf04ca0f8d3964ceefb1b266f1ebcba74a2781d7daba0a86.png","nickName":"6ce52fc346f14","email":"8dfade06004a4e71a8abd374135257df","bindWx":false,"company":false},"searchStr":"CVE-2023-23638","resource":"XVE-2023-4535","resourceName":"Apache Dubbo 反序列化远程代码执行漏洞","resourceType":"vul","summaryInfo":{"count":9,"holeResource":"26c5f6de1694b7e7ece1ab498631a75f8e10f823b29633004ffa3fd526297d3936f76cf0aa03dc41708f1b71574fcbc6","thrType":{"my_code":"1","en":"Remote","zh":"远程"},"solutionsList":[],"solutionsListZh":[{"source":"CNVD,CNNVD","text":"目前厂商已发布升级补丁以修复漏洞，补丁获取链接:\nhttps:\u002F\u002Flists.apache.org\u002Fthread\u002F8h6zscfzj482z512d2v5ft63hdhzm0cb","url":"https:\u002F\u002Flists.apache.org\u002Fthread\u002F8h6zscfzj482z512d2v5ft63hdhzm0cb"}],"id":"XVE-2023-4535","cve_id":"CVE-2023-23638","_cnvd_id":["CNVD-2023-23551"],"_cnnvd_id":["CNNVD-202303-617"],"hole_name":"Apache Dubbo 反序列化远程代码执行漏洞","hole_class":"代码注入","hole_grade":"HIGH","hole_grade_zh":"高危","hole_platform_list":["应用程序"],"hole_publish_time":"2023-03-08","hole_update_time":"2023-10-23","thr_type_zh":"远程","is_solution":true,"is_poc":true,"is_exp":false,"poc_exist":true,"poc_details":[],"exp_exist":false,"tag_groups":[{"classify":"1","tag":["RCE","关键漏洞"]},{"classify":"2","tag":["微步PoC","公开PoC"]},{"classify":"3","tag":["影响范围广泛"]}],"is_rce":true,"is_safeguard":false,"is_oppose":false,"hole_description":"Apache Dubbo是美国阿帕奇（Apache）基金会的一款基于Java的轻量级RPC（远程过程调用）框架。该产品提供了基于接口的远程呼叫、容错和负载平衡以及自动服务注册和发现等功能。Dubbo 2.7.21版本及之前的2.7.x 版本、3.0.13版本及之前的3.0.x版本、3.1.5版本及之前的3.1.x 版本存在代码问题漏洞，该漏洞源于存在反序列化漏洞，可能导致恶意代码执行。\n经过分析与研判，该漏洞可以远程代码执行，建议尽快修复。","affect_vendors":["apache"],"affect_products":["dubbo"],"x_exp_details":[],"reference_info_count":"6","hole_reference_infos":[{"source":"MISC","url":"https:\u002F\u002Flists.apache.org\u002Fthread\u002F8h6zscfzj482z512d2v5ft63hdhzm0cb","text":"https:\u002F\u002Flists.apache.org\u002Fthread\u002F8h6zscfzj482z512d2v5ft63hdhzm0cb"},{"source":"cxsecurity.com","url":"https:\u002F\u002Fcxsecurity.com\u002Fcveshow\u002FCVE-2023-23638\u002F","text":"https:\u002F\u002Fcxsecurity.com\u002Fcveshow\u002FCVE-2023-23638\u002F"},{"source":"奇安信攻防社区","url":"https:\u002F\u002Fforum.butian.net\u002Fshare\u002F2277","text":"Apache Dubbo （CVE-2023-23638）完整利用及工程化实践"},{"source":"先知社区","url":"https:\u002F\u002Fxz.aliyun.com\u002Ft\u002F12333","text":"Apache Dubbo CVE-2023-23638 JavaNative 反序列化漏洞分析"},{"source":"MISC","url":"https:\u002F\u002Fxz.aliyun.com\u002Ft\u002F12396","text":""},{"source":"GitHub","url":"https:\u002F\u002Fgithub.com\u002FYYHYlh\u002FApache-Dubbo-CVE-2023-23638-exp\u002F","text":""}],"status_code":200},"query":{"searchStr":"CVE-2023-23638"}}};</script><script type="text/javascript" src="/public/js/vendor.b8a65747.js"></script><script type="text/javascript" src="/public/js/runtime.00de9a33.js"></script><script type="text/javascript" src="/public/js/chunk/common.8c32f78d.js"></script><script type="text/javascript" src="/public/js/chunk/result/vul.330f09df.js"></script>
         </body>
</html>
    """

    # for html in [html_content, html_content_two]:
    #     format_html = FormatHtmlData()
    #     ret = format_html.extract_vuln_data(html)
    #     print(ret)



    parser = MyHTMLParser('script')
    parser.feed(html_content)
    for item in parser.data:
        start_str = 'window.__INITIAL_STATE__='
        if item and item.startswith(start_str):
            vuln_info = item[len(start_str):]
            vuln_info = vuln_info.strip(';')
            vuln_info = vuln_info.replace('\n', '')
            # vuln_info = eval(vuln_info)
            print(vuln_info)
            pprint.pprint(json.loads(vuln_info))


if __name__ == '__main__':
    html_parser()
    # main()




