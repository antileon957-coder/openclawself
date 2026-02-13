import json
import requests
import os

def send_test_button_card(app_id, app_secret, receive_id):
    # 1. Get token
    token_url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    token_res = requests.post(token_url, json={"app_id": app_id, "app_secret": app_secret})
    token = token_res.json().get("tenant_access_token")
    
    # 2. Send interactive card with reply button
    send_url = "https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=open_id"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json; charset=utf-8"
    }
    
    # Card with a button that triggers a reply back to the bot
    card = {
        "config": {"wide_screen_mode": True},
        "header": {"template": "blue", "title": {"content": "🧬 按钮交互测试", "tag": "plain_text"}},
        "elements": [
            {
                "tag": "div",
                "text": {"content": "点击下方按钮，它会模拟你向我发送一条指令 **“状态自检”**。\n\n如果我立刻回复了系统状态，说明按钮逻辑完全打通！", "tag": "lark_md"}
            },
            {
                "tag": "action",
                "actions": [
                    {
                        "tag": "button",
                        "text": {"content": "🔍 立即触发自检", "tag": "plain_text"},
                        "type": "primary",
                        "value": {"reply": "状态自检"} # Depending on config, this value might be sent back
                    }
                ]
            }
        ]
    }
    
    payload = {
        "receive_id": receive_id,
        "msg_type": "interactive",
        "content": json.dumps(card)
    }
    res = requests.post(send_url, headers=headers, json=payload)
    return res.json()

# Config from env
APP_ID = "cli_a902644de9785bc2"
APP_SECRET = os.environ.get("FEISHU_APP_SECRET")
RECEIVE_ID = "ou_a7b3338f93ad20fa995104f38e6c8e01"

if APP_SECRET:
    print(send_test_button_card(APP_ID, APP_SECRET, RECEIVE_ID))
else:
    print("Error: Missing FEISHU_APP_SECRET")
