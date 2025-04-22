import time, base64

import requests
from elasticsearch import Elasticsearch


def get_es_client():
    es = Elasticsearch(
        ['https://10.100.7.1:9200'],
        basic_auth=('elastic', 'JvEDV1igUdZmw5kC'),
        verify_certs=False,
        ssl_show_warn=False
    )
    return es


es_client = get_es_client()


def get_mobile_application_data(page, page_size, title, title_type):
    headers = {
        "Accept": "application/json, text/plain, */*;",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "sessionid=k1baftythwwy2ga6twev5k2pkn93xdlc; csrftoken=keZDemAxiNd6v8eYJ1ssHRrnoV8t9cMsNkjscpPsl2CtJ9fd5tZDjBPQXRpB7p1L",
        "Host": "0.zone",
        "Origin": "https://0.zone",
        "Pragma": "no-cache",
        "sec-ch-ua": """Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99""",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Linux",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "X-CSRFToken": "keZDemAxiNd6v8eYJ1ssHRrnoV8t9cMsNkjscpPsl2CtJ9fd5tZDjBPQXRpB7p1L",
    }

    url = "https://0.zone/api/home/search/"
    session = requests.Session()
    session.headers.update(headers)

    payload = {
        "page": page,
        "pagesize": page_size,
        "title": title,
        "title_type": title_type
    }
    response = session.post(url=url, data=payload)
    time.sleep(1.5)
    if status_code := response.status_code != 200:
        print(f'req status_code is not 200!!!, status_code: {status_code}')
    data_list = response.json().get('data', {}).get('data_list')
    if not data_list:
        print(f"data_list 数据为空")
    return data_list


def add_data_to_es(index_name, data_list, title_type=None):
    if title_type == 'email':
        id_field = 'email'
    else:
        id_field = '_id'
    for data in data_list:
        _id = data.get(id_field, '')
        _id = base64.b64encode(_id.encode('utf-8')).decode()
        _doc = data.get('_source', {})
        _doc.update({"id": _id})
        es_client.index(index=index_name, id=_id, document=_doc)


def get_max_page(data_count, page_size):
    if page_size <= 0:
        print(f'page_size 不能小于等于0')
        return 1
    return data_count//page_size + 1


def get_message_system(title):
    data_count = 100
    page_size = 10
    title_type = 'site'
    index_name = 'assets_message_system_asset'
    max_page = get_max_page(data_count, page_size)
    for page in range(1, max_page):
        data_list = get_mobile_application_data(page, page_size, title, title_type)
        if not data_list:
            break
        add_data_to_es(index_name=index_name, data_list=data_list)
        print(f"【信息系统】获取第{page}页数据，入库成功")


def get_mobile_application(title):
    data_count = 20
    page_size = 10
    title_type = 'apk'
    index_name = 'assets_mobile_application_asset'
    max_page = get_max_page(data_count, page_size)
    for page in range(1, max_page):
        data_list = get_mobile_application_data(page, page_size, title, title_type)
        if not data_list:
            break
        add_data_to_es(index_name=index_name, data_list=data_list)
        print(f"【移动应用】获取第{page}页数据，入库成功")


def get_external_domain_name(title):
    data_count = 20
    page_size = 10
    title_type = 'domain'
    index_name = 'assets_external_domain_name_asset'
    max_page = get_max_page(data_count, page_size)
    for page in range(1, max_page):
        data_list = get_mobile_application_data(page, page_size, title, title_type)
        if not data_list:
            break
        add_data_to_es(index_name=index_name, data_list=data_list)
        print(f"【外部域名】获取第{page}页数据，入库成功")


def get_email(title):
    data_count = 20
    page_size = 10
    title_type = 'email'
    index_name = 'assets_email_asset'
    max_page = get_max_page(data_count, page_size)
    for page in range(1, max_page):
        data_list = get_mobile_application_data(page, page_size, title, title_type)
        if not data_list:
            break
        add_data_to_es(index_name=index_name, data_list=data_list, title_type=title_type)
        print(f"【邮箱】获取第{page}页数据，入库成功")


def get_code_document(title):
    data_count = 20
    page_size = 10
    title_type = 'my_code'
    index_name = 'assets_code_document_asset'
    max_page = get_max_page(data_count, page_size)
    for page in range(1, max_page):
        data_list = get_mobile_application_data(page, page_size, title, title_type)
        if not data_list:
            break
        add_data_to_es(index_name=index_name, data_list=data_list)
        print(f"【代码、文档】获取第{page}页数据，入库成功")


def get_external_employee(title):
    data_count = 20
    page_size = 10
    title_type = 'member'
    index_name = 'assets_external_employee_asset'
    max_page = get_max_page(data_count, page_size)
    for page in range(1, max_page):
        data_list = get_mobile_application_data(page, page_size, title, title_type)
        if not data_list:
            break
        add_data_to_es(index_name=index_name, data_list=data_list)
        print(f"【人员】获取第{page}页数据，入库成功")


if __name__ == '__main__':
    """
    #     "title_type": "site",
    #     "title_type": "apk",
    #     "title_type": "domain",
    #     "title_type": "email",
    #     "title_type": "my_code",
          "title_type": "member",
    """
    # title = '(company==中兴证券)'
    title = '(company==中信证券)||(title==中信证券)||(component==中信证券)||(ssl_info.detail==中信证券)'
    # title = '中信证券'
    # get_message_system(title)
    get_mobile_application(title)
    get_external_employee(title)
    get_external_domain_name(title)
    get_code_document(title)
    get_email(title)



