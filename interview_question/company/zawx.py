"""
知安网星
"""

"""
1. python垃圾回收中的分代回收
2. redis常用命令
3. csrf:
    csrf 是跨域攻击，浏览器的同源策略是核心最基础的安全策略
    什么是跨域请求？
    协议 + 域名 + 端口都相同就认为是同域，浏览器基于同源策略会对跨区请求做出限制。因为可能被不法分子进行csrf攻击
    如何运行跨域请求？
    1. nginx中配置add_header Access-Control-Allow-Origin *
    django如何防止跨域请求？
    在request请求头中添加csrf token值
"""