import http.client
import json
conn = http.client.HTTPSConnection("api.collectapi.com")
    
headers = {
    'content-type': "application/json",
    'authorization': "apikey token"
    # Yukarıda token yazan yere kendi tokeninizi giriniz.
    # https://collectapi.com/tr/auth tokene burdan ulaşabilirsiniz
    }
while True:
    sehir=input("""Namaz Vakitleri Uygulamasına Hoşgeldiniz!
Lütfen Şehir Giriniz:
""")
    conn.request("GET", "/pray/all?data.city=" + sehir, headers=headers)

    res = conn.getresponse()
    data = res.read()
    jsonoku = json.loads(data)
    datamiz= jsonoku["result"]
    print(f"""{sehir} Bölgesi Ezan Vakitleri:

    {datamiz[0]["vakit"] + ": "+ str(datamiz[0]["saat"])}
    {datamiz[1]["vakit"] + ": "+ str(datamiz[1]["saat"])}
    {datamiz[2]["vakit"] + ": "+ str(datamiz[2]["saat"])}
    {datamiz[3]["vakit"] + ": "+ str(datamiz[3]["saat"])}
    {datamiz[4]["vakit"] + ": "+ str(datamiz[4]["saat"])}
    {datamiz[5]["vakit"] + ": "+ str(datamiz[5]["saat"])}
    """)
    x=input("""
Programa Devam Etmek İçin [1] Çıkmak İçin [0] Tuşlayınız.
""")
    if x=="1":
        continue
    else:
        print("Çıkış Yapılıyor..")
        break