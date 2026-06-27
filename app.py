from flask import Flask, jsonify, request, render_template_string
import os
import requests
from datetime import datetime, timedelta
import json
import random
import string

app = Flask(__name__)

# 🔑 ညီလေး၏ Official Telegram Bot အချက်အလက်များ
TELEGRAM_BOT_TOKEN = "8782790273:AAHNKvYoXxmjM6HRJCSH_fqG_KhZM2F2gjI"
TELEGRAM_CHAT_ID = "8505831943"

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

# 💎 ညီလေး အလိုရှိသော Premium AI Creator Hub UI HTML Code
PREMIUM_HOME_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Creator Hub - Premium All-in-One Platform</title>
    <script src="https://jsdelivr.net"></script>
    <link rel="stylesheet" href="https://cloudflare.com">
    <style>
        body { background-color: #0b0f19; font-family: 'Segoe UI', Roboto, sans-serif; overflow-x: hidden; }
        .glass-nav { background: rgba(11, 15, 25, 0.7); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(255, 255, 255, 0.08); }
        .glass-card { background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.05); transition: all 0.4s ease; }
        .glass-card:hover { border-color: #3b82f6; box-shadow: 0 0 25px rgba(59, 130, 246, 0.2); transform: translateY(-5px); }
        .text-gradient { background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 50%, #ec4899 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .bg-gradient-animate { background: linear-gradient(-45deg, #0b0f19, #1e1b4b, #311042, #0b0f19); background-size: 400% 400%; animation: gradientBG 15s ease infinite; }
        @keyframes gradientBG { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
        .marquee-container { background: linear-gradient(90deg, #3b82f6, #ec4899); color: white; overflow: hidden; white-space: nowrap; box-shadow: 0 4px 15px rgba(236, 72, 153, 0.3); }
        .marquee-text { display: inline-block; padding-left: 100%; animation: marquee 20s linear infinite; font-weight: bold; font-size: 16px; text-transform: uppercase; letter-spacing: 2px; }
        @keyframes marquee { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-100%, 0, 0); } }
        .premium-popup { background: rgba(15, 23, 42, 0.95); backdrop-filter: blur(24px); border: 1px solid rgba(239, 68, 68, 0.3); display: none; }
    </style>
</head>
<body class="bg-gradient-animate text-slate-100 min-h-screen smooth-scroll">

    <!-- Welcome စာတန်းပြေးစနစ် -->
    <div class="marquee-container py-2.5 fixed top-0 w-full z-50">
        <div class="marquee-text">
            🚀 Welcome to AI Creator Hub Pro Toolset v2.0! — Experience Next-Gen Artificial Intelligence Technology — Every New User Receives a FREE 3-Day Premium Trial! ⚡
        </div>
    </div>

    <!-- 1. Sticky Navigation Bar -->
    <nav class="glass-nav fixed top-11 w-full z-40 px-6 py-4 flex justify-between items-center">
        <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-500 to-pink-500 flex items-center justify-center text-white shadow-lg shadow-blue-500/30">
                <i class="fa-solid fa-cubes text-xl animate-pulse"></i>
            </div>
            <span class="text-xl font-black tracking-wider text-white">AI CREATOR <span class="text-blue-500">HUB</span></span>
        </div>
        <div class="hidden md:flex items-center gap-8 font-medium text-slate-300">
            <a href="#" class="hover:text-blue-400 transition">Home</a>
            <a href="#ai-tools" class="hover:text-blue-400 transition">AI Tools</a>
            <a href="#seller-tools" class="hover:text-blue-400 transition">Seller Tools</a>
            <a href="#dev-tools" class="hover:text-blue-400 transition">Developer Tools</a>
            <a href="#existing-tools" class="hover:text-pink-400 transition text-yellow-400 font-bold"><i class="fa-solid fa-wand-magic-sparkles mr-1"></i> Core Tools</a>
        </div>
        <div class="flex items-center gap-4">
            <button onclick="location.href='/admin'" class="bg-slate-800 hover:bg-slate-700 px-4 py-2 rounded-lg font-bold text-sm border border-slate-700 transition">Login</button>
        </div>
    </nav>

    <!-- 2. Hero Section -->
    <section class="pt-40 pb-20 px-6 max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
        <div class="space-y-8">
            <div class="inline-flex items-center gap-2 bg-blue-500/10 border border-blue-500/30 text-blue-400 px-4 py-1.5 rounded-full text-xs font-bold tracking-wide uppercase">
                <i class="fa-solid fa-shield-halved"></i> Powered by Defender Zero Trust
            </div>
            <h1 class="text-5xl md:text-6xl font-black tracking-tight leading-tight text-white">
                The Ultimate <br><span class="text-gradient">AI Creator Hub</span> Platform
            </h1>
            <p class="text-lg text-slate-400 leading-relaxed max-w-xl">
                A modern All-in-One AI Platform specialized for Online Sellers, Content Creators, UI/UX Designers, and Full-Stack Developers. Built for extreme security and performance.
            </p>
            <div class="flex flex-wrap gap-4 pt-2">
                <a href="#existing-tools" class="bg-gradient-to-r from-blue-500 to-pink-500 hover:opacity-90 px-8 py-4 rounded-xl font-bold tracking-wide shadow-xl shadow-blue-500/20 transform hover:-translate-y-1 transition text-center">Get Started Free</a>
            </div>
        </div>
    </section>

    <!-- ⚠️ ညီလေး၏ မူရင်းရှိပြီးသား Core Tools ၄ ခု -->
    <section id="existing-tools" class="py-12 px-6 max-w-7xl mx-auto border-t border-b border-slate-900">
        <div class="text-center space-y-3 mb-12">
            <h2 class="text-3xl font-black text-white tracking-tight"><i class="fa-solid fa-cube text-blue-500 mr-2"></i> YANT Core Multi-Tools</h2>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            <div class="glass-card p-6 rounded-xl text-center space-y-4">
                <div class="text-3xl text-pink-500"><i class="fa-brands fa-tiktok"></i></div>
                <h3 class="font-bold text-lg text-white">TikTok ဒေါင်းလုဒ်</h3>
            </div>
            <div class="glass-card p-6 rounded-xl text-center space-y-4">
                <div class="text-3xl text-blue-500"><i class="fa-brands fa-facebook"></i></div>
                <h3 class="font-bold text-lg text-white">FB ဒေါင်းလုဒ်</h3>
            </div>
            <div class="glass-card p-6 rounded-xl text-center space-y-4">
                <div class="text-3xl text-orange-500"><i class="fa-solid fa-palette"></i></div>
                <h3 class="font-bold text-lg text-white">Logo ပြုလုပ်ရန်</h3>
            </div>
            <div class="glass-card p-6 rounded-xl text-center space-y-4">
                <div class="text-3xl text-yellow-500"><i class="fa-solid fa-key"></i></div>
                <h3 class="font-bold text-lg text-white">Password ထုတ်ရန်</h3>
            </div>
        </div>
    </section>
</body>
</html>
"""

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
        send_telegram_alert(f"👤 *NEW USER COMPILER ALERT:*\n📱 Device: `{user_agent[:30]}`\n🌐 IP: `{user_ip}`\n⏳ Trial End: `{expire_time.strftime('%Y-%m-%d')}`")
    
    user_info = db["users"][device_id]
    expire_date = datetime.strptime(user_info["expires_at"], "%Y-%m-%d %H:%M:%S")
    
    if now > expire_date and user_info["status"] != "VIP":
        return "<h1>⚠️ Your 3-Day Trial Has Expired!</h1>"
        
    return render_template_string(PREMIUM_HOME_HTML)

@app.route("/admin")
def admin_panel():
    return "<h1>Admin Panel Connected!</h1>"

if __name__ == "__main__":
    # ✅ Fix: Render Cloud ၏ Dynamic Environment Port စနစ်အား အော်တိုဖတ်ရှုစေခြင်းဖြင့် လမ်းကြောင်းပိတ်ဆို့မှုအား အပြီးတိုင်ချေမှုန်းခြင်း
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
