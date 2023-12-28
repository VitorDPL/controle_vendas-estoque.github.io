from tkinter import *
from tkinter import ttk

app= Tk()
app.title("Tipos")

def imprimirEsporte():
    ve= cb_esportes.get()
    print(ve)

tipo_peca= [
    'Short Jeans',
    'Short Bengaline',
    'Short Alfaiataria',
    'Calça Jeans',
    'Short Jogger',
    'Calça Bengaline',
    'Calça Jogger',
    'Vestido Curto',
    'Vestido Médio', 
    'Vestido Longo',
    'Macaquinho', 
    'Macacão',
    'Saída de praia',
    'Conjunto',
    'Cropped',
]

lb_esportes= Label(app, text= "Esportes")
lb_esportes.grid()

cb_esportes= ttk.Combobox(app, values= tipo_peca)
cb_esportes.grid()

btn_esporte = Button(app, text="Esporte selecionado", command= imprimirEsporte)
btn_esporte.grid()

app.mainloop()