import tkinter as tk
from tkinter import ttk
import mysql.connector
from datetime import datetime
from pandas_analise import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#----------------Conexão Vendas--------------------
conexao_vendas= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= '00214023vV#',
    database= 'vendas_fix',
)

cursor_vendas = conexao_vendas.cursor()

#----------------Conexão Estoque--------------------
conexao_estoque= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= '00214023vV#',
    database= 'bd_controle_estoque',
)

cursor_estoque= conexao_estoque.cursor()
#----------------Janela TK--------------------
janela= customtkinter.CTk()
janela.title('Controle de Vendas')
janela.geometry("600x600")

janela.rowconfigure([5, 0], weight=1) #Essa linha e a de baixo configuram p as cores acompanharem o esticamento da tela.
janela.columnconfigure([5, 0], weight=1)

#----------------Vendedores--------------------
lista_vendedores= [
    'Vitor',
    'Mariana',
]
#----------------Commands--------------------

def efetuar_analise():
    janela_analise= tk.Toplevel()

    janela_analise.rowconfigure([5, 0], weight=1) #Essa linha e a de baixo configuram p as cores acompanharem o esticamento da tela.
    janela_analise.columnconfigure([5, 0], weight=1)

    #----------------Layout Análise--------------------

    melhores_vendas_txt_vendas= tk.Label(janela_analise, text='Referências Mais Vendidas', borderwidth= 1, relief= 'solid', foreground="white", background="#363636", width="30", height="1", font=("Bold", 15))
    melhores_vendas_txt_vendas.grid(row=0, column= 1, sticky= 'nswe', columnspan= 3, pady=8)
    caixa_resultado_melhores_vendas= tk.Text(janela_analise, width= 55, height= 13)
    caixa_resultado_melhores_vendas.grid(row= 1, column=1, columnspan= 3, padx=20, pady=5, sticky= 'nswe')
    caixa_resultado_melhores_vendas.delete("1.0", tk.END)
    caixa_resultado_melhores_vendas.insert("1.0", f'{df_ref_vendas.sort_values(by="quantidade", ascending=False)}')

    numeracao_vendida_txt_vendas= tk.Label(janela_analise, text='Numerações Mais Vendidas', borderwidth= 1, relief= 'solid', foreground="white", background="#363636", width="30", height="1", font=("Bold", 15))
    numeracao_vendida_txt_vendas.grid(row=2, column= 1, sticky= 'nswe', columnspan= 3, pady=8)
    caixa_resultado_numeracao= tk.Text(janela_analise, width= 55, height= 13)
    caixa_resultado_numeracao.grid(row= 3, column=1, columnspan= 3, padx=20, pady=5, sticky= 'nswe')
    caixa_resultado_numeracao.delete("1.0", tk.END)
    caixa_resultado_numeracao.insert("1.0", f'{df_number_vendas.sort_values(by="quantidade", ascending=False)}')

    tipo_roupa_txt_vendas= tk.Label(janela_analise, text='Tipo de Roupa Mais Vendida', borderwidth= 1, relief= 'solid', foreground="white", background="#363636", width="30", height="1", font=("Bold", 15))
    tipo_roupa_txt_vendas.grid(row=4, column= 1, sticky= 'nswe', columnspan= 3, pady=8)
    caixa_resultado_tipo_roupa= tk.Text(janela_analise, width= 55, height= 13)
    caixa_resultado_tipo_roupa.grid(row= 5, column=1, columnspan= 3, padx=20, pady=5, sticky= 'nswe')
    caixa_resultado_tipo_roupa.delete("1.0", tk.END)
    caixa_resultado_tipo_roupa.insert("1.0", f'{df_tipo_vendas.sort_values(by="quantidade", ascending=False)}')

    ###########################

    ref_estoque_txt= tk.Label(janela_analise, text='Referências Em Estoque', borderwidth= 1, relief= 'solid', foreground="white", background="#363636", width="30", height="1", font=("Bold", 15))
    ref_estoque_txt.grid(row=0, column= 4, sticky= 'nswe', columnspan= 3, pady=8, padx=20)
    caixa_resultado_ref_estoque= tk.Text(janela_analise, width= 55, height= 13)
    caixa_resultado_ref_estoque.grid(row= 1, column=4, columnspan= 3, padx=20, pady=5, sticky= 'nswe')
    caixa_resultado_ref_estoque.delete("1.0", tk.END)
    caixa_resultado_ref_estoque.insert("1.0", f'{df_ref_estoque.sort_values(by="quantidade", ascending=False)}')

    number_estoque_txt= tk.Label(janela_analise, text='Numerações Em Estoque', borderwidth= 1, relief= 'solid', foreground="white", background="#363636", width="30", height="1", font=("Bold", 15))
    number_estoque_txt.grid(row=2, column= 4, sticky= 'nswe', columnspan= 3, pady=8, padx=20)
    caixa_resultado_ref_estoque= tk.Text(janela_analise, width= 55, height= 13)
    caixa_resultado_ref_estoque.grid(row= 3, column=4, columnspan= 3, padx=20, pady=5, sticky= 'nswe')
    caixa_resultado_ref_estoque.delete("1.0", tk.END)
    caixa_resultado_ref_estoque.insert("1.0", f'{df_tam_estoque.sort_values(by="quantidade", ascending=False)}')
    
    tipo_peca_estoque_txt= tk.Label(janela_analise, text='Tipos de Peças em Estoque', borderwidth= 1, relief= 'solid', foreground="white", background="#363636", width="30", height="1", font=("Bold", 15))
    tipo_peca_estoque_txt.grid(row=4, column= 4, sticky= 'nswe', columnspan= 3, pady=8, padx=20)
    caixa_resultado_peca_estoque= tk.Text(janela_analise, width= 55, height= 13)
    caixa_resultado_peca_estoque.grid(row= 5, column=4, columnspan= 3, padx=20, pady=5, sticky= 'nswe')
    caixa_resultado_peca_estoque.delete("1.0", tk.END)
    caixa_resultado_peca_estoque.insert("1.0", f'{df_tipo_peca.sort_values(by="quantidade", ascending=False)}')


