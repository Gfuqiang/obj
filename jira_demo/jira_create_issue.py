import tempfile

import pandas as pd
from jira import JIRA


class JiraClient:

    def __init__(self, server, token_auth):
        self.server = server
        self.token_auth = token_auth
        self.client = self.get_client()

    def get_client(self):
        jira = JIRA(
            server=self.server,
            token_auth=self.token_auth
        )
        me = jira.myself()
        jira_project = jira.project("VTAF")
        return jira

    def add_attachment(self):
        jira = self.get_client()
        issue = jira.issue("VTAF-27")
        conditions = {}
        temp_file = self.write_asset_data_to_temp_file(conditions)
        jira.add_attachment(
            issue=issue, attachment=temp_file, filename='资产数据.xlsx'
        )
        temp_file.close()
        print(issue)

    def write_asset_data_to_temp_file(self, conditions):
        """
        assets_data:
            [{"id": 1, "ip": 127.0.0.1},{}]
        """
        assets_data = [{"id": 1, "ip": "127.0.0.1"}]
        es_export_df = pd.DataFrame(assets_data)
        es_export_df.fillna('')
        # need rename column name
        _source = conditions.get('_source', ["id", "ip"])
        if not _source:
            return
        field_map = {}
        df = es_export_df[_source]
        df.rename(columns=field_map)
        temp_f = tempfile.TemporaryFile()
        with pd.ExcelWriter(temp_f) as writer:
            df.to_excel(writer)
        temp_f.seek(0)
        return temp_f


if __name__ == '__main__':
    server = 'http://jira.instra.zhiqiansec.net/'
    token_auth = 'MzY1MjAxMTA1Mzc5Oqq0cXUA6cxeK+acE4MGKGW9RM5F'
    jira_cli = JiraClient(server, token_auth)
    jira_cli.add_attachment()