import customtkinter as ctk
import random

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

PLATAFORMA_NOME = "•  Genius Edu •"

PARTICIPANTES = {"ana", "beto", "carol", "davi"}

AREAS = {
    "Português": ["Quiz", "Forca", "Caça-palavras"],
    "Matemática": ["Quiz", "Decifração"],
    "Ciências": ["Quiz"],
    "História": ["Quiz"]
}

PERGUNTAS = {
    "Português": {
        "Quiz": [
            ("Qual é o plural de 'cão'?", ["Cães", "Cãos", "Cãoses", "Cãons"], "Cães"),
            ("Qual é o feminino de 'menino'?", ["Menina", "Menine", "Meninos", "Menininha"], "Menina"),
            ("Qual é o antônimo de 'feliz'?", ["Triste", "Alegre", "Contente", "Satisfeito"], "Triste"),
            ("Qual é o verbo na frase: 'Ela correu rápido'?", ["correu", "Ela", "rápido", "frase"], "correu"),
            ("O que é uma onomatopeia?", ["Imitação de som", "Nome próprio", "Verbo", "Adjetivo"], "Imitação de som"),
        ],
        "Forca": [
            "amizade", "alegria", "sabedoria", "livro", "escola", "gramatica", "palavra"
        ],
        "Caça-palavras": [
            {
                "matriz": [
                    list("C A S A"),
                    list("A M O R"),
                    list("S O L X"),
                    list("A R V O")
                ],
                "palavras": ["CASA", "AMOR", "SOL", "ARVO"],
                "dicas": [
                    "Lugar onde moramos",
                    "Sentimento forte",
                    "Estrela que ilumina",
                    "Começo de 'árvore'"
                ]
            },
            {
                "matriz": [
                    list("P A L A V R A"),
                    list("L I V R O X X"),
                    list("E S C O L A"),
                    list("A M I G O X")
                ],
                "palavras": ["PALAVRA", "LIVRO", "ESCOLA", "AMIGO"],
                "dicas": [
                    "Conjunto de letras com significado",
                    "Objeto de leitura",
                    "Local de aprendizado",
                    "Pessoa querida"
                ]
            }
        ]
    },
    "Matemática": {
        "Quiz": [
            ("Quanto é 7 x 8?", ["56", "54", "48", "58"], "56"),
            ("Qual é a raiz quadrada de 49?", ["7", "6", "8", "9"], "7"),
            ("Quanto é 12 x 3?", ["36", "15", "24", "30"], "36"),
            ("Quanto é 25 ÷ 5?", ["5", "10", "15", "20"], "5"),
            ("Qual a raiz quadrada de 81?", ["9", "8", "7", "6"], "9"),
        ],
        "Decifração": [
            ("Resolva: 12 + __ = 20", ["8", "6", "10", "12"], "8"),
            ("Resolva: __ x 5 = 35", ["7", "5", "6", "8"], "7"),
            ("Resolva: 100 - __ = 55", ["45", "55", "65", "35"], "45"),
            ("Resolva: 9 x __ = 81", ["9", "8", "7", "6"], "9"),
            ("Resolva: __ ÷ 2 = 6", ["12", "10", "8", "14"], "12"),
        ]
    },
    "Ciências": {
        "Quiz": [
            ("O que é biosfera?", ["Conjunto de todos os seres vivos", "Atmosfera", "Solo", "Água"], "Conjunto de todos os seres vivos"),
            ("Qual é o símbolo químico do ouro?", ["Au", "Ag", "Fe", "Hg"], "Au"),
            ("Qual planeta é conhecido como planeta vermelho?", ["Marte", "Júpiter", "Saturno", "Vênus"], "Marte"),
            ("Qual órgão bombeia sangue?", ["Coração", "Pulmão", "Fígado", "Rim"], "Coração"),
            ("Qual é o estado da água a 100°C?", ["Gasoso", "Líquido", "Sólido", "Plasma"], "Gasoso"),
        ]
    },
    "História": {
        "Quiz": [
            ("Quem proclamou a independência do Brasil?", ["Dom Pedro I", "Dom Pedro II", "Getúlio Vargas", "Tiradentes"], "Dom Pedro I"),
            ("Em que ano foi proclamada a independência do Brasil?", ["1822", "1500", "1889", "1964"], "1822"),
            ("Quem foi o primeiro presidente do Brasil?", ["Deodoro da Fonseca", "Getúlio Vargas", "Juscelino Kubitschek", "Lula"], "Deodoro da Fonseca"),
            ("Qual era a capital do Brasil antes de Brasília?", ["Rio de Janeiro", "São Paulo", "Salvador", "Belo Horizonte"], "Rio de Janeiro"),
            ("Quem foi Zumbi dos Palmares?", ["Líder quilombola", "Imperador", "Presidente", "Bandeirante"], "Líder quilombola"),
        ]
    }
}

