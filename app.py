from flask import Flask, jsonify, request, render_template_string
import os
import requests

app = Flask(__name__)

# 🔑 ညီလေး၏ Official Telegram Bot အချက်အလက်များ နေရာကွက်တိ ထည့်သွင်းပြီးပါပြီ
TELEGRAM_BOT_TOKEN = "8818379142:AAGfhS5s8TWfoUJ40clinjbAsX_zBWxPwNU"
TELEGRAM_CHAT_ID = "8505831943"

def send_telegram_alert(message):
    try:
        url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
        requests.post(url, json=payload, timeout=5)
    except Exception as e:
        print(f"❌ Telegram Alert Error: {e}")

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
            <div class="card" onclick="loadModule('Users Management', '👤 လက်ရှိအသုံးပြုသူ စာရင်းနှင့် ဒေတာများကို ဤနေရာတွင် ထိန်းချုပ်နိုင်ပါသည်။')"><h3>👥 Users Management</h3></div>
            <div class="card" onclick="loadModule('Security Settings', '🛡️ Firewall ပိတ်ဆို့မှုများနှင့် Zero Trust Rules များ သတ်မှတ်ရန် နေရာ။')"><h3>🛡️ Security Settings</h3></div>
            <div class="card" onclick="loadModule('Analytics', '📈 ဝက်ဘ်ဆိုက် Traffic စာရင်းများကို Live ဖော်ပြပေးနေပါသည်။')"><h3>📈 Analytics</h3></div>
            <div class="card" onclick="triggerKeyGen()"><h3>🔑 License Creator</h3></div>
            <div class="card" onclick="loadModule('System Config', '⚙️ Backend Server Engine ၏ Core Parameters များကို ပြင်ဆင်ရန်။')"><h3>⚙️ System Config</h3></div>
            <div class="card" onclick="loadModule('Telegram Bot', '💬 Real-time Intrusion Alerts စနစ် အသက်ဝင်နေပါသည်။')"><h3>💬 Telegram Bot</h3></div>
        </div>
        <div id="contentBox" class="content-area">
            <h2 id="contentTitle" style="color: #4CAF50; margin-top:0;"></h2>
            <p id="contentText"></p>
        </div>
    </div>
    <div id="toastBox" class="toast"></div>
    <script>
        function loadModule(title, text) {
            document.getElementById("contentBox").style.display = "block";
            document.getElementById("contentTitle").innerText = title;
            document.getElementById("contentText").innerText = text;
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
    </script>
</body>
</html>
"""

@app.route("/admin")
def admin_panel():
    send_telegram_alert("⚠️ *SECURITY ALERT:* Admin Panel ထဲသို့ ဝင်ရောက်မှု ရှိခဲ့ပါသည်။")
    return render_template_string(ADMIN_HTML)

@app.route("/api/create-key", methods=["POST"])
def create_key():
    send_telegram_alert("🔑 *LICENSE ALERT:* VIP Activation Key အသစ်တစ်ခု အောင်မြင်စွာ ထုတ်ယူပြီးပါပြီ။")
    return jsonify({"status": "SUCCESS"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
