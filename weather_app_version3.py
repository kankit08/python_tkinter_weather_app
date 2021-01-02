# pylint: disable=wildcard-import
# pylint: disable=W0614

from tkinter import *
import requests
import time
from datetime import datetime

root = Tk()
root.title("Weather App")
root.geometry("1360x780")
root.maxsize(1360, 760)
root.minsize(1360,760)
root.config(bg="#081923")

def getweather(root):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=09fc4480fffb0eb504cd6eab5ee263ce"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = round((json_data['wind']['speed']*3.6),2)
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise']-23400))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset']-23400))
    date_time = datetime.now().strftime("%d %b %Y  %I:%M:%S %p")

    final_info = date_time+"\n" + city.capitalize()+ " Feels Like\n" + condition + "  " + str(temp) + "°C"
                                                     
    max_tp= str(max_temp) + "°C"
    min_tp= str(min_temp) + "°C"
    prs= str(pressure)+"hPa"
    hmd= str(humidity)+"%"
    wd= str(wind)+" km/h"
    srise= str(sunrise) +"AM"
    sset= str(sunset)+"PM"

    label1.config(text=date_time)
    label1.config(text=final_info)
    label_max_t.config(text=max_tp)
    label_min_t.config(text=min_tp)
    label_p.config(text=prs)
    label_h.config(text=hmd)
    label_ws.config(text=wd)
    label_sr.config(text=srise)
    label_st.config(text=sset)

#textfield
textfield = Entry(root, font=("Lora", 50), bg="#DAE0E2", justify='center')
textfield.pack(pady = 70, padx=15)

#To make city name focused, user can type without moving cursor
textfield.focus() 
textfield.bind('<Return>',getweather)


label1 = Label(root, text="--\n", font=("Alegreya Sans", 27),bg="#0875B7",fg="white", justify='center')
label1.place(x=470, y=200, width=500, height=190)

## MAX TEMP
label_max_t = Label(root, text="--", font=("Times new roman", 40, "bold"),bg="#FF3E4D",fg="white")
label_max_t.place(x=60, y=450, width=150, height=150)

label_max_t2 = Label(root, text="Max. Temp", font=("Times new roman", 20, "bold"),bg="#FF3E4D",fg="white")
label_max_t2.place(x=60, y=620, width=150, height=50)

## Min TEMP
label_min_t = Label(root, text="--", font=("Times new roman", 40, "bold"),bg="#EC4849",fg="white")
label_min_t.place(x=220, y=450, width=150, height=150)

label_min_t2 = Label(root, text="Min. Temp", font=("Times new roman", 20, "bold"),bg="#EC4849",fg="white")
label_min_t2.place(x=220, y=620, width=150, height=50)

# ##PRESSURE
label_p = Label(root, text="--", font=("Times new roman", 30, "bold"),bg="#01CBC6",fg="white")
label_p.place(x=380, y=450, width=150, height=150)

label_p2 = Label(root, text="Pressure", font=("Times new roman", 20, "bold"),bg="#01CBC6",fg="white")
label_p2.place(x=380, y=620, width=150, height=50)

# ## HUMIDITY
label_h = Label(root, text="--", font=("Times new roman", 40, "bold"),bg="#2ecc72",fg="white")
label_h.place(x=540, y=450, width=150, height=150)

label_h2 = Label(root, text="Humidity", font=("Times new roman", 20, "bold"),bg="#2ecc72",fg="white")
label_h2.place(x=540, y=620, width=150, height=50)

# ## WIND SPEED
label_ws = Label(root, text="--", font=("Times new roman", 25, "bold"),bg="#019031",fg="white")
label_ws.place(x=700, y=450, width=150, height=150)

label_ws2 = Label(root, text="Wind Speed", font=("Times new roman", 20, "bold"),bg="#019031",fg="white")
label_ws2.place(x=700, y=620, width=150, height=50)

# ## SUNRISE
label_sr = Label(root, text="--", font=("Times new roman", 30, "bold"),bg="#FAD02E",fg="white")
label_sr.place(x=860, y=450, width=240, height=150)

label_sr2 = Label(root, text="Sunrise", font=("Times new roman", 20, "bold"),bg="#FAD02E",fg="white")
label_sr2.place(x=860, y=620, width=240, height=50)

# ## SUNSET
label_st = Label(root, text="--", font=("Times new roman", 30, "bold"),bg="#EA7773",fg="white")
label_st.place(x=1110, y=450, width=230, height=150)

label_st2 = Label(root, text="Sunset", font=("Times new roman", 20, "bold"),bg="#EA7773",fg="white")
label_st2.place(x=1110, y=620, width=230, height=50)

root.mainloop()