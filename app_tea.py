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
        self.root.geometry("600x550")
        self.root.configure(bg=COR_FUNDO)
        
        # Variável para armazenar a letra alvo atual do jogo
        self.letra_alvo = ""
        
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
        """Módulo de Letras expandido de forma dinâmica para todo o alfabeto (A-Z)"""
        self.limpar_tela()
        
        # Seleciona uma letra aleatória de A a Z como alvo pedagógico
        self.letra_alvo = random.choice(string.ascii_uppercase)
        
        label_instrucao = tk.Label(
            self.root, 
            text=f"Clique na Letra {self.letra_alvo}", 
            font=("Comic Sans MS", 24, "bold"), 
            bg=COR_FUNDO, 
            fg=COR_TEXTO
        )
        label_instrucao.pack(pady=25)

        # Gera 4 alternativas: a letra correta + 3 letras incorretas aleatórias
        alternativas = [self.letra_alvo]
        while len(alternativas) < 4:
            letra_aleatoria = random.choice(string.ascii_uppercase)
            if letra_aleatoria not in alternativas:
                alternativas.append(letra_aleatoria)
        
        # Embaralha as alternativas para a letra certa não ficar sempre no mesmo lugar
        random.shuffle(alternativas)

        # Grid 2x2 para exibição de botões grandes e fáceis de clicar (Baixo esforço físico)
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
        """Processa a resposta fornecendo reforço positivo ou tolerância ao erro"""
        if letra_escolhida == self.letra_alvo:
            messagebox.showinfo("Parabéns!", "🌟 Você acertou! Muito bem! 🌟")
            self.abrir_modulo_letras()  # Avança para uma nova letra aleatória automaticamente
        else:
            messagebox.showinfo("Tente de Novo", "Vamos tentar mais uma vez? Você consegue! ✨")

    def abrir_modulo_numeros(self):
        self.limpar_tela()
        
        label_instrucao = tk.Label(
            self.root, 
            text="Quantas estrelas você vê?\n⭐  ⭐  ⭐", 
            font=("Comic Sans MS", 22, "bold"), 
            bg=COR_FUNDO, 
            fg=COR_TEXTO
        )
        label_instrucao.pack(pady=30)

        frame_opcoes = tk.Frame(self.root, bg=COR_FUNDO)
        frame_opcoes.pack(pady=20)

        btn_1 = tk.Button(frame_opcoes, text="1", font=("Arial", 32, "bold"), width=4, bg="#FFF", fg=COR_TEXTO, command=lambda: self.processar_resposta_geral(False))
        btn_1.grid(row=0, column=0, padx=15)

        btn_3 = tk.Button(frame_opcoes, text="3", font=("Arial", 32, "bold"), width=4, bg="#FFF", fg=COR_TEXTO, command=lambda: self.processar_resposta_geral(True))
        btn_3.grid(row=0, column=1, padx=15)
        
        btn_voltar = tk.Button(self.root, text="⬅ Voltar ao Menu", font=("Comic Sans MS", 12), command=self.criar_tela_principal)
        btn_voltar.pack(side="bottom", pady=30)

    def processar_resposta_geral(self, acerto):
        if acerto:
            messagebox.showinfo("Parabéns!", "🌟 Você acertou! Muito bem! 🌟")
        else:
            messagebox.showinfo("Tente de Novo", "Vamos tentar mais uma vez? Você consegue! ✨")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppEducacionalTEA(root)
    root.mainloop()