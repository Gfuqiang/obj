"""
根据job name获取job label，拼接指定格式
"""
import psycopg2
import pandas as pd


def main():
    job_name = ["场景测试_百度", "场景测试_抖音", "场景测试_抖音火山版", "场景测试_抖音极速版", "场景测试_番茄免费小说", "场景测试_和平精英", "场景测试_今日头条", "场景测试_今日头条极速版",
                "场景测试_快手", "场景测试_快手极速版", "场景测试_浏览器", "场景测试_拼多多", "场景测试_七猫免费小说", "场景测试_腾讯视频", "场景测试_王者荣耀", "场景测试_微信",
                "场景测试_西瓜视频", "场景测试_拨号", "场景测试_QQ"]

    job_execute_num = [1, 7, 1, 2, 1, 1, 1, 1, 6, 6, 4, 2, 1, 1, 1, 31, 1, 8, 4]

    job_execute_time = [5, 93, 3, 33, 7, 11, 10, 5, 63, 71, 5, 8, 3, 4, 14, 74, 11, 8, 7]

    if len(job_execute_time) == len(job_execute_num) == len(job_name):
        print("Yes !")

        conn = psycopg2.connect(
            dbname="reef",
            user="postgres",
            password="Hy1Nv9LX",
            host="10.80.15.138",
            port="5432"
        )

        result_list = []
        for index, job in enumerate(job_name):
            sql = f"select job_label from apiv1_job where job_name='{job}'"
            df = pd.read_sql(sql, con=conn)
            line_data = df.iloc[0]
            job_label = line_data.job_label
            result_list.append(
                {"job_label": job_label, "job_name": job, "execute_num": job_execute_num[index], "execute_time": job_execute_time[index]}
            )
        print(result_list)
        # 提交事务
        conn.commit()
        # 关闭连接
        conn.close()


def read_excel():
    df = pd.read_excel('./用户行为模型--交付行为细化.xlsx', sheet_name="Sheet3")
    df = df[0:18]
    print(list(df['运行次数']))


if __name__ == '__main__':
    # read_excel()
    main()

