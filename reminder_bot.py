from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import time
import os

BOT_TOKEN = os.getenv("7454315114:AAGC5qF8xN0ElDb32jJTv4l7zWAojUXvtoY
")
CHAT_ID = int(os.getenv("-4709648795"))

bot = Bot(token=BOT_TOKEN)
scheduler = BlockingScheduler()

def send_reminder():
    message = (
        "📦 Bộ phận kho kiểm tra đơn bất thường trước khi xác nhận và in tem,\n\n"
        "Đơn bất thường là:\n"
        "- Đơn có nhiều sản phẩm trùng nhau\n"
        "- Đơn giá trị cao trên 500k"
    )
    bot.send_message(chat_id=CHAT_ID, text=message)

scheduler.add_job(send_reminder, 'cron', hour=8, minute=10)
print("Bot đang chạy. Nhắc việc sẽ gửi lúc 8h10 mỗi ngày.")
scheduler.start()
