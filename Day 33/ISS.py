import requests
from datetime import datetime
import smtplib
import time


MY_LAT = 28
MY_LONG = 50


def is_iss_overhead():
    response_ISS = requests.get(url="http://api.open-notify.org/iss-now.json")

    response_ISS.raise_for_status()
    longitude_ISS = float(response_ISS.json()["iss_position"]["longitude"])
    latitude_ISS = float(response_ISS.json()["iss_position"]["latitude"])
    #if MY_LAT-5 <= latitude_ISS <= MY_LAT+5 and MY_LONG-5 <= longitude_ISS <= MY_LONG+5
        #return True
    print(f"The longitude: {longitude_ISS} and latitude: {latitude_ISS} from the ISS")
is_iss_overhead()
def night():
    parameters = {
        "lat":  MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now >= sunset or time_now <= sunrise:
        return True
#while True:
 #   time.sleep(60)
  #  if is_iss_overhead() and night():
   #     with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
    #        connection.starttls()
     #       connection.login(carloslbnm, MY_PASSWORD)
      #      connection.sendmail(
       #         from_addr=MY_EMAIL,
        #        to_addrs=birthday_person["email"],
         #       msg=f"The ISS is in the SKY!\n\n{contents}"
          #  )