import ftplib
import os
from pathlib import Path


class ReefFTP:

    def __init__(self, ip, user, passwd, port=21):
        self.ftp_ip = ip
        self.ftp_user = user
        self.ftp_passwd = passwd
        self.ftp_port = port
        self.ftp = None
        print(f"init ftp parameter")

    def __call__(self, *args, **kwargs):
        ftp = ftplib.FTP()
        # ftp.set_debuglevel(2)
        print(f'start connect ftp')
        # 连接ftp
        ftp_conn_ret = ftp.connect(self.ftp_ip, self.ftp_port, timeout=10)
        print(f'ftp_conn_ret: {ftp_conn_ret}')
        # ftp登录
        ftp_login_ret = ftp.login(self.ftp_user, self.ftp_passwd)
        print(f"ftp_login_ret: {ftp_login_ret}")
        print(ftp.getwelcome())
        self.ftp = ftp
        print('login success')
        return self

    def quit(self):
        self.ftp.quit()

    def ftp_path_exist(self, ftp_path):
        try:
            self.ftp.cwd(ftp_path)
        except Exception as e:
            print(f"ftp path not exist: {e}")
            raise ftplib.error_perm(e)

    def download_file(self, ftp_file_name, local_file_name):
        try:
            file_handle = open(local_file_name, "wb").write  # 以写模式在本地打开文件
            self.ftp.retrbinary("RETR " + ftp_file_name, file_handle)
        except Exception as e:
            raise

    def download_dir_files(self, ftp_path, local_path):
        # check path
        self.ftp_path_exist(ftp_path)
        # 进入指定目录
        self.ftp.cwd(ftp_path)
        # 区分文件和文件夹
        dirs = []
        self.ftp.dir(".", dirs.append)
        file_list = []
        for i in dirs:
            try:
                if '<DIR>' in i:
                    # 目录跳过
                    continue
                else:
                    ftp_file_name = i.split(' ')[-1]
                    if local_path.endswith('/'):
                        local_file_name = local_path + ftp_file_name
                    else:
                        local_file_name = os.path.join(local_path, ftp_file_name)
                    print(f"download file: {local_file_name}")
                    self.download_file(ftp_file_name, local_file_name)
                    file_list.append(local_file_name)
            except Exception as e:
                print(e)

        # 退出当前目录
        self.ftp.cwd("..")
        self.quit()



def conn_ftp():
    '''
     作用：连接ftp服务器
     参数：无
     返回：ftp服务器连接的对象
    '''

    # FTP连接信息
    ftp_ip = "10.80.5.80"
    # 默认端口21
    ftp_port = 21
    # 如果未指定，使用默认用户名为Anonymous，密码为空
    ftp_user = "ftpuser"
    ftp_password = "ftpuser"

    ftp = ftplib.FTP()
    # 连接ftp
    ftp.connect(ftp_ip, ftp_port)
    # ftp登录
    ftp.login(ftp_user, ftp_password)
    # 查看欢迎信息
    # print(ftp.getwelcome())

    return ftp


# ftp = conn_ftp()


def display_dir(ftp, path):
    '''
     作用：进入并展示指定的目录内容
     参数1：ftp连接对象
     参数2：要展示的目录
     返回：无
    '''

    # 进入指定目录
    ftp.cwd(path)
    # 显示当前所在位置
    print("当前所在位置为：")
    print(ftp.pwd())
    # 展示目录内容
    print("\n显示目录内容：")
    dirs = []
    ftp.dir(".", dirs.append)
    for i in dirs:
        if 'd' in i:
            print(f'目录为: {i.split(" ")[-1]}')
        print(i)
    # 展示目录下的文件名，*文件夹和文件都会显示
    print("\n文件和文件夹名为：")
    for i in ftp.nlst():
        print(i)


path = "/data/ftp/data"
# display_dir(ftp, path)


def download_file(ftp, path, local_path):
    '''
     作用: 下载目录
     参数1：ftp连接对象
     参数2：要展示的目录
     参数3：本地存放路径
     返回：无
    '''

    # 进入指定目录
    ftp.cwd(path)
    # 区分文件和文件夹
    dirs = []
    ftp.dir(".", dirs.append)
    for i in dirs:
        try:
            if 'd' in i:
                # 目录跳过
                continue
            else:
                file_name = i.split(' ')[-1]
                local_file_name = local_path + file_name
                print(f"download file: {local_file_name}")
                file_handle = open(local_file_name, "wb").write  # 以写模式在本地打开文件
                ftp.retrbinary("RETR " + file_name, file_handle)
        except Exception as e:
            print(e)

    # 退出当前目录
    ftp.cwd("..")


if __name__ == '__main__':
    # local_path = './ftp/download/'
    # p = Path(local_path)
    # if not p.exists():
    #     print("创建本地目录")
    #     p.mkdir(parents=True)
    # 调用函数
    # download_file(ftp, path, local_path)

    # coolpad conf
    ip = '10.5.11.12'
    user = 'yulong\zengxingming'
    passwd = '1q2w3e4r5t@'
    ftp_path = '/dailybuild-nj/odvb/cp07_project/2022-09-27_3_cp07_r_ta/cp07_user_all_nonta/flash/'
    local_path = '/app/media/coolpad' + ftp_path

    # ip = '10.80.5.80'
    # user = 'ftpuser'
    # passwd = 'ftpuser'
    # ftp_path = '/data/ftp/data'
    # local_path = './ftp/download/' + ftp_path

    # server path
    p = Path(local_path)
    if not p.exists():
        print("创建本地目录")
        p.mkdir(parents=True)
    ftp = ReefFTP(ip, user, passwd)()
    ftp.download_dir_files(ftp_path, local_path)
    # execute scp、
    # coral_ip = '192.168.12.17'
    # coral_ip = '10.5.41.12'
    # ret_val = os.system(f'scp -r {local_path} root@{coral_ip}:/TMach_source/source/rom{ftp_path}')
    # if ret_val != 0:
    #     print(f'scp command error: {ret_val}')
    # else:
    #     print(f'scp success !!!')