class PlataformaEducativa(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(f"🌟 {PLATAFORMA_NOME} 🌟")
        self.geometry("850x650")
        self.resizable(False, False)
        self.configure(fg_color="#e9f5db")
        self.frames = {}
        self.usuario = None
        self.area = None
        self.tipo = None
        self._criar_frames()
        self.mostrar_frame("Login")

    def _criar_frames(self):
        self.frames["Login"] = FrameLogin(self, self.autenticar, self.cadastrar)
        self.frames["Home"] = FrameAbertura(self, self.mostrar_frame)
        self.frames["Area"] = FrameArea(self, self.selecionar_area)
        self.frames["Tipo"] = FrameTipo(self, self.selecionar_tipo)
        self.frames["Quiz"] = FrameQuiz(self, self.voltar_tipo)
        self.frames["Decifração"] = FrameDecifracao(self, self.voltar_tipo)
        self.frames["Forca"] = FrameForca(self, self.voltar_tipo)
        self.frames["CacaPalavras"] = FrameCacaPalavras(self, self.voltar_tipo)
        for frame in self.frames.values():
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def mostrar_frame(self, nome):
        for f in self.frames.values():
            f.lower()
        self.frames[nome].lift()

    def autenticar(self, usuario):
        if usuario.lower() in PARTICIPANTES:
            self.usuario = usuario.capitalize()
            self.mostrar_frame("Home")
        else:
            self.frames["Login"].msg_erro("Usuário não cadastrado!")

    def cadastrar(self, usuario):
        if not usuario:
            self.frames["Login"].msg_erro("Digite um nome para cadastrar!")
        elif usuario.lower() in PARTICIPANTES:
            self.frames["Login"].msg_erro("Usuário já existe!")
        else:
            PARTICIPANTES.add(usuario.lower())
            self.frames["Login"].msg_erro("Cadastro realizado! Faça login.", cor="#38b000")

    def selecionar_area(self, area):
        self.area = area
        self.frames["Tipo"].configurar(area)
        self.mostrar_frame("Tipo")

    def selecionar_tipo(self, tipo):
        self.tipo = tipo
        if tipo == "Quiz":
            self.frames["Quiz"].novo_jogo(self.area)
            self.mostrar_frame("Quiz")
        elif tipo == "Decifração":
            self.frames["Decifração"].novo_jogo(self.area)
            self.mostrar_frame("Decifração")
        elif tipo == "Forca":
            self.frames["Forca"].novo_jogo(self.area)
            self.mostrar_frame("Forca")
        elif tipo == "Caça-palavras":
            self.frames["CacaPalavras"].novo_jogo(self.area)
            self.mostrar_frame("CacaPalavras")

    def voltar_tipo(self):
        self.mostrar_frame("Tipo")

class FrameLogin(ctk.CTkFrame):
    def __init__(self, master, autenticar, cadastrar):
        super().__init__(master, fg_color="#b5ead7")
        self.autenticar = autenticar
        self.cadastrar = cadastrar
        ctk.CTkLabel(self, text=f"🎓 Bem-vindo ao {PLATAFORMA_NOME}!", font=("Comic Sans MS", 28, "bold"), text_color="#38b000").pack(pady=40)
        ctk.CTkLabel(self, text="Digite seu nome:", font=("Comic Sans MS", 18), text_color="#22577a").pack(pady=10)
        self.entry = ctk.CTkEntry(self, font=("Comic Sans MS", 18), width=220, corner_radius=20)
        self.entry.pack(pady=10)
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(pady=10)
        ctk.CTkButton(btn_frame, text="Entrar", font=("Comic Sans MS", 18, "bold"), fg_color="#38b000", hover_color="#70e000", text_color="#fff", corner_radius=32, command=self.tentar).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Cadastrar", font=("Comic Sans MS", 18, "bold"), fg_color="#22577a", hover_color="#57cc99", text_color="#fff", corner_radius=32, command=self.tentar_cadastro).pack(side="left", padx=5)
        self.label_erro = ctk.CTkLabel(self, text="", font=("Comic Sans MS", 16), text_color="#d90429")
        self.label_erro.pack(pady=5)

    def tentar(self):
        self.label_erro.configure(text="", text_color="#d90429")
        usuario = self.entry.get().strip()
        self.autenticar(usuario)

    def tentar_cadastro(self):
        self.label_erro.configure(text="", text_color="#d90429")
        usuario = self.entry.get().strip()
        self.cadastrar(usuario)

    def msg_erro(self, msg, cor="#d90429"):
        self.label_erro.configure(text=msg, text_color=cor)

class FrameAbertura(ctk.CTkFrame):
    def __init__(self, master, trocar):
        super().__init__(master, fg_color="#e9f5db")
        ctk.CTkLabel(self, text=f"🌟 {PLATAFORMA_NOME} 🌟", font=("Comic Sans MS", 34, "bold"), text_color="#22577a").pack(pady=40)
        ctk.CTkLabel(self, text="Aprenda brincando! Escolha uma área para começar:", font=("Comic Sans MS", 20), text_color="#38b000").pack(pady=10)
        ctk.CTkButton(self, text="🎯 Escolher Área", font=("Comic Sans MS", 22, "bold"), fg_color="#38b000", hover_color="#70e000", text_color="#fff", corner_radius=32, command=lambda: trocar("Area")).pack(pady=30)
        ctk.CTkButton(self, text="❌ Sair", font=("Comic Sans MS", 18), fg_color="#d90429", hover_color="#ef233c", text_color="#fff", corner_radius=32, command=master.destroy).pack(pady=10)

class FrameArea(ctk.CTkFrame):
    def __init__(self, master, selecionar_area):
        super().__init__(master, fg_color="#e9f5db")
        ctk.CTkLabel(self, text="Escolha a área do conhecimento:", font=("Comic Sans MS", 26, "bold"), text_color="#22577a").pack(pady=40)
        for area in AREAS:
            ctk.CTkButton(self, text=area, font=("Comic Sans MS", 20, "bold"), fg_color="#57cc99", hover_color="#80ed99", text_color="#22577a", corner_radius=32, command=lambda a=area: selecionar_area(a)).pack(pady=10)
        ctk.CTkButton(self, text="🏠 Home", font=("Comic Sans MS", 16), fg_color="#b5ead7", hover_color="#57cc99", text_color="#22577a", corner_radius=32, command=lambda: master.mostrar_frame("Home")).pack(pady=20)

class FrameTipo(ctk.CTkFrame):
    def __init__(self, master, selecionar_tipo):
        super().__init__(master, fg_color="#e9f5db")
        self.selecionar_tipo = selecionar_tipo
        self.label = ctk.CTkLabel(self, text="", font=("Comic Sans MS", 26, "bold"), text_color="#22577a")
        self.label.pack(pady=40)
        self.botoes = []
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=10)
        ctk.CTkButton(self, text="🏠 Home", font=("Comic Sans MS", 16), fg_color="#b5ead7", hover_color="#57cc99", text_color="#22577a", corner_radius=32, command=lambda: master.mostrar_frame("Home")).pack(pady=20)

    def configurar(self, area):
        for btn in self.botoes:
            btn.destroy()
        self.botoes.clear()
        self.label.configure(text=f"{area} - Escolha o tipo de jogo:")
        for tipo in AREAS[area]:
            btn = ctk.CTkButton(self.btn_frame, text=tipo, font=("Comic Sans MS", 20, "bold"), fg_color="#38b000", hover_color="#70e000", text_color="#fff", corner_radius=32, command=lambda t=tipo: self.selecionar_tipo(t))
            btn.pack(pady=10)
            self.botoes.append(btn)

