from fastapi import FastAPI, Request
import requests

app = FastAPI()

@app.get("/geolocate")
async def geolocate(request: Request):
    client_ip = request.client.host
    response = requests.get(f"http://ip-api.com/json/{client_ip}")
    return response.json()
