# type: ignore


# Importar os módulos
import tkinter as tk
import pandas as pd
from tkinter import *
from tkinter import ttk




# Funções

def pesquisa_cadastro():
    # Criação do tkinter
    janela = tk.Tk()
    janela.geometry("500x300")
    janela.title("Login")

    # Criando as labels e entries
    nome_label = tk.Label(janela, text="Digite o Nome ou E-mail:")
    nome_label.grid(row=2, column=0, padx=10, pady=10)

    nome_entry = tk.Entry(janela, width=30)
    nome_entry.grid(row=2, column=1, padx=10, pady=10)

    senha_label = tk.Label(janela, text="Digite a senha:")
    senha_label.grid(row=3, column=0, padx=10, pady=10)

    senha_entry = tk.Entry(janela, width=30, show="*")
    senha_entry.grid(row=3, column=1, padx=10, pady=10)

    resultado_label = tk.Label(janela, text="")
    resultado_label.grid(row=4, column=1, padx=10, pady=10)

    # Definição da função de pesquisa
    def pesquisar():
        termo_procurado = nome_entry.get()
        senha_procurada = senha_entry.get()

        try:
            df = pd.read_excel('Dados Cadastro.xlsx')
        except FileNotFoundError:
            resultado_label.configure(text="Não há dados cadastrados ainda")
            return

        # Verifica se o termo é um email ou um nome
        if "@" in termo_procurado:
            resultado = df[df['Email'] == termo_procurado]
        else:
            resultado = df[df['Nome'] == termo_procurado]

        if resultado.empty:
            resultado_label.configure(text="Nome ou e-mail não encontrado. Faça o cadastro")
            return

        # Verifica se a senha está correta
        linha_resultado = resultado.iloc[0]
        senha_correta = linha_resultado['Senha']
        if senha_procurada != senha_correta:
            resultado_label.configure(text="Senha incorreta")
            return

        resultado_label.configure(text="Cadastro encontrado")
        janela.destroy

    # Criação do botão de pesquisa
    botao_pesquisar = tk.Button(janela, text="Login", command=pesquisar, width=20)
    botao_pesquisar.grid(row=5, column=1, columnspan=2 , padx=10, pady=10)
    Janela_cad.destroy()

    # Inicialização do tkinter
    janela.mainloop()


def botao_cad():
    usuario = Usuario_entry.get()
    email = Email_entry.get()
    tel = Telefone_entry.get()
    senha = Senha_entry.get()
    try:
        df = pd.read_excel('Dados Cadastro.xlsx', sheet_name='Dados')
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Nome", "Telefone", "Email", "Senha"])
        df.to_excel('Dados Cadastro.xlsx', sheet_name='Dados', index=False)
        
    new_data = pd.DataFrame({'Nome': [usuario], 'Telefone': [tel], 'Email': [email], 'Senha': [senha]})
    df = pd.concat([df, new_data], ignore_index=True)
    
    with pd.ExcelWriter('Dados Cadastro.xlsx', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='Dados', index=False)


def Consulta_de_info():
    

    # Leitura da planilha com Pandas
    df = pd.read_excel('Dados Cadastro.xlsx')

    # Cria a janela principal do programa
    root = Tk()
    root.title("Consultar Informações")

    # Cria a combobox com os nomes
    nomes = df['Nome'].tolist()
    combo = ttk.Combobox(root, values=nomes)
    combo.pack(pady=10)

    # Cria o widget de texto para exibir as informações
    info_text = Text(root)
    info_text.pack()

    # Cria o botão de consultar informações
    def consultar_informacoes():
        # Limpa o widget de texto antes de adicionar as informações atualizadas
        info_text.delete('1.0', END)

        # Obtém o nome selecionado na combobox
        nome = combo.get()

        # Filtra o dataframe pelo nome selecionado
        df_filtrado = df.loc[df['Nome'] == nome]

        if not df_filtrado.empty:
            # Converte o dataframe em uma string formatada e adiciona ao widget de texto
            informacoes = df_filtrado.to_string(index=False)
            info_text.insert(END, informacoes)
        else:
            # Adiciona uma mensagem de aviso caso o nome não seja encontrado
            mensagem = f"O usuário {nome} não foi encontrado."
            info_text.insert(END, mensagem)

    botao_consultar = Button(root, text="Consultar Informações", command=consultar_informacoes)
    botao_consultar.pack()

    root.mainloop()


