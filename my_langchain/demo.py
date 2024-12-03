import os
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import BaseOutputParser
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain

API_KEY = 'sk-ac22a7dd286a4697882a33a71a907e10'

def tongyi_qwen():

    os.environ["DASHSCOPE_API_KEY"] = API_KEY
    chatLLM = ChatTongyi(streaming=True)
    content = '给生成袜子的公司起一个有意义的名字'
    res = chatLLM.stream([HumanMessage(content=content)], streaming=True)
    for r in res:
        print("chat resp:", r)


class SplitOutputParser(BaseOutputParser):

    def parse(self, text):
        return text.strip().split(',')


def common_llm():
    chatLLM = ChatTongyi(api_key=API_KEY)
    sys_template = '返回用户输入内容的5个相关对象，并使用逗号连接，仅此而已'
    system_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)
    human_template = "{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    chain = LLMChain(
        llm=chatLLM,
        prompt=chat_prompt,
        output_parser=SplitOutputParser()
    )
    return chain


def main():
    llm = common_llm()
    llm.run('颜色')


if __name__ == '__main__':
    main()