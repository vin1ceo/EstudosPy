import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from abc import ABC, abstractmethod

# --------------------------------------------------------------------
# PARTE 1: O "CÉREBRO" DO JOGO (Suas classes, levemente modificadas)
# --------------------------------------------------------------------

class Personagem(ABC):
    def __init__(self, nome, vida, pts_ataque, pts_defesa):
        self.__nome = nome
        self.__vida = vida
        self.__pts_ataque = pts_ataque
        self.__pts_defesa = pts_defesa

    @property
    def nome(self):
        return self.__nome

    @property
    def vida(self):
        return self.__vida
    
    @property
    def pts_ataque(self):
        return self.__pts_ataque

    @property
    def pts_defesa(self):
        return self.__pts_defesa
    
    def receber_dano(self, dano):
        dano_sofrido = dano - self.pts_defesa
        if dano_sofrido < 0:
            dano_sofrido = 0
        
        self.__vida -= dano_sofrido
        if self.__vida < 0:
            self.__vida = 0
        # MODIFICAÇÃO: Retorna a mensagem em vez de imprimir
        return f"-> {self.nome} sofreu {dano_sofrido:.0f} de dano e agora tem {self.vida:.0f} de vida."

    @abstractmethod
    def atacar(self, alvo):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida, pts_ataque, pts_defesa):
        super().__init__(nome, vida, pts_ataque, pts_defesa)
    
    def atacar(self, alvo):
        # MODIFICAÇÃO: Retorna a mensagem
        mensagem_ataque = f"🗡️ {self.nome} ataca {alvo.nome} com sua espada!"
        mensagem_dano = alvo.receber_dano(self.pts_ataque)
        return mensagem_ataque + "\n" + mensagem_dano


class Mago(Personagem):
    def __init__(self, nome, vida, pts_ataque, pts_defesa, mana):
        super().__init__(nome, vida, pts_ataque, pts_defesa)
        self.__mana = mana

    @property
    def mana(self):
        return self.__mana
    
    def atacar(self, alvo):
        custo_mana = 10
        if self.__mana >= custo_mana:
            dano_magico = self.pts_ataque * 1.5
            self.__mana -= custo_mana
            
            mensagem_ataque = f"✨ {self.nome} lança uma bola de fogo em {alvo.nome}!"
            mensagem_dano = alvo.receber_dano(dano_magico)
            return mensagem_ataque + "\n" + mensagem_dano
        else:
            return f"💨 {self.nome} tenta, mas não tem mana suficiente para o feitiço!"


# --------------------------------------------------------------------
# PARTE 2: A INTERFACE GRÁFICA (A "Tela" do Jogo)
# --------------------------------------------------------------------

class BattleGUI:
    def __init__(self, master, p1, p2):
        self.master = master
        self.p1 = p1
        self.p2 = p2
        self.turno = 0

        master.title("Arena de Batalha RPG")
        master.geometry("600x400")
        
        # --- Frames para organizar a tela ---
        frame_p1 = tk.Frame(master, relief=tk.GROOVE, borderwidth=2)
        frame_p1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        frame_p2 = tk.Frame(master, relief=tk.GROOVE, borderwidth=2)
        frame_p2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # --- Widgets do Personagem 1 ---
        self.p1_nome_label = tk.Label(frame_p1, text=p1.nome, font=("Helvetica", 16, "bold"))
        self.p1_nome_label.pack(pady=5)
        self.p1_vida_label = tk.Label(frame_p1, text=f"Vida: {p1.vida:.0f}", font=("Helvetica", 12))
        self.p1_vida_label.pack(pady=5)
        self.p1_mana_label = tk.Label(frame_p1, text="", font=("Helvetica", 12)) # Vazio por enquanto
        if isinstance(p1, Mago):
            self.p1_mana_label.pack(pady=5)

        # --- Widgets do Personagem 2 ---
        self.p2_nome_label = tk.Label(frame_p2, text=p2.nome, font=("Helvetica", 16, "bold"))
        self.p2_nome_label.pack(pady=5)
        self.p2_vida_label = tk.Label(frame_p2, text=f"Vida: {p2.vida:.0f}", font=("Helvetica", 12))
        self.p2_vida_label.pack(pady=5)
        self.p2_mana_label = tk.Label(frame_p2, text="", font=("Helvetica", 12)) # Vazio por enquanto
        if isinstance(p2, Mago):
            self.p2_mana_label.pack(pady=5)

        # --- Log de Batalha e Botão ---
        self.log_batalha = scrolledtext.ScrolledText(master, height=8, state=tk.DISABLED)
        self.log_batalha.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
        
        self.botao_turno = tk.Button(master, text="Iniciar Batalha", command=self.proximo_turno)
        self.botao_turno.pack(side=tk.BOTTOM, pady=5)
        
        self.atualizar_status()

    def logar_mensagem(self, mensagem):
        self.log_batalha.config(state=tk.NORMAL)
        self.log_batalha.insert(tk.END, mensagem + "\n\n")
        self.log_batalha.config(state=tk.DISABLED)
        self.log_batalha.see(tk.END) # Auto-scroll

    def atualizar_status(self):
        self.p1_vida_label.config(text=f"Vida: {self.p1.vida:.0f}")
        if isinstance(self.p1, Mago):
            self.p1_mana_label.config(text=f"Mana: {self.p1.mana:.0f}")

        self.p2_vida_label.config(text=f"Vida: {self.p2.vida:.0f}")
        if isinstance(self.p2, Mago):
            self.p2_mana_label.config(text=f"Mana: {self.p2.mana:.0f}")

    def proximo_turno(self):
        if self.turno == 0:
            self.botao_turno.config(text="Próximo Turno")
            self.logar_mensagem(f"💥 A BATALHA COMEÇA: {self.p1.nome} VS {self.p2.nome} 💥")

        # Verifica se a batalha já terminou
        if self.p1.vida <= 0 or self.p2.vida <= 0:
            return

        # Determina quem ataca
        if self.turno % 2 == 0:
            atacante, alvo = self.p1, self.p2
        else:
            atacante, alvo = self.p2, self.p1
            
        # Executa o ataque e loga a mensagem retornada
        resultado_ataque = atacante.atacar(alvo)
        self.logar_mensagem(resultado_ataque)

        # Atualiza a tela
        self.atualizar_status()
        self.turno += 1

        # Verifica o vencedor
        if self.p1.vida <= 0:
            self.logar_mensagem(f"🏆 O grande vencedor é {self.p2.nome}!")
            self.botao_turno.config(state=tk.DISABLED)
        elif self.p2.vida <= 0:
            self.logar_mensagem(f"🏆 O grande vencedor é {self.p1.nome}!")
            self.botao_turno.config(state=tk.DISABLED)


# --------------------------------------------------------------------
# PARTE 3: Execução do Programa
# --------------------------------------------------------------------

# Garante que o código só será executado quando o arquivo for rodado diretamente
# Exemplo de uma nova batalha:

if __name__ == "__main__":
    
    # --- PASSO 1: CRIE PERSONAGENS DIFERENTES ---
    guerreira_veterana = Guerreiro(nome="Xena", vida=150, pts_ataque=15, pts_defesa=12)
    mago_aprendiz = Mago(nome="Elminster", vida=70, pts_ataque=25, pts_defesa=4, mana=30)
    
    # O resto do código é EXATAMENTE O MESMO
    root = tk.Tk()
    app = BattleGUI(root, guerreira_veterana, mago_aprendiz) # Entregamos os novos personagens
    root.mainloop()