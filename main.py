from tkinter import *

import tkintermapview


foundation:list=[]
beneficiary:list=[]
worker:list=[]
temporary:list=[]

class temporarys:
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self.coordinates=self.get_coordinates()
        self.marker=map_widget.set_marker(self.coordinates[0],self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
        return [latitude, longitude]

def create_beneficiarys():

    for idx,val in enumerate(temporary):
        temporary[idx].marker.delete()

    temporary.clear()
    u=listbox_lista_obiketow.index(ACTIVE)
    d=foundation[u].name

    for idx,val in enumerate(beneficiary):
        if beneficiary[idx].location2==d:
            val=temporarys(name=beneficiary[idx].name,location=beneficiary[idx].location)
            temporary.append(val)
        beneficiary[idx].marker.delete()
        worker[idx].marker.delete()

    show_beneficiary_temp()
    button_pokaz_szczegoly_obiektu_beneficiary.configure(command=show_beneficiary_temp_details)

def show_beneficiary_temp():
    listbox_lista_beneficiary.delete(0,END)
    listbox_lista_obiektow_worker.delete(0,END)
    for idx,val in enumerate(temporary):
        listbox_lista_beneficiary.insert(idx,f'{idx+1}.{val.name}')

def show_beneficiary_temp_details():
    o=listbox_lista_beneficiary.index(ACTIVE)
    name=temporary[o].name
    location=temporary[o].location

    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text='...')

    map_widget.set_position(temporary[o].coordinates[0],temporary[o].coordinates[1])
    map_widget.set_zoom(17)


def create_workers():
    for idx, val in enumerate(temporary):
        temporary[idx].marker.delete()

    temporary.clear()
    z = listbox_lista_obiketow.index(ACTIVE)
    d = foundation[z].name

    for idx, val in enumerate(worker):
        if worker[idx].location2 == d:
            val = temporarys(name=worker[idx].name, location=worker[idx].location)
            temporary.append(val)
        beneficiary[idx].marker.delete()
        worker[idx].marker.delete()

    show_worker_temp()
    button_pokaz_szczegoly_obiektu_worker.configure(command=show_worker_temp_details)


def show_worker_temp():
    listbox_lista_beneficiary.delete(0, END)
    listbox_lista_obiektow_worker.delete(0, END)
    for idx, val in enumerate(temporary):
        listbox_lista_obiektow_worker.insert(idx, f'{idx + 1}.{val.name}')


def show_worker_temp_details():
    o = listbox_lista_obiektow_worker.index(ACTIVE)
    name = temporary[o].name
    location = temporary[o].location

    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text='...')

    map_widget.set_position(temporary[o].coordinates[0], temporary[o].coordinates[1])
    map_widget.set_zoom(17)

def restore():
    show_beneficiary()
    show_worker()
    for idx,val in enumerate(temporary):
        temporary[idx].marker.delete()

    for idx,val in enumerate(beneficiary):
        beneficiary[idx].coordinates=beneficiary[idx].get_coordinates()
        beneficiary[idx].marker=map_widget.set_marker(beneficiary[idx].coordinates[0],beneficiary[idx].coordinates[1])

    for idx,val in enumerate(worker):
        worker[idx].coordinates=worker[idx].get_coordinates()
        worker[idx].marker=map_widget.set_marker(worker[idx].coordinates[0],worker[idx].coordinates[1])

    button_pokaz_szczegoly_obiektu_worker.configure(command=show_worker_details)
    button_pokaz_szczegoly_obiektu_beneficiary.configure(command=show_beneficiary_details)