class FrameQuiz(ctk.CTkFrame):
    def __init__(self, master, voltar):
        super().__init__(master, fg_color="#e9f5db")
        self.voltar = voltar
        self.area = None
        self.perguntas = []
        self.indice = 0
        self.pontos = 0
        self.progress = ctk.CTkProgressBar(self, width=400, height=20, progress_color="#38b000")
        self.progress.pack(pady=10, padx=30)
        self.label_pergunta = ctk.CTkLabel(self, font=("Comic Sans MS", 22, "bold"), text_color="#22577a")
        self.label_pergunta.pack(pady=30)
        self.botoes = []
        for i in range(4):
            btn = ctk.CTkButton(self, text="", font=("Comic Sans MS", 18), fg_color="#57cc99", hover_color="#80ed99", text_color="#22577a", corner_radius=32, command=lambda idx=i: self.responder(idx))
            btn.pack(pady=7)
            self.botoes.append(btn)
        self.label_resultado = ctk.CTkLabel(self, font=("Comic Sans MS", 18), text_color="#22577a")
        self.label_resultado.pack(pady=10)
        ctk.CTkButton(self, text="🏠 Home", font=("Comic Sans MS", 16), fg_color="#b5ead7", hover_color="#57cc99", text_color="#22577a", corner_radius=32, command=lambda: master.mostrar_frame("Home")).pack(pady=10)
        ctk.CTkButton(self, text="⬅️ Tipos", font=("Comic Sans MS", 16), fg_color="#d1d5db", hover_color="#6b7280", text_color="#22577a", corner_radius=32, command=voltar).pack(pady=5)

    def novo_jogo(self, area):
        self.area = area
        self.pontos = 0
        self.perguntas = random.sample(PERGUNTAS[area]["Quiz"], len(PERGUNTAS[area]["Quiz"]))
        self.indice = 0
        self.mostrar_pergunta()

    def mostrar_pergunta(self):
        total = len(self.perguntas)
        self.progress.set(self.indice / total if total else 1)
        if self.indice < total:
            pergunta, alternativas, _ = self.perguntas[self.indice]
            self.label_pergunta.configure(text=pergunta)
            random.shuffle(alternativas)
            for i, btn in enumerate(self.botoes):
                btn.configure(text=alternativas[i], state="normal", fg_color="#57cc99")
            self.label_resultado.configure(text="")
        else:
            self.label_pergunta.configure(text=f"Fim do Quiz! Pontuação: {self.pontos}/{len(self.perguntas)}")
            for btn in self.botoes:
                btn.configure(text="", state="disabled")
            self.label_resultado.configure(text="")

    def responder(self, idx):
        _, alternativas, correta = self.perguntas[self.indice]
        resposta = self.botoes[idx].cget("text")
        if resposta == correta:
            self.label_resultado.configure(text="🎉 Acertou!", text_color="#38b000")
            self.pontos += 1
            self.botoes[idx].configure(fg_color="#38b000")
        else:
            self.label_resultado.configure(text=f"😅 Errou! Resposta: {correta}", text_color="#d90429")
            self.botoes[idx].configure(fg_color="#d90429")
        for btn in self.botoes:
            btn.configure(state="disabled")
        self.indice += 1
        self.after(1200, self.mostrar_pergunta)