def pulaLinha():
    return f"\n"*6

def darEspaco():
    return f" "*58
    
def buscar_produto():
    # caixa_ref.get('1.0', tk.END)
    # caixa_qtd.get('1.0', tk.END)
    # caixa_tamanho.get('1.0', tk.END)
    # caixa_valor.get('1.0', tk.END)
    tamanho_get= tamanho.get("1.0", tk.END)
    ref_get= ref.get("1.0", tk.END)
    # Produto encontrado pela referência
    '''
    Basicamente, na linha abaixo estava ''bugando'', pois o len(tamanho), quando VAZIO, dava UM, e não ZERO. Por isso, significa que quando era colocado
    UM caractere, o tamanho era DOIS.
    '''
    if 2 > len(tamanho_get): #Essa linha tava bugando, por isso foi "2 > len(tamanho).

        cursor_estoque.execute(f'SELECT * FROM controle WHERE ref= "{ref.get("1.0", tk.END)}"')
        valores= cursor_estoque.fetchall()
        #print(valores)

    elif 2 > len(ref_get):
        cursor_estoque.execute(f'SELECT * FROM controle WHERE tamanho= "{tamanho.get("1.0", tk.END)}"')
        valores= cursor_estoque.fetchall()

    else:
        cursor_estoque.execute(f'SELECT * FROM controle WHERE ref= "{ref.get("1.0", tk.END)}" AND tamanho= {tamanho_get}')
        valores= cursor_estoque.fetchall()
        #print(valores)
    texto = ''
    
    for id_produto, ref1, tamanho1, quantidade_pecas,valor , tipo_peca in valores:
        texto = texto + (f'----------------------------------\n'
                         f'ID: "{id_produto}"\n'
                         f'REFERÊNCIA: "{ref1}"\n'
                         f'TAMANHO: "{tamanho1}"\n'
                         f'QUANTIDADE: "{quantidade_pecas}"\n'
                         f'VALOR: R$"{valor:.2f}"\n'
                         f'TIPO DA PEÇA: "{tipo_peca}"\n'
        )
        
    if len(texto) > 0:
        caixa_resultado.delete("1.0", tk.END)
        caixa_resultado.insert("1.0", f'{texto}')
    else:
        caixa_resultado.delete("1.0", tk.END)
        caixa_resultado.insert("1.0", 'Produto não encontrado. Busque as peças [[APENAS]] por referência e/ou tamanho.')

