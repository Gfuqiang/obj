import base64
import json

from gmssl import sm3, func
from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT

key = b'3l5butlj26hvv313'
value = json.dumps({"a": 1}).encode('utf-8') #  bytes类型
iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' #  bytes类型
crypt_sm4 = CryptSM4()


def test_sm4():

    # 设置key
    crypt_sm4.set_key(key, SM4_ENCRYPT)
    # 对value进行加密， 加密内容可能不适合传输，可以转为base64进行传输。
    encrypt_value = crypt_sm4.crypt_ecb(value)  # bytes类型
    print(encrypt_value)

    # base64 编解码
    base64_code = base64.b64encode(encrypt_value)
    print(base64_code)
    base64_decode = base64_code.decode()
    print(base64_decode)
    print(f'encode utf-8: {base64_decode.encode("utf-8")}')
    print(f'decode utf-8: {base64.b64decode(base64_decode.encode("utf-8"))}')


    # 解析不同编码
    # encrypt_value = encrypt_value.decode('TIS-620')
    # print(encrypt_value)
    # encrypt_value = encrypt_value.encode('TIS-620')
    # print(encrypt_value)
    # print(int.from_bytes(encrypt_value, 'little'))

    crypt_sm4.set_key(key, SM4_DECRYPT)
    decrypt_value = crypt_sm4.crypt_ecb(encrypt_value)  # bytes类型
    print(decrypt_value.decode())
    assert value == decrypt_value


def test_sm3():
    y = sm3.sm3_hash(func.bytes_to_list(b"Abc123***"))
    print(y)


if __name__ == '__main__':
    test_sm4()


