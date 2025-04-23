from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler
import os
import pytz  # 👉 Thêm dòng này

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

bot = Bot(token=BOT_TOKEN)
# 👉 Chỉ định múi giờ Việt Nam
scheduler = BlockingScheduler(timezone=pytz.timezone("Asia/Ho_Chi_Minh"))

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