class FrameDecifracao(ctk.CTkFrame):
    def __init__(self, master, voltar):
        super().__init__(master, fg_color="#e9f5db")
        self.voltar = voltar
        self.area = None
        self.perguntas = []
        self.indice = 0
        self.pontos = 0
        self.progress = ctk.CTkProgressBar(self, width=400, height=20, progress_color="#38b000")
        self.progress.pack(pady=10, padx=30)
        self.label_pergunta = ctk.CTkLabel(self, font=("Comic Sans MS", 22, "bold"), text_color="#22577a")
        self.label_pergunta.pack(pady=30)
        self.botoes = []
        for i in range(4):
            btn = ctk.CTkButton(self, text="", font=("Comic Sans MS", 18), fg_color="#57cc99", hover_color="#80ed99", text_color="#22577a", corner_radius=32, command=lambda idx=i: self.responder(idx))
            btn.pack(pady=7)
            self.botoes.append(btn)
        self.label_resultado = ctk.CTkLabel(self, font=("Comic Sans MS", 18), text_color="#22577a")
        self.label_resultado.pack(pady=10)
        ctk.CTkButton(self, text="🏠 Home", font=("Comic Sans MS", 16), fg_color="#b5ead7", hover_color="#57cc99", text_color="#22577a", corner_radius=32, command=lambda: master.mostrar_frame("Home")).pack(pady=10)
        ctk.CTkButton(self, text="⬅️ Tipos", font=("Comic Sans MS", 16), fg_color="#d1d5db", hover_color="#6b7280", text_color="#22577a", corner_radius=32, command=voltar).pack(pady=5)

    def novo_jogo(self, area):
        self.area = area
        self.pontos = 0
        self.perguntas = random.sample(PERGUNTAS[area]["Decifração"], len(PERGUNTAS[area]["Decifração"]))
        self.indice = 0
        self.mostrar_pergunta()

    def mostrar_pergunta(self):
        total = len(self.perguntas)
        self.progress.set(self.indice / total if total else 1)
        if self.indice < total:
            pergunta, alternativas, _ = self.perguntas[self.indice]
            self.label_pergunta.configure(text=pergunta)
            random.shuffle(alternativas)
            for i, btn in enumerate(self.botoes):
                btn.configure(text=alternativas[i], state="normal", fg_color="#57cc99")
            self.label_resultado.configure(text="")
        else:
            self.label_pergunta.configure(text=f"Fim! Pontuação: {self.pontos}/{len(self.perguntas)}")
            for btn in self.botoes:
                btn.configure(text="", state="disabled")
            self.label_resultado.configure(text="")

    def responder(self, idx):
        _, alternativas, correta = self.perguntas[self.indice]
        resposta = self.botoes[idx].cget("text")
        if resposta == correta:
            self.label_resultado.configure(text="🎉 Acertou!", text_color="#38b000")
            self.pontos += 1
            self.botoes[idx].configure(fg_color="#38b000")
        else:
            self.label_resultado.configure(text=f"😅 Errou! Resposta: {correta}", text_color="#d90429")
            self.botoes[idx].configure(fg_color="#d90429")
        for btn in self.botoes:
            btn.configure(state="disabled")
        self.indice += 1
        self.after(1200, self.mostrar_pergunta)

