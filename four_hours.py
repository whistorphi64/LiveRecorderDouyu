import subprocess
import time
import schedule

def run_live_recorder():
    process = subprocess.Popen(['python', 'live_recorder.py'])  # 启动 live_recorder.py 子进程
    # 设置四小时后结束程序
    schedule.every(4).hours.do(lambda: process.terminate())

# 设置每天在指定时间运行 live_recorder.py
schedule.every().day.at("23:00").do(run_live_recorder)

while True:
    schedule.run_pending()
    time.sleep(1)