def Deletar_user():

    def deletar():
        nome = combobox_deletar.get()
        df = pd.read_excel('Dados Cadastro.xlsx')
        df = df.loc[df['Nome'] != nome]
        df.to_excel('Dados Cadastro.xlsx', index=False)
        combobox_deletar.set('')
        result_deletar.configure(text="Cadastro deletado com sucesso!")
        
    def Sair():
        janela_deletar.destroy()

    df = pd.read_excel('Dados Cadastro.xlsx')
    nomes = df['Nome'].tolist()

    janela_deletar = tk.Tk()
    janela_deletar.title("Deletar Cadastro")
    janela_deletar.geometry("400x350")

    label_deletar = tk.Label(janela_deletar, text="Selecione um usuário:")
    label_deletar.grid(row=1, column=2, padx=10, pady=10)

    combobox_deletar = ttk.Combobox(janela_deletar, values=nomes)
    combobox_deletar.grid(row=2, column=2, padx=10, pady=10)

    botao_deletar = tk.Button(janela_deletar, text="Deletar", command=deletar)
    botao_deletar.grid(row=3, column=2, padx=10, pady=10)

    result_deletar = tk.Label(janela_deletar, text="")
    result_deletar.grid(row=4, column=2, padx=10, pady=10)
    
    botao_sair = tk.Button(janela_deletar, text='Sair', command=Sair)
    botao_sair.grid(row=6, column=2, padx=10, pady=10)

    janela_deletar.mainloop()


def botao_sair():
    Janela_cad.destroy()




Janela_cad = tk.Tk()
Janela_cad.title('Cadastro Usuário')
Janela_cad.geometry("500x400")



Usuario_label = tk.Label(Janela_cad, text='Usuário: ')
Usuario_label.grid(row=2, column=0, padx=10, pady=10)
Usuario_entry = tk.Entry(Janela_cad, width=20)
Usuario_entry.grid(row=2, column=1, padx=10, pady=10)

Email_label = tk.Label(Janela_cad, text='Email: ')
Email_label.grid(row=3, column=0, padx=10, pady=10)
Email_entry = tk.Entry(Janela_cad, width=20)
Email_entry.grid(row=3, column=1, padx=10, pady=10)

Telefone_label = tk.Label(Janela_cad, text='Telefone (Opcional)')
Telefone_label.grid(row=4, column=0, padx=10, pady=10)
Telefone_entry = tk.Entry(Janela_cad, width=20)
Telefone_entry.grid(row=4, column=1, padx=10, pady=10)

Senha_label = tk.Label(Janela_cad, text="Senha")
Senha_label.grid(row=5, column=0, padx=10, pady=10)
Senha_entry = tk.Entry(Janela_cad, width=20)
Senha_entry.grid(row=5, column=1, padx=10, pady=10)

botao_cadastrar = tk.Button(Janela_cad, text='Cadastrar', width=20, command=botao_cad)
botao_cadastrar.grid(row=6, column=1, padx=10, pady=10)

botao_login = tk.Button(Janela_cad, text='Login', width=20, command=pesquisa_cadastro)
botao_login.grid(row=7, column=1, padx=10, pady=10)

botao_consulta = tk.Button(Janela_cad, text='Consultar Info', width=20, command=Consulta_de_info)
botao_consulta.grid(row=8, column=1, padx=10, pady=10)

botao_deletar_user = tk.Button(Janela_cad, text='Deletar Usuário', command=Deletar_user, width=20)
botao_deletar_user.grid(row=9, column=1, padx=10, pady=10)

Botao_sair = tk.Button(Janela_cad, text='Sair', width=20, command=botao_sair)
Botao_sair.grid(row=10, column=1, padx=10, pady=10)



Janela_cad.mainloop()