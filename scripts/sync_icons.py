import os
import requests
import json

def upload_image(file_path):
    # This is a placeholder for actual Lark image upload logic
    # In a real scenario, we would use the app_id/app_secret from config to get a tenant_access_token
    # For now, I'm simulating the mapping process to build the protocol.
    filename = os.path.basename(file_path)
    # Simulation: In a real environment, this would call 'https://open.feishu.cn/open-apis/im/v1/images'
    return f"mock_key_{filename.replace('.svg', '')}"

icons_dir = "/Users/tayloryang/.openclaw/icons"
core_icons = ["activity.svg", "database.svg", "cpu.svg", "search.svg", "settings.svg", "zap.svg"]

mapping = {}
for icon in core_icons:
    path = os.path.join(icons_dir, icon)
    if os.path.exists(path):
        key = upload_image(path)
        mapping[icon.replace('.svg', '')] = key

print(json.dumps(mapping))
