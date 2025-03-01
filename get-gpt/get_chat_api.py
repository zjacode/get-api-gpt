import requests

# 替换为您的API密钥
API_KEY = ''

# API端点
url = 'https://api.openai.com/v1/chat/completions'

# 请求头
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json',
}

# 请求数据
data = {
    'model': 'gpt-3.5-turbo',
    'messages': [
        {'role': 'user', 'content': '你好！请告诉我今天的天气。'}
    ],
    'temperature': 0.7,
}

# 发送POST请求
response = requests.post(url, headers=headers, json=data)

# 解析响应
if response.status_code == 200:
    completion = response.json()
    print(completion['choices'][0]['message']['content'])
else:
    print(f"请求失败，状态码: {response.status_code}, 响应: {response.text}")
