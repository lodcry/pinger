# pinger

No Render, nas configurações do serviço:
Campo
Valor
Build Command
pip install -r requirements.txt
Start Command
gunicorn app:app --bind 0.0.0.0:10000 --workers 1 --threads 2