class FrameForca(ctk.CTkFrame):
    def __init__(self, master, voltar):
        super().__init__(master, fg_color="#e9f5db")
        self.voltar = voltar
        self.area = None
        self.palavra = ""
        self.letras_certas = set()
        self.tentativas = 6
        self.label_palavra = ctk.CTkLabel(self, font=("Comic Sans MS", 28, "bold"), text_color="#22577a")
        self.label_palavra.pack(pady=30)
        self.label_status = ctk.CTkLabel(self, font=("Comic Sans MS", 18), text_color="#22577a")
        self.label_status.pack(pady=10)
        self.entry = ctk.CTkEntry(self, font=("Comic Sans MS", 18), width=60, placeholder_text="Letra")
        self.entry.pack(pady=10)
        ctk.CTkButton(self, text="Chutar", font=("Comic Sans MS", 18), fg_color="#38b000", hover_color="#70e000", text_color="#fff", corner_radius=32, command=self.chutar).pack(pady=10)
        ctk.CTkButton(self, text="🏠 Home", font=("Comic Sans MS", 16), fg_color="#b5ead7", hover_color="#57cc99", text_color="#22577a", corner_radius=32, command=lambda: master.mostrar_frame("Home")).pack(pady=10)
        ctk.CTkButton(self, text="⬅️ Tipos", font=("Comic Sans MS", 16), fg_color="#d1d5db", hover_color="#6b7280", text_color="#22577a", corner_radius=32, command=voltar).pack(pady=5)

    def novo_jogo(self, area):
        self.area = area
        self.palavra = random.choice(PERGUNTAS[area]["Forca"])
        self.letras_certas = set()
        self.tentativas = 6
        self.entry.configure(state="normal")
        self.atualizar_tela()

    def atualizar_tela(self):
        exibicao = " ".join([l if l in self.letras_certas else "_" for l in self.palavra])  # noqa: E741
        self.label_palavra.configure(text=exibicao)
        self.label_status.configure(text=f"Tentativas restantes: {self.tentativas}")
        if "_" not in exibicao:
            self.label_status.configure(text="🎉 Parabéns, você venceu!", text_color="#38b000")
            self.entry.configure(state="disabled")
        elif self.tentativas == 0:
            self.label_status.configure(text=f"😢 Fim de jogo! Era '{self.palavra}'", text_color="#d90429")
            self.entry.configure(state="disabled")

    def chutar(self):
        letra = self.entry.get().lower()
        self.entry.delete(0, "end")
        if len(letra) == 1 and letra.isalpha():
            if letra in self.palavra:
                self.letras_certas.add(letra)
            else:
                self.tentativas -= 1
        self.atualizar_tela()

