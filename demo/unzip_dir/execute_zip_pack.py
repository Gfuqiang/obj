import os, zipfile, requests
from pathlib import Path
from collections import defaultdict


path = Path('.')
path = path / '314'

def get_custom_data():
    result = defaultdict(list)
    for file_name in os.listdir(path):
        zip_file_path = path / file_name
        if os.path.isfile(zip_file_path) and '.zip' in file_name:
            # {zip_file_name: [job_label_list]}
            with zipfile.ZipFile(zip_file_path, 'r') as z:
                job_label_list = []
                # 获取zip包中文件列表
                for zip_info in z.infolist():
                    filename = zip_info.filename
                    if '/' in filename:
                        job_label = filename.split('/')[0]
                        if job_label not in job_label_list:
                            job_label_list.append(job_label)
            result[file_name] = job_label_list
    return result


def pg_read_data(dict_data):
    conn = psycopg2.connect(database="reef", user="postgres", password="Hy1Nv9LX", host="10.80.15.138", port="5432")
    cur = conn.cursor()
    results = defaultdict(list)
    for zip_file_name in dict_data:
        job_label_list = dict_data[zip_file_name]
        # print(f"****one job label: {len(job_label_list)}")
        job_label_list = ["'" + job_label + "'" for job_label in job_label_list]
        job_labels = ",".join(job_label_list)
    #   job_label_list = "'job-0d7b2621-2835-ae4f-ed9f-dc18e7f85e09', 'job-30ab3f65-457e-783e-db56-ca0c72afec50'"
        cur.execute(
            f"""
            select id from apiv1_job where job_label in ({job_labels}) and job_deleted = false 
            """
        )
        rows = cur.fetchall()
        result = [raw[0] for raw in rows]
        # print(f"====two job label: {len(result)}")
        results[zip_file_name] = result
    conn.close()
    return results


def get_zip_pack(dict_data):
    result = {}
    url = "http://10.80.15.138:8000/api/v1/cedar/job_export/"
    for zip_file_name in dict_data:
        body = {"user_id": 2, "job_ids": dict_data[zip_file_name]}
        rep = requests.post(url=url, headers={"Content-Type": "application/json"}, json=body)
        rep = rep.json()
        result[zip_file_name] = rep.get('success')
    return result


def down_zip_pack(dict_data):
    base_dir = Path('.')
    p = base_dir / "zip_file_dir"
    for zip_file_name in dict_data:
        print(f"{zip_file_name} 开始拉取zip包")
        url = f"http://10.80.15.138:8000{dict_data[zip_file_name]}"
        zip_file_path = p / zip_file_name
        rsp = requests.get(url=url)
        with open(zip_file_path, "wb") as f:
            for chunk in rsp.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)


if __name__ == '__main__':
    # 获取job label列表
    # res = get_custom_data()
    # for zip_file_name in res:
    #     print(f"{zip_file_name}-{len(res[zip_file_name])}:{res[zip_file_name]}")

    # 获取job id列表
    # results = pg_read_data(res)
    # for zip_file_name in results:
    #     print(f"{zip_file_name}-{len(results[zip_file_name])}:{results[zip_file_name]}")

    # [6967, 6968, 6969, 6980, 6975, 6982]
    # 生成zip包
    # result = get_zip_pack(results)

    dict_data = {
        'job-export-好看视频-6.zip': '/media/job_export/job-export-2022-04-01-15:57:15-6.zip',
        'job-export-夸克-43.zip': '/media/job_export/job-export-2022-04-01-15:57:59-43.zip',
        'job-export-支付宝-36.zip': '/media/job_export/job-export-2022-04-01-15:58:27-36.zip',
        'job-export-百度-5.zip': '/media/job_export/job-export-2022-04-01-15:58:35-5.zip',
        'job-export-番茄小说-19.zip': '/media/job_export/job-export-2022-04-01-15:58:44-19.zip',
        'job-export-QQ音乐-29.zip': '/media/job_export/job-export-2022-04-01-15:59:02-29.zip',
        'job-export-UC浏览器-23.zip': '/media/job_export/job-export-2022-04-01-15:59:16-23.zip',
        'job-export-腾讯视频-11.zip': '/media/job_export/job-export-2022-04-01-15:59:27-11.zip',
        'job-export-哔哩哔哩-11.zip': '/media/job_export/job-export-2022-04-01-15:59:43-11.zip',
        'job-export-微视-14.zip': '/media/job_export/job-export-2022-04-01-15:59:53-14.zip',
        'job-export-淘宝-27.zip': '/media/job_export/job-export-2022-04-01-16:00:20-27.zip',
        'job-export-虎牙-13.zip': '/media/job_export/job-export-2022-04-01-16:00:36-13.zip'
    }

    # 拉取zip包
    #down_zip_pack(dict_data)





