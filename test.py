#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-19 10:38
# @Desc   : ChatGLM4测试代码
# --------------------------------------------------------
"""
from zhipuai import ZhipuAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ZHIPUAI_API_KEY")

def test_chatglm4():
    # 初始化API客户端
    client = ZhipuAI(api_key=api_key)  # 替换为您的API密钥
    
    # 测试问题列表
    test_questions = [
        "请解释一下量子计算的基本原理",
        "写一个简单的Python函数来计算斐波那契数列",
        "分析一下人工智能对未来就业市场的影响"
    ]
    
    # 进行多轮对话测试
    for question in test_questions:
        try:
            # 发送请求
            response = client.chat.completions.create(
                model="glm-4",  # 使用GLM-4模型
                messages=[
                    {"role": "user", "content": question}
                ],
                temperature=0.7,  # 控制响应的随机性
                max_tokens=8192,  # 最大输出长度
                # top_p=3,          # 控制输出的多样性
                stream=True
            )
            
            # 打印结果
            print("\n问题:", question)
            print("\n回答:", end="")
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    print(chunk.choices[0].delta.content, end="", flush=True)
            print("\n" + "="*50)
            
        except Exception as e:
            print(f"处理问题时出错: {str(e)}")

if __name__ == "__main__":
    test_chatglm4()
