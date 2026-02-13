import os
import time
import json
import sys
import requests

# 获取环境信息
PORT = os.environ.get("OPENCLAW_GATEWAY_PORT", "18789")
TOKEN = os.environ.get("OPENCLAW_GATEWAY_TOKEN")
URL = f"http://localhost:{PORT}"
USER_ID = "ou_a7b3338f93ad20fa995104f38e6c8e01"

def send_message(text):
    headers = {"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}
    payload = {"action": "send", "to": USER_ID, "message": text}
    try:
        requests.post(f"{URL}/api/tool/message", json=payload, headers=headers)
    except Exception: pass

def get_history(session_key):
    headers = {"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}
    params = {"sessionKey": session_key, "limit": 3}
    try:
        resp = requests.get(f"{URL}/api/tool/sessions_history", params=params, headers=headers)
        return resp.json().get("messages", [])
    except: return []

def monitor(session_key, duration=600):
    last_tool_call = ""
    start_time = time.time()
    print(f"Monitoring started for {session_key}")
    while time.time() - start_time < duration:
        messages = get_history(session_key)
        if messages:
            latest = messages[-1]
            for item in latest.get("content", []):
                if item.get("type") == "toolCall":
                    current_call = f"{item.get('name')}: {json.dumps(item.get('arguments'))}"
                    if current_call != last_tool_call:
                        send_message(f"🛠️ [进度通知] 正在执行：{item.get('name')}")
                        last_tool_call = current_call
        time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        monitor(sys.argv[1])
