from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import requests

root = tb.Window(themename = "superhero", resizable = [500, 500])
root.title("Weather")
root.geometry('900x600')

#Weather function
def weather(weather_entry):
    api_key = "63382a54a7369e8afacc7fe9fb8804c0"

    weather_web_base = ("http://api.openweathermap.org/data/2.5/weather?")
    weather_final = weather_web_base + "appid=" + api_key + "&q=" + weather_entry
    json_req = requests.get(weather_final) 

    json_req = json_req.json()


    def kel_to_cel(temp):
        result = temp - 273
        return result

    if(json_req['cod'] == "404"):
        my_label.config(text = "Invalid Request", font = ('Helvetica'))

    else:
        temp = json_req['main']['temp']
        temp_final = round(kel_to_cel(temp), 2)
        
        my_label.config(text = f"City: {weather_entry}\nWeather: {json_req['weather'][0]['main']}\nTemperature: {temp_final}C", font = ("Helvetica"))

def send_city():
    weather_entry = my_entry.get()
    weather(weather_entry)

def remove(event):
    my_entry.delete(0, END)

weather_label = tb.Label(root, text = "Weather", font = ("Helvetica", 28))
weather_label.pack(pady=50)


my_entry = tb.Entry(root)
my_entry.insert(0, "Enter a city")
my_entry.pack(pady=50)
my_entry.bind('<FocusIn>', remove)


my_button = tb.Button(root, text = "Click", bootstyle = ('success outline'), takefocus = False, command = send_city)
my_button.pack(pady=20)

my_label = tb.Label(root, text = "")
my_label.pack(pady=20)


root.mainloop()