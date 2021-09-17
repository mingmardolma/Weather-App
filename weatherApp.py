from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests
from PIL import ImageTk,Image
import datetime

def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_k = json['main']['temp']
        temp_c = temp_k - 273.15
        temp_f = (temp_k - 273.15)* 9/5 +32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city, country, int(temp_k), int(temp_c), int(temp_f), weather)
        return final
    else:
        return None

def search():
    city = input_city.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        curr_weather_lbl['text'] = weather[5]
        temp_lbl['text'] = '{}°K, {}°C, {}°F'.format(weather[2], weather[3], weather[4])
        
    else:
        messagebox.showerror("Error", "City not found {}".format(city))

#APP
app = Tk()
app.title("Weather App")
app.geometry('700x500')
app.configure(bg="pink")

#getting api key
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
config = ConfigParser()
config.read('config.cfg')
api_key = config.get('api_key', 'key')

#getting images
img = ImageTk.PhotoImage(Image.open('pinkWeather.png'))
panel = Label(app,image=img)
panel.configure(anchor=CENTER)
panel.pack()

#user Entry
input_city = StringVar()
city = Entry(app, textvariable=input_city, bg="white", fg="cadetblue")
city.pack()

#Buttons
search_btn = Button(app, text='Search weather', width=12, command=search)
search_btn.pack()

#Labels
location_lbl = Label(app, font=('bold', 20), bg="pink", fg="cadetblue")
location_lbl.pack()
curr_weather_lbl = Label(app,font=(25), padx=10, pady=2, bg='pink', fg="cadetblue")
curr_weather_lbl.pack()
temp_lbl = Label(app, font=(25), padx=10, pady=2, bg='pink', fg="cadetblue")
temp_lbl.pack()
#display current date and time
now = datetime.datetime.now()
curr_d_t = now.strftime("%Y-%m-%d %H:%M:%S")
curr_d_t_lbl = Label(app, text=curr_d_t, font=(5), padx=20, pady=50, bg='pink', fg="cadetblue")
curr_d_t_lbl.pack()


app.mainloop()
