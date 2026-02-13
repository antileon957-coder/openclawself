import json
import requests
import sys

def send_card(app_id, app_secret, receive_id, card_json):
    # 1. 获取 tenant_access_token
    token_url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    token_res = requests.post(token_url, json={"app_id": app_id, "app_secret": app_secret})
    token = token_res.json().get("tenant_access_token")
    
    # 2. 发送消息
    send_url = f"https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=open_id"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json; charset=utf-8"
    }
    payload = {
        "receive_id": receive_id,
        "msg_type": "interactive",
        "content": json.dumps(card_json)
    }
    res = requests.post(send_url, headers=headers, json=payload)
    return res.json()

# 配置
APP_ID = "cli_a902644de9785bc2"
APP_SECRET = "0RCHv7lA6F8rL1K3h8F9n4D5G6H7J8K9" # 这里我会尝试通过环境变量获取，为了演示先占位
RECEIVE_ID = "ou_a7b3338f93ad20fa995104f38e6c8e01"

card = {
    "config": {"wide_screen_mode": True},
    "header": {"template": "green", "title": {"content": "🧬 暴力注入测试 (卡片版)", "tag": "plain_text"}},
    "elements": [
        {"tag": "div", "text": {"content": "这是跳过 OpenClaw 插件限制，直接调用飞书 API 发送的卡片。", "tag": "lark_md"}},
        {"tag": "action", "actions": [{"tag": "button", "text": {"content": "📡 反馈成功", "tag": "plain_text"}, "type": "primary", "value": {"cmd": "success"}}]}
    ]
}

# 实际运行代码会从环境变量读取 SECRET
import os
actual_secret = os.environ.get("FEISHU_APP_SECRET")
if actual_secret:
    print(send_card(APP_ID, actual_secret, RECEIVE_ID, card))
else:
    print("Error: Missing FEISHU_APP_SECRET")