def efetuar_venda():
    #Definindo a data atual.
    data_atual = datetime.now()
    data_formatada = data_atual.strftime("%d/%m/%Y")
    print(data_formatada)

    #valores do dropdown
    vendedor= vendedor_combo.get()
    print(vendedor)

    #Verificando se a referência já está cadastrada no banco de dados antes de executar a venda.
    #Observe que pegamos exatamente o valor da referência + tamanho para que não seja descontado as peças do tamanho errado.
    seleciona_coluna_ref = "SELECT ref FROM controle WHERE ref ='{}' AND tamanho='{}'".format(ref.get("1.0", tk.END), tamanho.get("1.0", tk.END))
    cursor_estoque.execute(seleciona_coluna_ref)
    resultado = cursor_estoque.fetchall() #O resultado é basicamente uma lista de tuplas dizendo o nome das tabelas.

    #"Se a caixa de referências NÃO ESTIVER VAZIA, execute isso". Essa linha verifica se a referência existe no banco de dados. Não dá pra vender algo que não existe.
    #Essa linha abaixo entra no banco de dados CONTROLE e pega TODOS os valores que estarão na referencia digitada.
    if len(resultado) != 0 :
        seleciona_quantidade_maior_0= "SELECT * FROM controle WHERE ref ='{}' AND tamanho='{}'".format(ref.get("1.0", tk.END), tamanho.get("1.0", tk.END))
        cursor_estoque.execute(seleciona_quantidade_maior_0)
        resultado_quantidade_maior_0 = cursor_estoque.fetchall() #TODOS os itens. Referência, quantidade estocada, numeração, etc

        for item in resultado_quantidade_maior_0:
            caixa_qtd_int = float(caixa_qtd.get("1.0", tk.END))
            subtracao_itens= item[3] - caixa_qtd_int
            print(type(caixa_qtd_int))
            print(item)
            #item 5, lá no banco de dados "controle" é o TIPO DA PEÇA.
            tipo_peca_em_estoque= str(item[5])
            setor_multiplicativo= caixa_qtd_int * float(item[4])

            if subtracao_itens >= 0:
                if len(vendedor) > 1:
                    comando_vendas= (f'INSERT INTO vendas (ref, number, quantidade, vendedor, data_venda, tipo_peca, valor)'
                            f'VALUES ({ref.get("1.0", tk.END)},  {tamanho.get("1.0", tk.END)}, {caixa_qtd.get("1.0", tk.END)}, " {vendedor} ", "{data_formatada}", "{tipo_peca_em_estoque}", {float(item[4])})')
                    cursor_vendas.execute(comando_vendas)
                    conexao_vendas.commit()
                    #print('Venda realizada com sucesso.')
                    quantidade_vendida= caixa_qtd.get("1.0", tk.END)
                    comando_estoque= (f'UPDATE controle SET quantidade_pecas = quantidade_pecas - {quantidade_vendida} WHERE ref= {ref.get("1.0", tk.END)} '
                            f'AND tamanho= {tamanho.get("1.0", tk.END)}')
                    cursor_estoque.execute(comando_estoque)
                    conexao_estoque.commit()
                    caixa_resultado.delete("1.0", tk.END)
                    caixa_resultado.insert("1.0", f"Venda Finalizada.\n Referência: {item[1]} \n Numeração: {item[2]} \n Valor Unitário: {item[4]} \n Modelo: {item[5]} \n Quantidade: {caixa_qtd.get('1.0', tk.END)} Valor Total: {setor_multiplicativo:.2f} \n Vendedor: {vendedor} {pulaLinha()} {darEspaco()} Data: {data_formatada} \n ")
                else:
                    caixa_resultado.insert("1.0", f"Não é possível encerrar uma venda sem indicar quem foi o vendedor.")
            else:
                caixa_resultado.delete("1.0", tk.END)
                caixa_resultado.insert("1.0", f"A quantidade de peças dessa referência e tamanho em sistema é igual a {item[3]},\n portanto, não é possível realizar a venda de {caixa_qtd_int:.0f} itens. \n Favor repor o estoque.")

    else:
        caixa_resultado.delete("1.0", tk.END)
        caixa_resultado.insert("1.0", "Ocorreu um erro na hora de finalizar a venda. O produto pode não estar atualizado em nosso banco de dados ou os dados estão incorretos/ incompletos.")
    

        
    
