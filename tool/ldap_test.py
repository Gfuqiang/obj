import logging
from ldap3 import Server, Connection, ALL, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES
from ldap3_orm import Connection as Connection_orm
from ldap3.utils.conv import escape_filter_chars
def ldap3():
    from ldap3 import Server, Connection, SAFE_SYNC
    user = 'administrator'
    password = '800zhiQIANsec216'

    logger = logging.getLogger("oauth")

    LDAP = {
        "server": "10.33.70.216",
        "port": 389,
        "use_ssl": False,
        "domain": "zhiqian.com",
        "base": "ou=User,dc=zhiqian,dc=com"
    }

    class LdapAdmin(object):
        def __init__(self):
            """
            init
            """
            self.host = LDAP['server']
            self.port = LDAP.get('port', 389)
            self.use_ssl = LDAP.get('use_ssl', False)
            domain_ = LDAP['domain']
            self.domain = domain_
            self.search_filter = "(&(objectCategory=person)(objectclass=user))"
            self.search_base = "CN=Users,DC=zhiqian,DC=com"
            self.search_attributes = [ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES]

        def login(self, username, password):
            """
            登录
            :return:
            """
            server = Server(host=self.host,
                            port=self.port,
                            use_ssl=self.use_ssl,
                            connect_timeout=15,
                            get_info=ALL)

            try:
                conn = Connection(server,
                                  user=f"CN={username},CN=Users,DC=zhiqian,DC=com",
                                  password=password,
                                  receive_timeout=10,
                                  # client_strategy=SAFE_SYNC,
                                  # auto_bind=True
                                  )
                if not conn.bind():
                    print(conn.result)
            except Exception as e:
                err_msg = f'LDAP 认证失败:{e}'
                logger.error(err_msg)
                return False
            else:
                # return conn
                count = 0
                conn.search(
                    "DC=zhiqian,DC=com",
                    '(objectClass=*)',
                    # attributes=['cn']
                    attributes=[ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES],
                    paged_size=3
                )
                # print(conn.statu)
                # print(conn.response)
                # print(conn.result)
                # conn.start_tls()
                count += len(conn.response)
                # print(conn.entries[0].entry_to_json())
                for item in conn.entries:
                    print(item)
                    if "scmdb" in item.name.values:
                        print(item)

                cookie = conn.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
                while cookie:
                    conn.search(
                        "CN=Users,DC=zhiqian,DC=com",
                        '(objectClass=organizationalPerson)',
                        # attributes=['cn']
                        attributes=[ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES],
                        paged_size=30,
                        paged_cookie=cookie
                    )
                    count += len(conn.response)
                    count_num = conn.result['controls']['1.2.840.113556.1.4.319']['value']['size']
                    print(f"数据总条数是: {count_num}")
                    print(f"获取数据条数是: {len(conn.response)}")
                    cookie = conn.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
                    for item in conn.entries:
                        if "scmdb" in item.name.values:
                            # {"department": '部门', "homePhone": "电话", "地址": "l"}
                            # name 用户名
                            print(item.entry_to_json())
                print(f"数据总数是: {count}")
                # print(server.info)

                return True

        def test_generator(self, conn):
            total_entries = 0
            entry_generator = conn.extend.standard.paged_search(search_base=self.search_base,
                                                                search_filter=self.search_filter,
                                                                attributes=self.search_attributes,
                                                                paged_size=5,
                                                                generator=True)
            for entry in entry_generator:
                total_entries += 1
                attributes = entry.get('attributes', {})
                print(f"name: {attributes.get('name')}")
                print(f"mobile: {attributes.get('mobile')}")
            print('Total entries retrieved:', total_entries)

        def test_bind(self):
            # define the server
            s = Server(host=self.host,
                            port=self.port,
                            use_ssl=False,
                            connect_timeout=15,
                            get_info=ALL)
            # define an unsecure LDAP server, requesting info on DSE and schema

            # define the connection
            c = Connection(s)  # define an ANONYMOUS connection

            # perform the Bind operation
            if not c.bind():
                print('error in bind', c.result)
            else:
                print(c.result)
            return c

    ldap_ins = LdapAdmin()
    conn = ldap_ins.login(user, password)
    # conn = ldap_ins.test_bind()
    ldap_ins.test_generator(conn)



def ldap():
    import ldap
    # 1390
    conn = ldap.initialize('ldap://10.33.70.216:389')
    conn.set_option(ldap.OPT_REFERRALS, 0)
    conn.set_option(ldap.OPT_TIMEOUT, 10)
    conn.set_option(ldap.OPT_NETWORK_TIMEOUT, 10)
    conn.protocal_version = ldap.VERSION3
    result = conn.simple_bind_s('administrator', '800zhiQIANsec216')
    print(result)
    print(f'conn: {conn}')


def ldap_orm():
    from ldap3_orm import EntryBase, AttrDef, ALL_ATTRIBUTES

    class User(EntryBase):
        dn = "uid={uid},{base_dn}"
        base_dn = "ou=People,dc=example,dc=com"
        object_classes = ["top", "inetUser", "inetOrgPerson"]

        username = AttrDef("uid")
        password = AttrDef("userPassword")
        fullname = AttrDef("cn")
        givenname = AttrDef("givenName")
        surname = AttrDef("sn")
        email = AttrDef("mail")

    user = 'scmdb'
    password = 'Abc123**'
    with Connection_orm("ldap://10.33.70.216:389", user=user, password=password) as conn:
        conn.bind()
        search_base = "ou=People,dc=example,dc=com"
        conn.search(search_base, User.username == "guest",
                    attributes=ALL_ATTRIBUTES)


if __name__ == '__main__':
    # ldap()
    ldap3()
