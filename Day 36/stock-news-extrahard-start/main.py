import smtplib



MY_EMAIL = "infopythonprojects@gmail.com"
MY_PASSWORD = "ajygnfxsvtldpuea"



name = 1002
while name > 1000:
    with smtplib.SMTP("Smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        contents = f"Money back "
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="servicelivraisonanyvan@gmail.com, onlinewisealerts@gmail.com",
            msg=f"Money Back: Money Back")


# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
