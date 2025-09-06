
## Deployment

Install Ngrox from [Microsoft Store](ms-windows-store://pdp/?ProductId=9mvs1j51gmk6) and complete installation process including their authentication.

Install all dependencies required
```
pip install -r requirements.txt
```

Run the app
```
Python app.py
```

On other terminal, run Ngrox
```
ngrok http 5000
```

Ngrox will give a public HTTPS URL like:
```
https://f8e5def045fa.ngrok-free.app
```

Add /predict route, thus:
```
https://f8e5def045fa.ngrok-free.app/predict
```