class FrameCacaPalavras(ctk.CTkFrame):
    def __init__(self, master, voltar):
        super().__init__(master, fg_color="#e9f5db")
        self.voltar = voltar
        self.area = None
        self.matriz = []
        self.palavras = []
        self.dicas = []
        self.encontradas = set()
        self.label = ctk.CTkLabel(self, text="Caça-palavras", font=("Comic Sans MS", 22, "bold"), text_color="#22577a")
        self.label.pack(pady=10)
        self.grid_frame = ctk.CTkFrame(self, fg_color="#b5ead7")
        self.grid_frame.pack(pady=10)
        self.label_palavras = ctk.CTkLabel(self, text="", font=("Comic Sans MS", 16), text_color="#22577a")
        self.label_palavras.pack(pady=10)
        self.label_dicas = ctk.CTkLabel(self, text="", font=("Comic Sans MS", 15), text_color="#38b000")
        self.label_dicas.pack(pady=5)
        self.entry = ctk.CTkEntry(self, font=("Comic Sans MS", 18), width=180, placeholder_text="Digite a palavra encontrada")
        self.entry.pack(pady=5)
        ctk.CTkButton(self, text="Verificar", font=("Comic Sans MS", 16), fg_color="#38b000", hover_color="#70e000", text_color="#fff", corner_radius=32, command=self.verificar_palavra).pack(pady=5)
        self.label_resultado = ctk.CTkLabel(self, font=("Comic Sans MS", 18), text_color="#22577a")
        self.label_resultado.pack(pady=10)
        ctk.CTkButton(self, text="🏠 Home", font=("Comic Sans MS", 16), fg_color="#b5ead7", hover_color="#57cc99", text_color="#22577a", corner_radius=32, command=lambda: master.mostrar_frame("Home")).pack(pady=10)
        ctk.CTkButton(self, text="⬅️ Tipos", font=("Comic Sans MS", 16), fg_color="#d1d5db", hover_color="#6b7280", text_color="#22577a", corner_radius=32, command=voltar).pack(pady=5)

    def novo_jogo(self, area):
        self.area = area
        self.encontradas = set()
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        dados = random.choice(PERGUNTAS[area]["Caça-palavras"])
        self.matriz = dados["matriz"]
        self.palavras = dados["palavras"]
        self.dicas = dados["dicas"]
        self.label_palavras.configure(text=f"Descubra as {len(self.palavras)} palavras!")
        dicas_texto = "\n".join([f"{i+1}. {dica}" for i, dica in enumerate(self.dicas[:len(self.palavras)])])
        self.label_dicas.configure(text=f"Dicas:\n{dicas_texto}")
        for i, linha in enumerate(self.matriz):
            for j, letra in enumerate(linha):
                btn = ctk.CTkButton(self.grid_frame, text=letra, width=40, height=40, font=("Comic Sans MS", 18, "bold"),
                                    fg_color="#57cc99", hover_color="#80ed99", text_color="#22577a", state="disabled")
                btn.grid(row=i, column=j, padx=2, pady=2)
        self.label_resultado.configure(text="Digite a palavra formada pelas letras e clique em Verificar.")
        self.entry.delete(0, "end")

    def verificar_palavra(self):
        palavra = self.entry.get().strip().upper()
        if palavra in self.palavras and palavra not in self.encontradas:
            self.encontradas.add(palavra)
            self.label_resultado.configure(text=f"Encontrou: {palavra}!", text_color="#38b000")
            if len(self.encontradas) == len(self.palavras):
                self.label_resultado.configure(text="Parabéns! Encontrou todas as palavras!", text_color="#38b000")
        elif palavra in self.encontradas:
            self.label_resultado.configure(text="Palavra já encontrada!", text_color="#fbbf24")
        else:
            self.label_resultado.configure(text="Não está na lista!", text_color="#d90429")
        self.entry.delete(0, "end")

if __name__ == "__main__":
    PlataformaEducativa().mainloop()