import requests


response = requests.get("https://reservas.kartodromogranjaviana.com.br/inicio?d=22/04/2022&mes=4")

if "21:30" in response.text:
    requests.post("https://api.telegram.org/bot5245043648:AAEYlV84JtcfVgwy6ZdHfc2c9hVjHTSYobw/sendMessage?chat_id=170292386&text=Corre meu aliado")
