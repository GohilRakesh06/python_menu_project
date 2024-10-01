import os
import pywhatkit
import smtplib
from twilio.rest import Client
from geopy.geocoders import Nominatim
import geocoder

# Function to open Notepad
def notepad():
    os.system("notepad")

# Function to open Chrome
def chrome():
    os.system("start chrome")

# Function to send a WhatsApp message
def whatsapp():
    pywhatkit.sendwhatmsg_instantly("+919510407509", "Hello World!", wait_time=10, tab_close=True)

# Function to send an email
def email():
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("studytime12science@gmail.com", "pnbl pxsv rufe jiev")
        message = "Message_you_need_to_send"
        s.sendmail("studytime12science@gmail.com", "matlab1694@gmail.com", message)
        s.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error:", e)

# Function to send SMS using Twilio
def sms():
    try:
        account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="Message sent using Python.",
            from_="+17192590683",  # Your Twilio number
            to="+919510407509",   # Receiver's number
        )
        print("SMS sent:", message.body)
    except Exception as e:
        print("Error:", e)

# Function to get the geolocation
def geolocation():
    g = geocoder.ip('me')
    if g.latlng:
        print(f"Your IP-based location is: Latitude: {g.latlng[0]}, Longitude: {g.latlng[1]}")
    else:
        print("Unable to determine location.")

    def get_user_location():
        geolocator = Nominatim(user_agent="location_app")
        user_location = None
        while user_location is None:
            user_input = input("Please enter the location (city, country, etc.): ")
            try:
                user_location = geolocator.geocode(user_input)
                if user_location:
                    print(f"Latitude: {user_location.latitude}, Longitude: {user_location.longitude}")
                else:
                    print("Location not found. Please try again.")
            except Exception as e:
                print("Error occurred:", e)

    get_user_location()

# Function to post on Instagram (use valid credentials)
def instagrampost():
    from instagrapi import Client
    import myauth
    cl = Client()
    cl.login(myauth.username, myauth.password)
    media = cl.photo_upload(path="se.png", caption="Never Give Up")
    print("Instagram post uploaded.")

# Menu to select options
def menu():
    while True:
        print("\n1. Open Notepad")
        print("2. Open Chrome")
        print("3. Send WhatsApp Message")
        print("4. Send Email")
        print("5. Send SMS")
        print("6. Get Geolocation")
        print("7. Post on Instagram")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            notepad()
        elif choice == '2':
            chrome()
        elif choice == '3':
            whatsapp()
        elif choice == '4':
            email()
        elif choice == '5':
            sms()
        elif choice == '6':
            geolocation()
        elif choice == '7':
            instagrampost()
        elif choice == '8':
            print("Exited")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
