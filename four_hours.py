import time
import sys
import threading
from importlib import import_module
import schedule

def run_main_logic():
    # 导入并执行主体逻辑文件
    main_logic = import_module('live_recorder.py')
    main_logic.run_main_logic()

def time_check():
    # 检查是否已经运行了四个小时
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= 4 * 3600:  # 4小时 = 4 * 60 * 60 秒
            print("程序运行超过四个小时，自动关闭。")
            sys.exit()
        time.sleep(60)  # 每60秒检查一次

def daily_job():
    print("每天定时任务开始")
    # 在这里添加你每天定时需要执行的任务
    run_main_logic()

if __name__ == "__main__":
    # 使用多线程运行主体逻辑、时间检查和定时任务
    main_logic_thread = threading.Thread(target=run_main_logic)
    time_check_thread = threading.Thread(target=time_check)

    main_logic_thread.start()
    time_check_thread.start()

    # 使用 schedule 库添加每天定时任务
    schedule.every().day.at("23:00").do(daily_job)  # 在每天12:00执行任务

    while True:
        schedule.run_pending()
        time.sleep(1)
