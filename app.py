from flask import Flask
import requests
import schedule
import time
import threading

app = Flask(__name__)

URLS_TO_PING = [
    "https://pinger-koeh.onrender.com",
    "https://hubsian.onrender.com",
    "https://kyodevor.onrender.com",
    "https://refrigeracaoabel.onrender.com",
  #  "https://pingerbeats.onrender.com",
    "https://sorveteriafiorence1.onrender.com/api/health",
    "https://cachoeira.onrender.com",
   # "https://phdtatto.onrender.com/",
   # "https://maykonrodass.onrender.com/",
    # "https://beckend-ydd1.onrender.com/",
     # "https://painel-mariana-dentista.onrender.com/painel/",
     # "https://painel-mariana-dentista.onrender.com/",
     "https://contabilidade-inteligente-frcy.onrender.com/",
  #  "https://contabilidadefull.onrender.com/api/health",
   # "https://vscodelucas.onrender.com",
  #  "https://lucasdiario.onrender.com",
    "https://seleto.onrender.com",
    #  "https://qg-ironclad.onrender.com",
      "https://lucaslavaeseca.onrender.com",
      "https://lavaesecaerrors.onrender.com",
      "https://lucaszap-bpo0.onrender.com",
      "https://chatvivomad.onrender.com",
      "https://maykonrodasuberlandia.onrender.com",
      "https://maykonrodas.onrender.com",
     "https://siandiver.onrender.com/siandiver",
    "https://kyonfcteste.onrender.com",
    "https://qgkyo.onrender.com",
    "https://sorveteriafiorence1.onrender.com/api/health",
    "https://cachoeira.onrender.com",
   # "https://phdtatto.onrender.com/",
   # "https://maykonrodass.onrender.com/",
    # "https://beckend-ydd1.onrender.com/",
     # "https://painel-mariana-dentista.onrender.com/painel/",
     # "https://painel-mariana-dentista.onrender.com/",
     "https://contabilidade-inteligente-frcy.onrender.com/",
  #  "https://contabilidadefull.onrender.com/api/health",
   # "https://vscodelucas.onrender.com",
  #  "https://lucasdiario.onrender.com",
    "https://seleto.onrender.com",
    #  "https://qg-ironclad.onrender.com",
      "https://lucaslavaeseca.onrender.com",
      "https://lavaesecaerrors.onrender.com",
      "https://lucaszap-bpo0.onrender.com",
      "https://chatvivomad.onrender.com",
      "https://maykonrodasuberlandia.onrender.com",
      "https://maykonrodas.onrender.com",
      "https://genesis-3aqp.onrender.com",
      "https://radinhopiti.onrender.com",
      "https://siandiver-uni.onrender.com"
    
]

last_ping_result = "Aguardando primeiro ping..."

def ping_all_apps():
    global last_ping_result
    results = []
    timestamp = time.ctime()
    for url in URLS_TO_PING:
        try:
            r = requests.get(url, timeout=20)
            results.append(f"✅ {url} — {r.status_code} — {timestamp}")
        except Exception as e:
            results.append(f"❌ {url} — ERRO: {e} — {timestamp}")
    last_ping_result = "\n".join(results)

@app.route("/")
def index():
    rows = "".join(f"<tr><td>{line}</td></tr>" for line in last_ping_result.splitlines())
    return f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="60">
  <title>PingerBeats</title>
  <style>
    body {{ background:#0d0d0d; color:#00ff88; font-family:monospace; padding:2rem; }}
    h1 {{ font-size:1.5rem; margin-bottom:1rem; }}
    table {{ border-collapse:collapse; width:100%; }}
    td {{ padding:0.4rem 0.8rem; border-bottom:1px solid #1a1a1a; }}
    .ts {{ color:#555; font-size:0.8rem; margin-top:1rem; }}
  </style>
</head>
<body>
  <h1>🚀 PingerBeats</h1>
  <table>{rows}</table>
  <p class="ts">Atualiza automaticamente a cada 60s</p>
</body>
</html>"""

@app.route("/ping")
def ping_now():
    ping_all_apps()
    return last_ping_result, 200, {"Content-Type": "text/plain; charset=utf-8"}

def run_schedule():
    ping_all_apps()
    schedule.every(10).minutes.do(ping_all_apps)
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=run_schedule, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
