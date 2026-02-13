import os
import shutil
import sys
from datetime import datetime

VAULT_PATH = "/Users/tayloryang/Documents/Obsidian Vault"
TARGET_SUBFOLDER = "小O产出" # 默认子文件夹

def sync_to_obsidian(source, category=None):
    if category:
        dest_dir = os.path.join(VAULT_PATH, category)
    else:
        dest_dir = os.path.join(VAULT_PATH, TARGET_SUBFOLDER)

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Created directory: {dest_dir}")

    if os.path.isfile(source):
        filename = os.path.basename(source)
        dest_path = os.path.join(dest_dir, filename)
        shutil.copy2(source, dest_path)
        print(f"Synced file to: {dest_path}")
        return True
    elif os.path.isdir(source):
        for item in os.listdir(source):
            s = os.path.join(source, item)
            if os.path.isfile(s) and item.endswith(".md"):
                dest_path = os.path.join(dest_dir, item)
                shutil.copy2(s, dest_path)
                print(f"Synced file to: {dest_path}")
        return True
    else:
        print(f"Source not found: {source}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 obsidian_sync.py <source_path> [category]")
        sys.exit(1)
    
    src = sys.argv[1]
    cat = sys.argv[2] if len(sys.argv) > 2 else None
    sync_to_obsidian(src, cat)