class foundations:
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self.coordinates=self.get_coordinates()
        self.marker=map_widget.set_marker(self.coordinates[0],self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
        return [latitude, longitude]

def add_foundation():
    zmienna_imie=entry_name.get()
    zmienna_miejscowosc=entry_location.get()
    user= foundations(name=zmienna_imie, location=zmienna_miejscowosc)
    foundation.append(user)

    entry_name.delete(0,END)
    entry_location2.delete(0,END)
    entry_location.delete(0,END)

    entry_name.focus()

    show_foundation()



def show_foundation():
    listbox_lista_obiketow.delete(0,END)
    for idx,user in enumerate(foundation):
        listbox_lista_obiketow.insert(idx,f'{idx+1}. {user.name}')


def remove_foundation():
    i=listbox_lista_obiketow.index(ACTIVE)
    foundation[i].marker.delete()
    foundation.pop(i)
    show_foundation()

def edit_foundation():
    i=listbox_lista_obiketow.index(ACTIVE)
    name=foundation[i].name
    location=foundation[i].location

    entry_name.insert(0,name)
    entry_location.insert(0,location)

    button_dodaj_fundacje.config(text='zapisz',command=lambda: update_foundation(i))

def update_foundation(i):
    new_name=entry_name.get()
    new_location=entry_location.get()

    foundation[i].name=new_name
    foundation[i].location=new_location

    foundation[i].marker.delete()
    foundation[i].coordinates=foundation[i].get_coordinates()
    foundation[i].marker=map_widget.set_marker(foundation[i].coordinates[0],foundation[i].coordinates[1])



    entry_name.delete(0,END)
    entry_location.delete(0,END)
    entry_location2.delete(0,END)
    entry_name.focus()


    button_dodaj_fundacje.config(text='Dodaj obiekt',command=add_foundation)
    show_foundation()


def show_foundation_workers():
    i=listbox_lista_obiketow.index(ACTIVE)
    name=foundation[i].name
    location=foundation[i].location
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text='...')
    create_workers()

    map_widget.set_position(foundation[i].coordinates[0],foundation[i].coordinates[1])
    map_widget.set_zoom(17)

def show_foundation_beneficiarys():
    i=listbox_lista_obiketow.index(ACTIVE)
    name=foundation[i].name
    location=foundation[i].location
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text='...')
    create_beneficiarys()

    map_widget.set_position(foundation[i].coordinates[0],foundation[i].coordinates[1])
    map_widget.set_zoom(17)



class beneficiarys():
    def __init__(self, name, location, location2):
        self.name = name
        self.location = location
        self.location2 = location2
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
        return [latitude, longitude]


def add_beneficiary():
    zmienna_imie=entry_name.get()
    zmienna_miejscowosc=entry_location.get()
    zmienna_pochodzenie=entry_location2.get()
    user= beneficiarys(name=zmienna_imie, location=zmienna_miejscowosc, location2=zmienna_pochodzenie)
    beneficiary.append(user)

    entry_name.delete(0,END)
    entry_location2.delete(0,END)
    entry_location.delete(0,END)

    entry_name.focus()

    show_beneficiary()



def show_beneficiary():
    listbox_lista_beneficiary.delete(0,END)
    for idx,user in enumerate(beneficiary):
        listbox_lista_beneficiary.insert(idx,f'{idx+1}. {user.name}')

def remove_beneficiary():
    i=listbox_lista_beneficiary.index(ACTIVE)
    beneficiary[i].marker.delete()
    beneficiary.pop(i)
    show_beneficiary()

def edit_beneficiary():
    i=listbox_lista_beneficiary.index(ACTIVE)
    name=beneficiary[i].name
    location=beneficiary[i].location
    location2=beneficiary[i].location2

    entry_name.insert(0,name)
    entry_location.insert(0,location)
    entry_location2.insert(0,location2)

    button_dodaj_beneficiary.config(text='Zapisz',command=lambda: update_beneficiary(i))

def update_beneficiary(i):
    new_name=entry_name.get()
    new_location=entry_location.get()
    new_location2=entry_location2.get()

    beneficiary[i].name=new_name
    beneficiary[i].location=new_location
    beneficiary[i].location2=new_location2

    beneficiary[i].marker.delete()
    beneficiary[i].coordinates=beneficiary[i].get_coordinates()
    beneficiary[i].marker=map_widget.set_marker(beneficiary[i].coordinates[0],beneficiary[i].coordinates[1])



    entry_name.delete(0,END)
    entry_location.delete(0,END)
    entry_location2.delete(0,END)
    entry_name.focus()


    button_dodaj_beneficiary.config(text='Dodaj obiekt',command=add_beneficiary)
    show_beneficiary()


