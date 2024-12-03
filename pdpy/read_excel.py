import pandas as pd
import pathlib

if __name__ == '__main__':
    # ExcelTemplateName = '网络关系模版.xlsx'
    # excel_file = pathlib.Path(__file__).resolve().parent.joinpath(ExcelTemplateName)
    # df = pd.read_excel(excel_file, sheet_name=None)
    # # print(list(df.get('NAT OR Load Balancer').columns))
    # # print(type(df.get('NAT OR Load Balancer').iloc[0]))
    # # print(df.get('NAT OR Load Balancer').iloc[0])
    # print(df.get('WAF').columns.tolist())
    # # print(df.get('NAT OR Load Balancer').iloc[1])

    import pandas as pd

    # 创建示例 DataFrame
    data = {'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35]}
    df = pd.DataFrame(data)

    # 显示原始 DataFrame
    print("原始 DataFrame:")
    print(df)

    # 删除索引列
    # df = df.drop(columns='index')

    # 显示删除索引列后的 DataFrame
    print("\n删除索引列后的 DataFrame:")
    print(df)

    for index, data in df.iterrows():
        print(index)
        print(dict(data))
