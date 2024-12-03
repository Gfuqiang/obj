"""
递归例子，递归解析一个data字段
"""


def recursion_input_container(match, ret):
    # 传入容器和数据
    if not (data := match.get('data')):
        ret.append({"field": match.get('field'), 'value': match.get('value')})
        return
    for item in data:
        recursion_input_container(item, ret)
    return ret


def recursion_output_ret(match):
    # 传入数据，返回容器
    ret = []
    # 1.判断不符合条件，直接返回结果
    if not (data := match.get('data')):
        ret.append({"field": match.get('field'), 'value': match.get('value')})
        return ret
    for item in data:
        # 进入递归逻辑，获取递归结果，将结果进行汇总
        ret.extend(recursion_output_ret(item))
    return ret


if __name__ == '__main__':

    match = {
      "data": [
        {
          "field": "device__open_ports.service",
          "group": False,
          "value": "SMB",
          "source": "merge",
          "negation": False,
          "query_type": "value_compare",
          "target_field": "",
          "target_source": "",
          "comparison_operator": "$eq"
        },
        {
          "group": True,
          "logical_operator": "$and",
          "data": [
            {
              "source": "merge",
              "group": False,
              "negation": False,
              "field": "ipv4List",
              "comparison_operator": "$v_empty",
              "value": "",
              "query_type": "value_compare"
            },
            {
              "group": True,
              "logical_operator": "$and",
              "data": [
                {
                  "source": "merge",
                  "group": False,
                  "negation": False,
                  "field": "ipv6List",
                  "comparison_operator": "$eq",
                  "value": "",
                  "query_type": "field_compare",
                  "target_source": "ATI-4077534c39d740ecb524fa82d02f650d",
                  "target_field": "ipv6List"
                }
              ]
            }
          ]
        }
      ],
      "group": True,
      "model_name": "device",
      "logical_operator": "$and"
    }

    ret = []
    # ret = recursion_input_container(match, ret)
    ret = recursion_output_ret(match)
    print(repr(ret))