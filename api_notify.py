import requests
import subprocess
import time

def get_chicken_soup():
    # 这是一个免费的随机毒鸡汤 API
    url = "https://api.oick.cn/dutang/api.php"
    try:
        response = requests.get(url)
        # 直接返回纯文本
        return response.text.strip()
    except Exception as e:
        return "网络连不上，今天就不扎心了。"

print("开始接收毒鸡汤 (按 Ctrl+C 停止)...")

for i in range(5):  # 只弹 5 次，免得你被烦死
    soup = get_chicken_soup()
    
    # 调用 Linux 的弹窗命令！
    # 注意：这里用了 subprocess，相当于在 Python 里敲命令行
    subprocess.run(["notify-send", "来自雷蛇的问候 🐍", soup])
    
    print(f"已弹窗第 {i+1} 次: {soup}")
    time.sleep(5) # 等 5 秒