#----------------Layout--------------------

mensagem= customtkinter.CTkLabel(janela, text='Controle', font=("Arial", 25))
mensagem.grid(row=0, column= 0, sticky= 'nswe', columnspan= 6)

c_ref= customtkinter.CTkLabel(janela,text='Referência')
c_ref.grid(row=1, column= 0, padx= 20, pady=10, sticky= 'nswe', columnspan= 2)
ref= customtkinter.CTkTextbox(janela, width= 10, height= 1)
ref.grid(row= 2, column= 0, sticky= 'nswe', padx= 20, columnspan= 2)

qtd= customtkinter.CTkLabel(janela,text='Quantidade')
qtd.grid(row=1, column= 2, padx= 20, pady=10, sticky= 'nswe', columnspan= 2)
caixa_qtd= customtkinter.CTkTextbox(janela, width= 10, height= 1)
caixa_qtd.grid(row= 2, column= 2, sticky= 'nswe', padx= 20, columnspan= 2)

tamanho= customtkinter.CTkLabel(janela,text='Tamanho')
tamanho.grid(row= 1, column= 4, padx=20, pady=10, sticky= 'nswe', columnspan= 2)
tamanho= customtkinter.CTkTextbox(janela, width= 10, height= 1)
tamanho.grid(row=2, column= 4, sticky= 'nswe', padx= 20, columnspan= 2)

mensagem2= customtkinter.CTkLabel(janela,text='Ação', font=("Arial", 25))
mensagem2.grid(row=8, column= 0, sticky= 'nswe', pady=10, columnspan= 6)

caixa_resultado= tk.Text(janela,width= 50, height= 15)
caixa_resultado.grid(row= 10, column=0, columnspan= 6, padx=20, pady=10, sticky= 'nswe')

mensagem2= customtkinter.CTkLabel(janela,text='Análise Detalhada', font=("Arial", 25))
mensagem2.grid(row=11, column= 0, sticky= 'nswe', pady=(50, 20), columnspan= 6)

vendedores_combo_txt= customtkinter.CTkLabel(janela, text= "Vendedor")
vendedores_combo_txt.grid(row=6, column= 2, padx= 20, pady=5, sticky= 'nswe', columnspan=2)
vendedor_combo= customtkinter.CTkComboBox(janela, values= lista_vendedores)
vendedor_combo.grid(row=7, column= 2, padx= 20, pady=5, sticky= 'nswe', columnspan= 2)

#----------------Botões--------------------

fazer_venda= customtkinter.CTkButton(janela,corner_radius=10 ,text= 'Fazer Venda', command= efetuar_venda)
fazer_venda.grid(row=9, column= 0, padx=20, pady=10, sticky= 'nswe', columnspan= 2)

deletar_peca= customtkinter.CTkButton(janela, text= 'Buscar Produto', command= buscar_produto)
deletar_peca.grid(row=9, column= 5, padx=20, pady=10, sticky= 'nswe', columnspan= 2)

analise= customtkinter.CTkButton(janela, text= 'Efetuar Análise Detalhada', command=efetuar_analise)
analise.grid(row=12, column= 0, padx=20, pady=(0, 50), sticky= 'nswe', columnspan=6)

#janela tk
janela.mainloop()

#----------------Fechamento_vendas--------------------
cursor_vendas.close()
conexao_vendas.close()

#----------------Fechamento_estoque--------------------
cursor_estoque.close()
conexao_estoque.close()

