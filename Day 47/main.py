import requests
from bs4 import BeautifulSoup
import smtplib
from datetime import date

MY_EMAIL = 
MY_PASSWORD = 

def price_split(input_price):
    """This function just takes the characters out and converts it in an integer"""
    price_1 = input_price.split("€", 1)
    price_2 = price_1[1].split(',', 1)
    final_price = price_2[0].replace(".","")
    return final_price


website = "https://www.autoscout24.es/anuncios/ds-automobiles-ds-5-2-0bluehdi-sport-eat6-180-" \
          "diesel-blanco-e3062d0e-1277-4bdc-8a41-233df8eb6266?utm_source=web-native-share&utm_campaign=share"

header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
     'Accept-Language': 'en-GB,en;q=0.9,es-ES;q=0.8,es;q=0.7,en-US;q=0.6'}
print(header)

response = requests.get(url=website, headers=header)
bot_response = response.text


soup = BeautifulSoup(bot_response, "html.parser")
soup.prettify()

car_name = soup.find(name="span", class_="StageTitle_boldClassifiedInfo__L7JmO").getText()
product_price = soup.find(name="span", class_="StandardPrice_price__X_zzU")
price_website = product_price.getText()

price_converted = price_split(price_website)
today = date.today()

diccionario = {
     'date': "",
    'price': "" }
target = 15000

if int(price_converted) < target:
    with smtplib.SMTP("Smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        contents = f"The price of the {car_name}is below the target of {target} and is actually {price_converted}" \
                   f""
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: {car_name} Price Alert information!\n\n{contents}")