def show_beneficiary_details():
    i=listbox_lista_beneficiary.index(ACTIVE)
    name=beneficiary[i].name
    location=beneficiary[i].location
    location2=beneficiary[i].location2
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text=location2)

    map_widget.set_position(beneficiary[i].coordinates[0],beneficiary[i].coordinates[1])
    map_widget.set_zoom(17)



class workers():
    def __init__(self, name, location, location2):
        self.name = name
        self.location = location
        self.location2 = location2
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1])

    def get_coordinates(self) -> list:
         import requests
         from bs4 import BeautifulSoup
         url = f"https://pl.wikipedia.org/wiki/{self.location}"
         response = requests.get(url).text
         response_html = BeautifulSoup(response, "html.parser")
         longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
         latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
         print(longitude)
         print(latitude)
         return [latitude, longitude]

def add_worker():
    zmienna_imie=entry_name.get()
    zmienna_miejscowosc=entry_location.get()
    zmienna_pochodzenie=entry_location2.get()
    user= workers(name=zmienna_imie, location=zmienna_miejscowosc, location2=zmienna_pochodzenie)
    worker.append(user)

    entry_name.delete(0,END)
    entry_location2.delete(0,END)
    entry_location.delete(0,END)

    entry_name.focus()

    show_worker()



def show_worker():
    listbox_lista_obiektow_worker.delete(0,END)
    for idx,user in enumerate(worker):
        listbox_lista_obiektow_worker.insert(idx,f'{idx+1}. {user.name}')


def remove_worker():
    i=listbox_lista_obiektow_worker.index(ACTIVE)
    worker[i].marker.delete()
    worker.pop(i)
    show_worker()

def edit_worker():
    i=listbox_lista_obiektow_worker.index(ACTIVE)
    name=worker[i].name
    location=worker[i].location
    location2=worker[i].location2

    entry_name.insert(0,name)
    entry_location.insert(0,location)
    entry_location2.insert(0,location2)

    button_dodaj_worker.config(text='zapisz',command=lambda: update_worker(i))

def update_worker(i):
    new_name=entry_name.get()
    new_location=entry_location.get()
    new_location2=entry_location2.get()

    worker[i].name=new_name
    worker[i].location=new_location
    worker[i].location2=new_location2

    worker[i].marker.delete()
    worker[i].coordinates=worker[i].get_coordinates()
    worker[i].marker=map_widget.set_marker(worker[i].coordinates[0],worker[i].coordinates[1])



    entry_name.delete(0,END)
    entry_location.delete(0,END)
    entry_location2.delete(0,END)
    entry_name.focus()


    button_dodaj_worker.config(text='Dodaj obiekt',command=add_foundation)
    show_foundation()


def show_worker_details():
    i=listbox_lista_obiektow_worker.index(ACTIVE)
    name=worker[i].name
    location=worker[i].location
    location2=worker[i].location2
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_location2_wartosc.config(text=location2)

    map_widget.set_position(worker[i].coordinates[0],worker[i].coordinates[1])
    map_widget.set_zoom(17)





root = Tk()
root.geometry("1200x760")
root.title("projekt pop dk ")


ramka_lista_obiektow=Frame(root)
ramka_formularz=Frame(root)
ramka_szczegoly_obiektow=Frame(root)
ramka_mapa=Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0,columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)

# ramka_lista_obiektow
label_lista_obiektow=Label(ramka_lista_obiektow, text="Lista fundacji")
label_lista_obiektow.grid(row=0, column=0,columnspan=2)
listbox_lista_obiketow=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiketow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly_obiektu=Button(ramka_lista_obiektow, text='Pokaż szczegóły beneficjentów', command=show_foundation_beneficiarys)
button_pokaz_szczegoly_obiektu.grid(row=2, column=0)
button_pokaz_szczegoly_obiektu=Button(ramka_lista_obiektow, text='Pokaż szczegóły pracowników', command=show_foundation_workers)
button_pokaz_szczegoly_obiektu.grid(row=3, column=0)
button_usun_obiekt=Button(ramka_lista_obiektow, text='Usuń obiekt', command=remove_foundation)
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt=Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_foundation)
button_edytuj_obiekt.grid(row=2, column=2)


