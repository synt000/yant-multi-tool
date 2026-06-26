const express=require("express"),bodyParser=require("body-parser"),path=require("path"),fs=require("fs"),app=express();app.use(bodyParser.json());app.use(bodyParser.urlencoded({extended:true}));app.use(express.static(__dirname));app.get("/",(e,r)=>r.sendFile(path.join(__dirname,"index.html")));app.get("/admin",(e,r)=>r.sendFile(path.join(__dirname,"admin.html")));app.get("/pro-panel",(e,r)=>r.sendFile(path.join(__dirname,"dashboard.html")));app.get("/dashboard",(e,r)=>r.sendFile(path.join(__dirname,"dashboard.html")));app.post("/api/admin-login",(e,r)=>{const{username:a,password:t}=e.body;r.json("yannaingtun"===a&&"yant786"===t?{success:true}:{success:false,message:"Password မှားယွင်းနေပါသည်။"})});// 🕒 ၃ ရက်ပြည့်လျှင် စက်ပစ္စည်းအား အလိုအလျောက် Lock ချမည့် SaaS Core API
app.post("/api/verify-time",(req,res)=>{const {deviceId}=req.body;if(!deviceId)return res.json({status:"ERROR"});let db=JSON.parse(fs.readFileSync(path.join(__dirname,"enterprise_db.json"),"utf8"));if(!db.users[deviceId])return res.json({status:"NEW"});const user=db.users[deviceId];if(user.status==="Banned")return res.json({status:"BANNED"});const start=user.created_at;const current=Date.now();const daysPast=Math.floor((current-start)/(1000*60*60*24));const daysLeft=3-daysPast;if(daysLeft<=0){user.status="Expired";fs.writeFileSync(path.join(__dirname,"enterprise_db.json"),JSON.stringify(db,null,2),"utf8");return res.json({status:"EXPIRED",daysLeft:0})}res.json({status:"ACTIVE",daysLeft:daysLeft})});

// 🔔 TELEGRAM BOT REAL-TIME ALERT INFRASTRUCTURE SYSTEM
const TELEGRAM_BOT_TOKEN = "7864219503:AAH_ExampleTokenYOURS";
const TELEGRAM_CHAT_ID = "1234567890";

function sendTelegramAlert(message) {
 const payload = JSON.stringify({ chat_id: TELEGRAM_CHAT_ID, text: message, parse_mode: "HTML" });
 const req = https.request({ hostname: "api.telegram.org", port: 443, path: `/bot${TELEGRAM_BOT_TOKEN}/sendMessage`, method: "POST", headers: { "Content-Type": "application/json", "Content-Length": Buffer.byteLength(payload) } });
 req.write(payload); req.end();
}

// Trigger Alert on Access Check Route Hook
// sendTelegramAlert("⚠️ <b>[SECURITY WARNING]</b>\\nNew Device IP Detected in SaaS System Hub!");

app.listen(8080,()=>console.log("[SUCCESS] Server Active"));
