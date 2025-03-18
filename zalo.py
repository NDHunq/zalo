from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ACCESS_TOKEN = "lmUHJgJW2r2_2fj8f-y2LRe9cK-lz7iWsbFdISJpFrQ0I_HFsFO7FQ0MxqdwatHMXIgmAS6qL7Ax0hO0-evfTviSbs-6eMOfwJRvJkcz5L2ZMCOOmVWeP8LOiYMRocewvbUYUQcmVG7l29r3iPbn7Ey9kMUicLKPnNwxOO_rV3ZKSgKXp9TrDRCyc7pKtW0-etJSKFJUHZcLEDX0-gKN38D2o6hR-HS_i6tuPkdOPWUWJPLusjPn5xn2b5sy_5avf7cPKzhaKpkKGxXvY_zG7kTxltU6xouTv5-qS_Z2TYoHHPr6oQTk6eiry4FFloyjXmR7JUYpEIkJ9DzUqSy_4OHzvKNcn0eyX4RsT_FtDZJkLkvHYy4Z4Ez3irEkqLuarK6INx_-QnZ1QOb7ZTbcNVfSZZQDt7vwHotJgIsc-WbQ"  # Thay bằng Access Token của bạn

def send_message(user_id, message):
    """Gửi tin nhắn văn bản đến người dùng Zalo"""
    url = "https://openapi.zalo.me/v2.0/oa/message"
    headers = {
        "Content-Type": "application/json",
        "access_token": ACCESS_TOKEN
    }
    data = {
        "recipient": {"user_id": user_id},
        "message": {"text": message}
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if data and "sender" in data and "message" in data:
        user_id = data["sender"]["id"]
        message_text = data["message"]["text"]
        
        # Phản hồi tin nhắn
        reply = f"Bạn vừa gửi: {message_text}"
        send_message(user_id, reply)
    
    return jsonify({"status": "ok"})

@app.route("/", methods=["GET"])
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