label_lista_obiektow_beneficiary=Label(ramka_lista_obiektow, text="Lista beneficjentów")
label_lista_obiektow_beneficiary.grid(row=0, column=3,columnspan=2)
listbox_lista_beneficiary=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_beneficiary.grid(row=1, column=3, columnspan=3)
button_pokaz_szczegoly_obiektu_beneficiary=Button(ramka_lista_obiektow, text='Pokaż szczegóły', command=show_beneficiary_details)
button_pokaz_szczegoly_obiektu_beneficiary.grid(row=2, column=3)
button_usun_obiekt_beneficiary=Button(ramka_lista_obiektow, text='Usuń obiekt', command=remove_beneficiary)
button_usun_obiekt_beneficiary.grid(row=2, column=4)
button_edytuj_obiekt_beneficiary=Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_beneficiary)
button_edytuj_obiekt_beneficiary.grid(row=2, column=5)

label_lista_obiektow_worker=Label(ramka_lista_obiektow, text="Lista pracowników")
label_lista_obiektow_worker.grid(row=0, column=6,columnspan=2)
listbox_lista_obiektow_worker=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiektow_worker.grid(row=1, column=6, columnspan=3)
button_pokaz_szczegoly_obiektu_worker=Button(ramka_lista_obiektow, text='Pokaż szczegóły', command=show_worker_details)
button_pokaz_szczegoly_obiektu_worker.grid(row=2, column=6)
button_usun_obiekt_worker=Button(ramka_lista_obiektow, text='Usuń obiekt', command=remove_worker)
button_usun_obiekt_worker.grid(row=2, column=7)
button_edytuj_obiekt_worker=Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_worker)
button_edytuj_obiekt_worker.grid(row=2, column=8)

# ramka_formularz
label_formularz=Label(ramka_formularz, text="Formularz")
label_formularz.grid(row=0, column=0, columnspan=2)
label_name=Label(ramka_formularz, text="Name:")
label_name.grid(row=1, column=0, sticky=W)
label_location=Label(ramka_formularz, text="Miejscowość:")
label_location.grid(row=2, column=0,sticky=W)
label_location2=Label(ramka_formularz, text="Fundacja:")
label_location2.grid(row=3, column=0,sticky=W)

entry_name=Entry(ramka_formularz)
entry_name.grid(row=1, column=1)
entry_location=Entry(ramka_formularz)
entry_location.grid(row=2, column=1)
entry_location2=Entry(ramka_formularz)
entry_location2.grid(row=3, column=1)

button_dodaj_fundacje=Button(ramka_formularz, text='Dodaj fundację',command=add_foundation)
button_dodaj_fundacje.grid(row=5, column=0, columnspan=2)

button_dodaj_beneficiary=Button(ramka_formularz, text='Dodaj beneficjenta',command=add_beneficiary)
button_dodaj_beneficiary.grid(row=6, column=0, columnspan=2)

button_dodaj_worker=Button(ramka_formularz, text='Dodaj pracownika',command=add_worker)
button_dodaj_worker.grid(row=7, column=0, columnspan=2)

button_odswiez=Button(ramka_formularz,text='Odśwież listę',command=restore)
button_odswiez.grid(row=8, column=0, columnspan=2)

# ramka_szczegoly_obiektow
label_szczegoly_obiektow=Label(ramka_szczegoly_obiektow, text="Szczegoly obiektu:")
label_szczegoly_obiektow.grid(row=1, column=0)
label_szczegoly_name=Label(ramka_szczegoly_obiektow, text="Imię:")
label_szczegoly_name.grid(row=1, column=1)
label_szczegoly_name_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_name_wartosc.grid(row=1, column=2)
label_szczegoly_location=Label(ramka_szczegoly_obiektow, text="Miejscowość:")
label_szczegoly_location.grid(row=1, column=3)
label_szczegoly_location_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_location_wartosc.grid(row=1, column=4)
label_szczegoly_location2=Label(ramka_szczegoly_obiektow, text="Fundacja:")
label_szczegoly_location2.grid(row=1, column=5)
label_szczegoly_location2_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_location2_wartosc.grid(row=1, column=6)

# ramka_mapa
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1200, height=500, corner_radius=5)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.set_position(52.23,21.0)
map_widget.set_zoom(6)



root.mainloop()



root.mainloop()



