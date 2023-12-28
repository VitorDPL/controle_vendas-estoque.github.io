import tkinter as tk
import mysql.connector
from tkinter import ttk
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

conexao= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= '00214023vV#',
    database= 'bd_controle_estoque',
)

cursor= conexao.cursor()

janela= customtkinter.CTk()
janela.title('Controle de Estoque')
janela.geometry("600x600")

janela.rowconfigure([5, 0], weight=1) #Essa linha e a de baixo configuram p as cores acompanharem o esticamento da tela.
janela.columnconfigure([5, 0], weight=1)


#Tipos das peças;
lista_pecas= [
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

#Comands

def buscar():
    # caixa_ref.get('1.0', tk.END)
    # caixa_qtd.get('1.0', tk.END)
    # caixa_tamanho.get('1.0', tk.END)
    # caixa_valor.get('1.0', tk.END)
    tamanho_get= tamanho.get("1.0", tk.END)
    ref_get= ref.get("1.0", tk.END)
    ve= tipo_peca_combo.get()
    # Produto encontrado pela referência
    '''
    Basicamente, na linha abaixo estava ''bugando'', pois o len(tamanho), quando VAZIO, dava UM, e não ZERO. Por isso, significa que quando era colocado
    UM caractere, o tamanho era DOIS.
    '''
    if 2 > len(tamanho_get) and 2 < len(ref_get): #Essa linha tava bugando, por isso foi "2 > len(tamanho).

        cursor.execute(f'SELECT * FROM controle WHERE ref= "{ref.get("1.0", tk.END)}"')
        valores= cursor.fetchall()
        #print(valores)

    elif 2 > len(ref_get) and 2 < len(tamanho_get):
        cursor.execute(f'SELECT * FROM controle WHERE tamanho= "{tamanho.get("1.0", tk.END)}"')
        valores= cursor.fetchall()

    elif 2 > len(ref_get):
        cursor.execute(f'SELECT * FROM controle WHERE tipo_peca= "{ve}"')
        valores= cursor.fetchall()

    else:
        cursor.execute(f'SELECT * FROM controle WHERE ref= "{ref.get("1.0", tk.END)}" AND tamanho= {tamanho_get}')
        valores= cursor.fetchall()
        #print(valores)
    texto = ''
    for id_produto, ref1, tamanho1, quantidade_pecas, valor, tipo_peca in valores:
        texto = texto + (f'----------------------------------\n'
                         f'ID: {id_produto}\n'
                         f'REFERÊNCIA: {ref1}\n'
                         f'TAMANHO: {tamanho1}\n'
                         f'QUANTIDADE: {quantidade_pecas}\n'
                         f'VALOR: R${valor:.2f}\n'
                         f'TIPO DA PEÇA: "{tipo_peca}"\n')
    if len(texto) > 0:
        caixa_resultado.delete("1.0", tk.END)
        caixa_resultado.insert("1.0", f'{texto}')
    else:
        caixa_resultado.delete("1.0", tk.END)
        caixa_resultado.insert("1.0", 'Produto não encontrado.')
def adicionar_peca():

    #Verificando se a referência já está cadastrada no banco de dados antes de executar a venda.
    seleciona_coluna_ref = "SELECT * FROM controle WHERE ref ='{}' AND tamanho='{}'".format(ref.get("1.0", tk.END), tamanho.get("1.0", tk.END))
    cursor.execute(seleciona_coluna_ref)
    resultado = cursor.fetchall() #O resultado é basicamente uma lista de tuplas dizendo o nome das tabelas.
    print(resultado)

    pegar_ref= ref.get("1.0", tk.END)

    ve= tipo_peca_combo.get()


    if len(resultado) == 0:
        try:
            comando= (f'INSERT INTO controle (ref, tamanho, quantidade_pecas, valor, tipo_peca)'
                    f'VALUES ({ref.get("1.0", tk.END)}, {tamanho.get("1.0", tk.END)}, {caixa_qtd.get("1.0", tk.END)}, {caixa_valor.get("1.0", tk.END)}, "{ve}" )')
            cursor.execute(comando)
            conexao.commit()
            texto= ''
            caixa_resultado.delete("1.0", tk.END)
            caixa_resultado.insert("1.0", "Produto adicionado ao banco de dados.")

        except:
            caixa_resultado.delete("1.0", tk.END)
            caixa_resultado.insert("1.0", "Informações incompletas.")

    #impedindo o usuário de adicionar uma peça já existente.

    else:
        try:
            quantidade_atualizada= caixa_qtd.get("1.0", tk.END)
            comando= (f'UPDATE controle SET quantidade_pecas = quantidade_pecas + {quantidade_atualizada} WHERE ref= {ref.get("1.0", tk.END)} '
                    f'AND tamanho= {tamanho.get("1.0", tk.END)}')
            cursor.execute(comando)
            conexao.commit()
            for item in resultado:
                #print(item)
                soma= int(item[3]) + int(caixa_qtd.get("1.0", tk.END))
                #print(soma)

            caixa_resultado.delete("1.0", tk.END)
            caixa_resultado.insert("1.0", f"Produto já existente em nosso banco de dados. A quantidade foi alterada para [{soma}].")

        except:
            caixa_resultado.delete("1.0", tk.END)
            caixa_resultado.insert("1.0", "Erro ao finalizar venda. \n"
                                        "Faltam informações. Para realizar a venda, precisa-se das seguintes informações: \n"
                                        "[Referência], [Quantidade] e [Tamanho] ")


def alterar_produto():
    try:
        quantidade_vendida= caixa_qtd.get("1.0", tk.END)
        comando= (f'UPDATE controle SET quantidade_pecas = quantidade_pecas - {quantidade_vendida} WHERE ref= {ref.get("1.0", tk.END)} '
                  f'AND tamanho= {tamanho.get("1.0", tk.END)}')
        cursor.execute(comando)
        conexao.commit()
        caixa_resultado.delete("1.0", tk.END)
        caixa_resultado.insert("1.0", f"{quantidade_vendida} iten(s) deletado(s) com sucesso.")
    except:
        caixa_resultado.delete("1.0", tk.END)
        caixa_resultado.insert("1.0", "Erro ao finalizar venda. \n"
                                      "Faltam informações. Para realizar a venda, precisa-se das seguintes informações: \n"
                                      "[Referência], [Quantidade] e [Tamanho] ")

def deletar_peca():
    tamanho_get_delet = tamanho.get("1.0", tk.END)
    ref_get= ref.get("1.0", tk.END)
    try:
        if len(ref_get) < 2:
            caixa_resultado.delete("1.0", tk.END)
            caixa_resultado.insert("1.0", "Referência inválida.")
        elif len(tamanho_get_delet) < 2:
            comando= (f'DELETE FROM controle WHERE ref= "{ref_get}"')
            caixa_resultado.delete("1.0", tk.END)
            caixa_resultado.insert("1.0", f"Produto deletado com sucesso do banco de dados.")
            cursor.execute(comando)
            conexao.commit()
        else:
            comando= (f'DELETE FROM controle WHERE ref= "{ref_get}" AND tamanho= "{tamanho_get_delet}"')
            caixa_resultado.delete("1.0", tk.END)
            caixa_resultado.insert("1.0", f"Produto deletado com sucesso do banco de dados.")
            cursor.execute(comando)
            conexao.commit()
    except:
        caixa_resultado.delete("1.0", tk.END)
        caixa_resultado.insert("Erro !", tk.END)


#----------------Layout--------------------
        

mensagem= customtkinter.CTkLabel(janela, text='Controle de Estoque')
mensagem.grid(row=0, column= 0, sticky= 'nswe', columnspan= 6)

tipo_peca_combo_txt= customtkinter.CTkLabel(janela, text= "Tipo da peça")
tipo_peca_combo_txt.grid(row=1, column= 2, padx= 10, pady=5, sticky= 'nswe', columnspan= 1)
tipo_peca_combo= customtkinter.CTkComboBox(janela, values= lista_pecas)
tipo_peca_combo.grid(row=2, column= 2, padx= 10, pady=5, sticky= 'nswe', columnspan= 1)

c_ref= customtkinter.CTkLabel(janela, text='Referência')
c_ref.grid(row=3, column= 0, padx= 20, pady=10, sticky= 'nswe', columnspan= 2)
ref= customtkinter.CTkTextbox(janela, width= 100, height= 1)
ref.grid(row= 4, column= 0, columnspan= 2)

qtd= customtkinter.CTkLabel(janela, text='Quantidade')
qtd.grid(row=3, column= 3, padx= 20, pady=10, sticky= 'nswe', columnspan= 1)
caixa_qtd= customtkinter.CTkTextbox(janela, width= 100, height= 1)
caixa_qtd.grid(row= 4, column= 3, columnspan= 1)

tamanho= customtkinter.CTkLabel(janela, text='Numeração')
tamanho.grid(row= 5, column= 0, padx=20, pady=10, sticky= 'nswe', columnspan= 2)
tamanho= customtkinter.CTkTextbox(janela, width= 100, height= 1)
tamanho.grid(row=6, column= 0, columnspan= 2)

valor= customtkinter.CTkLabel(janela, text='Valor')
valor.grid(row= 5, column= 3, padx=20, pady= 10, sticky='nswe', columnspan= 1)
caixa_valor= customtkinter.CTkTextbox(janela, width= 100, height= 1)
caixa_valor.grid(row= 6, column= 3, columnspan= 1)

mensagem2= customtkinter.CTkLabel(janela, text='Insira a ação que deseja tomar')
mensagem2.grid(row=7, column= 1, sticky= 'nswe', pady=10, columnspan= 6)

#----------------Botões--------------------

buscar_botao= customtkinter.CTkButton(janela, text='Buscar Peça(s)', command= buscar)
buscar_botao.grid(row= 9, column= 1, padx=20, pady=10, sticky= 'nswe')

adicionar_peca= customtkinter.CTkButton(janela, text= 'Adicionar Peça', command= adicionar_peca)
adicionar_peca.grid(row= 8, column= 1, padx=20, pady=10, sticky= 'nswe')

deletar_peca= customtkinter.CTkButton(janela, text= 'Deletar Peça', command= deletar_peca)
deletar_peca.grid(row=8, column= 3, padx=20, pady=10, sticky= 'nswe')

fazer_venda= customtkinter.CTkButton(janela, text= 'Remover X Peças', command= alterar_produto)
fazer_venda.grid(row=9, column= 3, padx=20, pady=10, sticky= 'nswe')



#----------------Caixa Resultado--------------------

caixa_resultado= tk.Text(width= 50, height= 10)
caixa_resultado.grid(row= 11, column=1, columnspan= 3, padx=20, pady=(20, 70), sticky= 'nswe')




janela.mainloop()

cursor.close()
conexao.close()