from tkinter import *
import matplotlib.pyplot as plt
import requests
import json

TOKEN = "J97VWFP5ND6U4JAN53HUZRFND"


def pogoda():
    city = entry.get()
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/' \
          f'{city}?unitGroup=metric&key={TOKEN}'
    print(url)
    temp = []
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        data = data['days']
        for i in range(len(data)):
            temp.append(round(data[i]['temp']))
        print(temp)

    try:
        plt.hist(temp, bins=20)
        plt.xlabel("temperatura")
        plt.ylabel("Liczba dni")
        plt.title(f"Temperatura - {entry.get()}")
        plt.show()
    except KeyError:
        temperature_label.config(text="Nie znaleziono danych", background="red")


okno = Tk()

b2 = Button(okno, text="Pokaż histogram", command=pogoda)
entry = Entry(okno)
temperature_label = Label(okno, text="temperatura: ")
temperature_label.pack()
entry.pack()
b2.pack()

okno.geometry("600x600")
okno.mainloop()