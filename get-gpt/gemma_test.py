import requests
import json

# 设置API的URL和要使用的模型
url = ""
model = "gemma2:27b"

# 准备请求数据
payload = {
    "model": model,
    "messages": [
        {
            "role": "user",
            "content": "can you memory?"  # 您的输入消息
        }
    ]
}

# 发送POST请求
response = requests.post(url, json=payload)

# 输出响应文本，以检查内容
print("Raw response text:", response.text)

# 检查响应状态并输出结果
if response.status_code == 200:
    # 逐行解析
    messages = []
    full_response = []  # 用于存储整个响应的内容
    for line in response.text.splitlines():
        if line.strip():  # 仅处理非空行
            try:
                json_message = json.loads(line)
                messages.append(json_message)
                # 获取每条消息的内容并添加到full_response中
                full_response.append(json_message['message']['content'])
            except json.JSONDecodeError as e:
                print("JSON decoding error:", e)

    # 打印完整响应
    complete_message = ''.join(full_response)  # 合并所有响应内容
    print("Complete Response:", complete_message)
else:
    print("Error:", response.status_code, response.text)
