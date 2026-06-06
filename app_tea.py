import tkinter as tk
from tkinter import messagebox
import os

# Configuração de Cores Acessíveis (Cores pastéis evitam hipersensibilidade visual em crianças com TEA)
COR_FUNDO = "#EBF4F6"
COR_BOTAO_LETRAS = "#FFD1DC"  # Rosa pastel
COR_BOTAO_NUMEROS = "#BDFCC9" # Verde pastel
COR_TEXTO = "#2C3E50"

class AppEducacionalTEA:
    def __init__(self, root):
        self.root = root
        self.root.title("App Educacional - Aprendendo de Forma Divertida")
        self.root.geometry("600x500")
        self.root.configure(bg=COR_FUNDO)
        
        # Inicializa a tela principal
        self.criar_tela_principal()

    def limpar_tela(self):
        """Remove todos os widgets da tela atual para transição de menus."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def criar_tela_principal(self):
        self.limpar_tela()
        
        # Título Intuitivo com Fonte Amigável
        label_titulo = tk.Label(
            self.root, 
            text="Vamos Jogar?", 
            font=("Comic Sans MS", 28, "bold"), 
            bg=COR_FUNDO, 
            fg=COR_TEXTO
        )
        label_titulo.pack(pady=40)

        # Container para os botões em formato de ícones grandes (Navegação por Ícones / Baixo esforço físico)
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
        self.limpar_tela()
        
        label_instrucao = tk.Label(
            self.root, 
            text="Clique na Letra A", 
            font=("Comic Sans MS", 24, "bold"), 
            bg=COR_FUNDO, 
            fg=COR_TEXTO
        )
        label_instrucao.pack(pady=30)

        frame_opcoes = tk.Frame(self.root, bg=COR_FUNDO)
        frame_opcoes.pack(pady=20)

        # Botões de opção grandes para facilitar o clique
        btn_a = tk.Button(frame_opcoes, text="A", font=("Arial", 32, "bold"), width=4, bg="#FFF", command=lambda: self.processar_resposta(True))
        btn_a.grid(row=0, column=0, padx=15)

        btn_b = tk.Button(frame_opcoes, text="B", font=("Arial", 32, "bold"), width=4, bg="#FFF", command=lambda: self.processar_resposta(False))
        btn_b.grid(row=0, column=1, padx=15)
        
        btn_voltar = tk.Button(self.root, text="⬅ Voltar", font=("Comic Sans MS", 12), command=self.criar_tela_principal)
        btn_voltar.pack(side="bottom", pady=30)

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

        btn_1 = tk.Button(frame_opcoes, text="1", font=("Arial", 32, "bold"), width=4, bg="#FFF", command=lambda: self.processar_resposta(False))
        btn_1.grid(row=0, column=0, padx=15)

        btn_3 = tk.Button(frame_opcoes, text="3", font=("Arial", 32, "bold"), width=4, bg="#FFF", command=lambda: self.processar_resposta(True))
        btn_3.grid(row=0, column=1, padx=15)
        
        btn_voltar = tk.Button(self.root, text="⬅ Voltar", font=("Comic Sans MS", 12), command=self.criar_tela_principal)
        btn_voltar.pack(side="bottom", pady=30)

    def processar_resposta(self, acerto):
        """Fornece feedback visual e sonoro imediato adaptado (sem sons estridentes)."""
        if acerto:
            # Feedback Visual Positivo Seguro
            messagebox.showinfo("Parabéns!", "🌟 Você acertou! Muito bem! 🌟")
        else:
            # Tolerância ao Erro: Feedback suave sem tom punitivo
            messagebox.showinfo("Tente de Novo", "Vamos tentar mais uma vez? Você consegue! ✨")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppEducacionalTEA(root)
    root.mainloop()