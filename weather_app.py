import requests
from tkinter import *

def get_weather():
    city = city_entry.get().strip()
    if not city:
        result_label.config(text="⚠️ Please enter a city name!")
        return

    api_key = "your_api_key"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        print("STATUS CODE:", response.status_code)
        print("RESPONSE TEXT:", response.text)

        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind = data['wind']['speed']
            output = (
                f"🌡 Temp: {temp}°C\n"
                f"🌥 Weather: {desc.title()}\n"
                f"💧 Humidity: {humidity}%\n"
                f"💨 Wind: {wind} m/s"
            )
        elif response.status_code == 401:
            output = "❌ Invalid API key!"
        elif response.status_code == 404:
            output = f"❌ City '{city}' not found!"
        else:
            output = "⚠️ Unexpected error occurred!"
    except Exception as e:
        output = f"⚠️ Error: {str(e)}"

    result_label.config(text=output)

# GUI setup
root = Tk()
root.title("Live Weather App 🌦️")
root.geometry("300x250")
root.configure(bg="#e0f7fa")

Label(root, text="Enter City Name", font=("Poppins", 14, "bold"), bg="#e0f7fa").pack(pady=10)

city_entry = Entry(root, width=25, font=("Poppins", 12))
city_entry.pack()

Button(root, text="Get Weather", command=get_weather,
       font=("Poppins", 12), bg="#4fc3f7", fg="white").pack(pady=10)

result_label = Label(root, text="", font=("Poppins", 12), bg="#e0f7fa", justify=LEFT)
result_label.pack()

root.mainloop()
