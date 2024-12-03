# -*- coding:utf-8 -*-
"""
OTP MFA双因子验证
"""

import datetime
import pyotp
from qrcode import QRCode
from qrcode import constants

# 为了方便我用一个固定值测试
# secret_key = pyotp.random_base32()
secret_key = "IVMUUGHFE6XJ7YKX"


def generate_opt(username, issuer_name):
    """
    生成WFA认证二维码
    :param username: 用户名称
    :param issuer_name: 分发者名称
    :return: 生成二维码图片
    """
    totp = pyotp.TOTP(secret_key)
    provisioning_uri = totp.provisioning_uri(
        username
    )
    qr = QRCode(version=1,
                error_correction=constants.ERROR_CORRECT_L,
                box_size=6,
                border=4, )
    qr.add_data(provisioning_uri)
    qr.make(fit=True)
    img = qr.make_image()
    img.save('./OPT_%s.png' % (secret_key))


def check(secret_key, confirmation_code):
    """
    通过 授权令牌 和 验证6位码，验证当前是否匹配
    :param secret_key: 授权令牌
    :param confirmation_code: 验证6位码
    :return: 认证情况
    """
    totp = pyotp.TOTP(secret_key)
    if totp.verify(confirmation_code):
        print('认证通过')
        return True
    else:
        print('认证失败')
        return False


def get_confirmation_code():
    """
    通过令牌直接获取并显示 验证6位码
    :return:
    """
    # 获取 secret_key 对应的一次性密码
    totp = pyotp.TOTP(secret_key)
    print(totp.now())
    return totp.now()
    # print(datetime.datetime.now())


# 注册
generate_opt('Ken', 'Thompson')

# 检验
check(secret_key, "653988")
new_confirmation_code = get_confirmation_code()
check(secret_key, new_confirmation_code)

