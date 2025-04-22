import json
import pathlib

import pandas as pd


code_list = [
    'CVE-2023-2825', 'CVE-2023-28432', 'CVE-2023-23397', 'CVE-2023-21839', 'CNVD-2023-45001',
    'CVE-2023-33246', 'CVE-2023-27363', 'CVE-2023-31039', 'CVE-2023-38646', 'CVE-2023-20860',
    '暂无', 'CNVD-2023-02709', 'CVE-2022-33891', 'CVE-2022-26134', 'CVE-2022-23131', 'CVE-2022-1388',
    'CNVD-2022-86535', 'CVE-2022-24706', 'CVE-2022-0543', 'CVE-2022-0847', 'CVE-2021-21972', '暂无',
    'CVE-2021-44228', '暂无', 'CVE-2023-32315']

qax_no_match = ['CNVD-2023-02709']


def handle_func():

    vuln_data_list = read_json_file()
    ret_vuln_list = []
    for vuln_data_dict in vuln_data_list:
        ret_data = {}
        data = vuln_data_dict.get('data')
        data = data[0]
        # summaryInfo = data.get('summaryInfo', {})
        ret_data['title'] = data.get('vuln_name_cn', '')
        ret_data['vulnOpenTime'] = data.get('publish_date', '')
        ret_data['vulnUpdateTime'] = data.get('update_time', '')
        ret_data['cveId'] = data.get('cve_id', '')
        # ret_data['vulnType'] = summaryInfo.get('hole_class', '')
        ret_data['cnnvdId'] = data.get('cnnvd_id', '')
        ret_data['cnvdId'] = data.get('cnvd_id', '')
        ret_data['xveId'] = data.get('resource', '')
        cvss = data.get('risk', {}).get('cvss', {})
        ret_data['cvss3'] = str(cvss.get('cvss2').get('base_score', '')) + ' ' + cvss.get('cvss2').get('vector', '')
        ret_data['cvss2'] = str(cvss.get('cvss3').get('base_score', '')) + ' ' + cvss.get('cvss3').get('vector', '')
        ret_data['vuln_description'] = data.get('vuln_description_cn', '')
        # ret_data['timeLine'] =
        ret_data['affect_manufacturers'] = data.get('product_name', '')
        ret_data['products_affected'] = data.get('vendor_name', '')
        ret_data['threat_type'] = ','.join(data.get('threat_category_cn', ''))
        ret_data['technology_type'] = ','.join(data.get('technical_category_cn', ''))
        path_list = [','.join(path.get('official_download_url', '')) for path in data.get('patch', [])]
        ret_data['patch'] = ','.join(path_list) if path_list else ''
        ret_data['time_line'] = '是' if data.get('timeline_info') else '否'
        ret_data['qvdId'] = data.get('qvd_id')
        if cpe := data.get('cpe', []):
            cpe_list = [cpe_match.get('cpe23Uri') for cpe_match in cpe[0].get('cpe_match')]
            cpe = ','.join(cpe_list)
            ret_data['isCPE'] = cpe
        ret_vuln_list.append(ret_data)
    return ret_vuln_list


def read_json_file():
    path = pathlib.Path('vuln_data.json')
    with open(path, 'r') as f:
        vuln_data_list = json.loads(f.read())
    if isinstance(vuln_data_list, list):
        return vuln_data_list
    return []


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
        'overall_rating': '综合评级',
        'vulnOpenTime': '漏洞公开时间',
        'vulnUpdateTime': '漏洞更新时间',
        'cnnvdId': 'CNNVD编号',
        'cnvdId': 'CNVD编号',
        'xveId': 'XVE编号',
        'qvdId': 'QVD漏洞编号',
        'reportId': '报告编号',
        'vuln_type': '漏洞类型',
        'usage_method': '利用方式',
        'vuln_platform': '漏洞平台',
        'affect_manufacturers': '影响厂商',
        'products_affected': '影响产品',
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
        'vuln_description': '漏洞描述',
        'eligibility': '利用条件',
        'interaction_requirements': '交互要求',
        'poc': 'PoC',
        'patch': '补丁列表',
        'reference_information': '参考信息',
        'time_line': '时间线',
        'related_content': '相关内容',
        'detection_rules': '检测规则',
        'isCPE': 'CPE',
        'url': '网址'}
    path = pathlib.Path('./奇安信漏洞数据.xlsx')
    df = pd.DataFrame(vuln_data)
    df.rename(columns=column_mapping, inplace=True)
    df.to_excel(path)


if __name__ == '__main__':
    vuln_list = handle_func()
    if vuln_list:
        write_excel(vuln_list)
    else:
        print('没有获取到漏洞数据')