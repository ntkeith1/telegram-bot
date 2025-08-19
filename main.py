import requests
import schedule
import time

# ----- THÔNG TIN BOT -----
TOKEN = "7870906217:AAFBm_hBoO5Z3RHj8ddSrJeMVX1fQtSb14k"   # Token bot
CHAT_ID = "7727472656"                                    # Chat ID của cậu

# ----- HÀM GỬI TIN NHẮN -----
def send_message():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": "Chào buổi sáng Gôn! ☀️\nChúc bạn một ngày đầy năng lượng!"
    }
    try:
        requests.post(url, data=payload)
        print("✅ Đã gửi tin nhắn chào buổi sáng")
    except Exception as e:
        print("❌ Lỗi khi gửi tin:", e)

# ----- LẬP LỊCH GỬI HẰNG NGÀY -----
schedule.every().day.at("07:00").do(send_message)   # Giờ VN: 7h sáng

# ----- CHẠY LIÊN TỤC -----
if __name__ == "__main__":
    print("🚀 Bot đã khởi động và đang chờ đến giờ gửi tin nhắn...")
    while True:
        schedule.run_pending()
        time.sleep(30)
# ----- TEST NGAY KHI CHẠY -----
send_message()
