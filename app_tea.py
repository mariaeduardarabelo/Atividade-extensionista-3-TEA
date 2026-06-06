import tkinter as tk
from tkinter import messagebox
import random
import string

# Configuração de Cores Acessíveis (Evitam hipersensibilidade visual em crianças com TEA)
COR_FUNDO = "#EBF4F6"
COR_BOTAO_LETRAS = "#FFD1DC"  # Rosa pastel
COR_BOTAO_NUMEROS = "#BDFCC9" # Verde pastel
COR_TEXTO = "#2C3E50"

class AppEducacionalTEA:
    def __init__(self, root):
        self.root = root
        self.root.title("App Educacional - Aprendendo de Forma Divertida")
        self.root.geometry("600x580")
        self.root.configure(bg=COR_FUNDO)
        
        # Variáveis de controle dos jogos
        self.letra_alvo = ""
        self.numero_alvo = 0
        self.objeto_atual = ""
        
        # Inicializa a tela principal
        self.criar_tela_principal()

    def limpar_tela(self):
        """Remove todos os widgets da tela atual para transição de menus."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def criar_tela_principal(self):
        self.limpar_tela()
        
        label_titulo = tk.Label(
            self.root, 
            text="Vamos Jogar?", 
            font=("Comic Sans MS", 28, "bold"), 
            bg=COR_FUNDO, 
            fg=COR_TEXTO
        )
        label_titulo.pack(pady=40)

        frame_botoes = tk.Frame(self.root, bg=COR_FUNDO)
        frame_botoes.pack(pady=20)

        btn_letras = tk.Button(
            frame_botoes, 
            text="🔤\nLetras", 
            font=("Comic Sans MS", 18, "bold"),
            bg=COR_BOTAO_LETRAS, 
            fg=COR_TEXTO,
            width=10, 
            height=4, 
            bd=3, 
            relief="groove",
            command=self.abrir_modulo_letras
        )
        btn_letras.grid(row=0, column=0, padx=20)

        btn_numeros = tk.Button(
            frame_botoes, 
            text="🔢\nNúmeros", 
            font=("Comic Sans MS", 18, "bold"),
            bg=COR_BOTAO_NUMEROS, 
            fg=COR_TEXTO,
            width=10, 
            height=4, 
            bd=3, 
            relief="groove",
            command=self.abrir_modulo_numeros
        )
        btn_numeros.grid(row=0, column=1, padx=20)

    def abrir_modulo_letras(self):
        """Módulo de Letras dinâmico para todo o alfabeto (A-Z)"""
        self.limpar_tela()
        
        self.letra_alvo = random.choice(string.ascii_uppercase)
        
        label_instrucao = tk.Label(
            self.root, 
            text=f"Clique na Letra {self.letra_alvo}", 
            font=("Comic Sans MS", 24, "bold"), 
            bg=COR_FUNDO, 
            fg=COR_TEXTO
        )
        label_instrucao.pack(pady=25)

        alternativas = [self.letra_alvo]
        while len(alternativas) < 4:
            letra_aleatoria = random.choice(string.ascii_uppercase)
            if letra_aleatoria not in alternativas:
                alternativas.append(letra_aleatoria)
        
        random.shuffle(alternativas)

        frame_opcoes = tk.Frame(self.root, bg=COR_FUNDO)
        frame_opcoes.pack(pady=15)

        for indice, letra in enumerate(alternativas):
            linha = indice // 2
            coluna = indice % 2
            
            btn_opcao = tk.Button(
                frame_opcoes, 
                text=letra, 
                font=("Arial", 32, "bold"), 
                width=5, 
                bg="#FFFFFF",
                fg=COR_TEXTO,
                bd=2,
                relief="raised",
                command=lambda l=letra: self.verificar_resposta_letras(l)
            )
            btn_opcao.grid(row=linha, column=coluna, padx=15, pady=15)
        
        btn_voltar = tk.Button(self.root, text="⬅ Voltar ao Menu", font=("Comic Sans MS", 12), command=self.criar_tela_principal)
        btn_voltar.pack(side="bottom", pady=25)

    def verificar_resposta_letras(self, letra_escolhida):
        if letra_escolhida == self.letra_alvo:
            messagebox.showinfo("Parabéns!", "🌟 Você acertou! Muito bem! 🌟")
            self.abrir_modulo_letras()
        else:
            messagebox.showinfo("Tente de Novo", "Vamos tentar mais uma vez? Você consegue! ✨")

    def abrir_modulo_numeros(self):
        """Módulo de Números atualizado: sorteia até 10 e varia os objetos na tela"""
        self.limpar_tela()
        
        # Sorteia uma quantidade de 1 a 10
        self.numero_alvo = random.randint(1, 10)
        
        # Lista com formatos e objetos diferentes para diversificar os estímulos
        lista_objetos = ['🍎', '🎈', '🚗', '🐱', '⚽', '🍦', '🦋', '🐶', '🍕', '🧸']
        self.objeto_atual = random.choice(lista_objetos)
        
        # Organiza a exibição dos objetos para não quebrar a tela de forma desorganizada
        if self.numero_alvo <= 5:
            exibicao_objetos = "  ".join([self.objeto_atual] * self.numero_alvo)
        else:
            # Se for maior que 5, quebra em duas linhas para manter o design limpo
            linha1 = "  ".join([self.objeto_atual] * 5)
            linha2 = "  ".join([self.objeto_atual] * (self.numero_alvo - 5))
            exibicao_objetos = f"{linha1}\n{linha2}"
        
        label_instrucao = tk.Label(
            self.root, 
            text=f"Quantos você vê?\n\n{exibicao_objetos}", 
            font=("Comic Sans MS", 22, "bold"), 
            bg=COR_FUNDO, 
            fg=COR_TEXTO
        )
        label_instrucao.pack(pady=20)

        # Gera 4 alternativas numéricas (a correta + 3 erradas de 1 a 10)
        alternativas = [self.numero_alvo]
        while len(alternativas) < 4:
            num_aleatorio = random.randint(1, 10)
            if num_aleatorio not in alternativas:
                alternativas.append(num_aleatorio)
        
        random.shuffle(alternativas)

        # Grid de botões 2x2 para facilitar a escolha física da criança
        frame_opcoes = tk.Frame(self.root, bg=COR_FUNDO)
        frame_opcoes.pack(pady=10)

        for indice, num in enumerate(alternativas):
            linha = indice // 2
            coluna = indice % 2
            
            btn_opcao = tk.Button(
                frame_opcoes, 
                text=str(num), 
                font=("Arial", 28, "bold"), 
                width=5, 
                bg="#FFFFFF",
                fg=COR_TEXTO,
                bd=2,
                relief="raised",
                command=lambda n=num: self.verificar_resposta_numeros(n)
            )
            btn_opcao.grid(row=linha, column=coluna, padx=15, pady=12)
        
        btn_voltar = tk.Button(self.root, text="⬅ Voltar ao Menu", font=("Comic Sans MS", 12), command=self.criar_tela_principal)
        btn_voltar.pack(side="bottom", pady=20)

    def verificar_resposta_numeros(self, numero_escolhido):
        if numero_escolhido == self.numero_alvo:
            messagebox.showinfo("Parabéns!", "🌟 Você acertou! Muito bem! 🌟")
            self.abrir_modulo_numeros() # Carrega um novo desafio de contagem automaticamente
        else:
            messagebox.showinfo("Tente de Novo", "Vamos tentar mais uma vez? Você consegue! ✨")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppEducacionalTEA(root)
    root.mainloop()