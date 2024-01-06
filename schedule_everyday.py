import schedule
import time
import subprocess

def job():
    # 在这里执行你的 Python 文件或命令
    print("live_recorder程序开始执行")
    subprocess.run(["python", "live_recorder.py"])

# 设置定时任务，每天的特定时间执行一次
schedule.every().day.at("23:00").do(job)

# 保持程序运行，直到手动停止
while True:
    schedule.run_pending()
    time.sleep(1)
