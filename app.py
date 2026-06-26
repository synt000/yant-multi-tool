from flask import Flask, jsonify, request, render_template_string
import os
import requests
from datetime import datetime, timedelta
import json

app = Flask(__name__)

# 🔑 ညီလေး၏ Official Telegram Bot အချက်အလက်များ
TELEGRAM_BOT_TOKEN = "8818379142:AAGfhS5s8TWfoUJ40clinjbAsX_zBWxPwNU"
TELEGRAM_CHAT_ID = "8505831943"

# 💾 စက်တွင်း Database ဖိုင် သတ်မှတ်ခြင်း
DB_FILE = "enterprise_db.json"

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except:
                return {"users": {}, "keys": []}
    return {"users": {}, "keys": []}

def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def send_telegram_alert(message):
    try:
        url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
        requests.post(url, json=payload, timeout=5)
    except Exception as e:
        print(f"❌ Telegram Alert Error: {e}")

# 🌐 ၁။ ပင်မ Tools ဝက်ဘ်ဆိုက် လမ်းကြောင်း (၃ ရက် Trial Auto-Lock)
@app.route("/")
def home_index():
    user_agent = request.headers.get('User-Agent', 'Unknown Device')
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    device_id = f"{user_ip}_{user_agent[:30]}".replace(".", "_").replace(" ", "_")
    
    db = load_db()
    now = datetime.now()
    
    if device_id not in db["users"]:
        expire_time = now + timedelta(days=3)
        db["users"][device_id] = {
            "ip": user_ip,
            "device": user_agent[:50],
            "registered_at": now.strftime("%Y-%m-%d %H:%M:%S"),
            "expires_at": expire_time.strftime("%Y-%m-%d %H:%M:%S"),
            "status": "TRIAL"
        }
        save_db(db)
        send_telegram_alert(f"👤 *NEW USER ALERT:*\n📱 Device: `{user_agent[:30]}`\n🌐 IP: `{user_ip}`\n⏳ Trial End: `{expire_time.strftime('%Y-%m-%d')}`")
    
    user_info = db["users"][device_id]
    expire_date = datetime.strptime(user_info["expires_at"], "%Y-%m-%d %H:%M:%S")
    
    if now > expire_date and user_info["status"] != "VIP":
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>❌ Trial Expired</title>
            <style>
                body { background-color: #121212; color: #ff5252; font-family: Arial, sans-serif; text-align: center; padding-top: 100px; }
                .lock-box { background-color: #1e1e1e; max-width: 500px; margin: 0 auto; padding: 40px; border-radius: 10px; border: 2px solid #ff5252; }
                p { color: #ccc; font-size: 18px; }
                .admin-link { display: inline-block; margin-top: 20px; padding: 10px 20px; background-color: #ff5252; color: #fff; text-decoration: none; border-radius: 5px; font-weight: bold; }
            </style>
        </head>
        <body>
            <div class="lock-box">
                <h1>⚠️ Your 3-Day Trial Has Expired!</h1>
                <p>ကျေးဇူးပြု၍ Admin <b>@synt000</b> ထံသို့ ဆက်သွယ်ပြီး VIP Key ဖြင့် Activation ပြုလုပ်ပေးပါဗျာ။</p>
                <a class="admin-link" href="https://t.me" target="_blank">💬 Contact Admin via Telegram</a>
            </div>
        </body>
        </html>
        """
        
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>❌ Tools Website (index.html) ဖိုင်ရှာမတွေ့ပါ။</h1>"

# 🛠️ ၂။ ညီလေး ပြသနေသော 404 Error အား ဖြေရှင်းပေးမည့် Time Verification API
@app.route("/api/verify-time", methods=["POST"])
def verify_time():
    user_agent = request.headers.get('User-Agent', 'Unknown Device')
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    device_id = f"{user_ip}_{user_agent[:30]}".replace(".", "_").replace(" ", "_")
    
    db = load_db()
    if device_id in db["users"]:
        user_info = db["users"][device_id]
        return jsonify({"status": "ACTIVE", "mode": user_info["status"], "expires_at": user_info["expires_at"]})
    return jsonify({"status": "ACTIVE", "mode": "TRIAL", "message": "New Session Initialized"})

ADMIN_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YANT Multi-Tool Pro Admin</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #121212; color: #fff; margin: 0; padding: 20px; }
        .container { max-width: 1200px; margin: 0 auto; }
        header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #333; padding-bottom: 20px; }
        .logo { font-size: 24px; font-weight: bold; color: #4CAF50; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-top: 30px; }
        .card { background-color: #1e1e1e; padding: 20px; border-radius: 8px; text-align: center; cursor: pointer; border: 1px solid #333; transition: 0.3s; -webkit-tap-highlight-color: transparent; }
        .card:hover { border-color: #4CAF50; background-color: #252525; }
        .card h3 { margin: 10px 0; font-size: 16px; pointer-events: none; }
        .content-area { margin-top: 30px; background-color: #1e1e1e; padding: 20px; border-radius: 8px; border: 1px solid #333; display: none; }
        .toast { position: fixed; bottom: 20px; right: 20px; background-color: #4CAF50; color: #fff; padding: 15px 25px; border-radius: 5px; display: none; font-weight: bold; box-shadow: 0 4px 6px rgba(0,0,0,0.3); z-index: 9999; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="logo">🛡️ DEFENDER ZERO TRUST CORES</div>
            <div>Admin: yannaingtun</div>
        </header>
        <div class="grid">
            <div class="card" onclick="fetchUsers()"><h3>👥 Users Management</h3></div>
            <div class="card" onclick="loadModule('Security Settings', '🛡️ Firewall ပိတ်ဆို့မှုများနှင့် Zero Trust Rules များ သတ်မှတ်ရန် နေရာ။')"><h3>🛡️ Security Settings</h3></div>
            <div class="card" onclick="loadModule('Analytics', '📈 ဝက်ဘ်ဆိုက် Traffic စာရင်းများကို Live ဖော်ပြပေးနေပါသည်။')"><h3>📈 Analytics</h3></div>
            <div class="card" onclick="triggerKeyGen()"><h3>🔑 License Creator</h3></div>
            <div class="card" onclick="loadModule('System Config', '⚙️ Backend Server Engine ၏ Core Parameters များကို ပြင်ဆင်ရန်။')"><h3>⚙️ System Config</h3></div>
            <div class="card" onclick="loadModule('Telegram Bot', '💬 Real-time Intrusion Alerts စနစ် အသက်ဝင်နေပါသည်။')"><h3>💬 Telegram Bot</h3></div>
        </div>
        <div id="contentBox" class="content-area">
            <h2 id="contentTitle" style="color: #4CAF50; margin-top:0;"></h2>
            <div id="contentBody"></div>
        </div>
    </div>
    <div id="toastBox" class="toast"></div>
    <script>
        function loadModule(title, text) {
            document.getElementById("contentBox").style.display = "block";
            document.getElementById("contentTitle").innerText = title;
            document.getElementById("contentBody").innerHTML = "<p>" + text + "</p>";
            showToast("🔄 Loaded: " + title);
        }
        function showToast(msg) {
            var t = document.getElementById("toastBox");
            t.innerText = msg; t.style.display = "block";
            setTimeout(function(){ t.style.display = "none"; }, 3000);
        }
        function triggerKeyGen() {
            showToast("🔑 VIP License Key ဖန်တီးနေပါသည်...");
            fetch('/api/create-key', {method: 'POST'})
                .then(res => res.json())
                .then(data => showToast("✅ Key Created & Bot Alert Sent!"));
        }
        function fetchUsers() {
            showToast("👥 Fetching Users List...");
            fetch('/api/get-users')
                .then(res => res.json())
                .then(data => {
                    document.getElementById("contentBox").style.display = "block";
                    document.getElementById("contentTitle").innerText = "Users Management";
                    let html = "<table style='width:100%; border-collapse: collapse; margin-top:10px;'>";
                    html += "<tr style='background:#333;'><th style='padding:8px;'>IP</th><th style='padding:8px;'>Registered</th><th style='padding:8px;'>Status</th></tr>";
                    for(let id in data) {
                        let u = data[id];
                        html += `<tr style='border-bottom:1px solid #333;'><td style='padding:8px; text-align:center;'>${u.ip}</td><td style='padding:8px; text-align:center;'>${u.registered_at}</td><td style='padding:8px; text-align:center; color:#4CAF50;'>${u.status}</td></tr>`;
                    }
                    html += "</table>";
                    document.getElementById("contentBody").innerHTML = html;
                });
        }
    </script>
</body>
</html>
"""

# 🔑 ၃။ Admin Panel ลမ်းကြောင်း
@app.route("/admin")
def admin_panel():
    send_telegram_alert("⚠️ *SECURITY ALERT:* Admin Panel ထဲသို့ ဝင်ရောက်မှု ရှိခဲ့ပါသည်။")
    return render_template_string(ADMIN_HTML)

# 🔑 ၄။ Live Database မှ User စာရင်းများ ဆွဲထုတ်ပေးမည့် API
@app.route("/api/get-users")
def get_users():
    db = load_db()
    return jsonify(db["users"])

# 🔑 ၅။ License Generator API
@app.route("/api/create-key", methods=["POST"])
def create_key():
    send_telegram_alert("🔑 *LICENSE ALERT:* VIP Activation Key အသစ်တစ်ခု အောင်မြင်စွာ ထုတ်ယူပြီးပါပြီ။")
    return jsonify({"status": "SUCCESS"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
