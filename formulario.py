def obter_resposta_pergunta(pergunta, opcoes):
    while True:
        resposta = input(f"{pergunta} ({', '.join(opcoes)}): ").strip()
        if resposta in opcoes:
            return resposta
        else:
            print("Resposta inválida. Por favor, escolha uma opção válida.")

formulario = {}

perguntas = [
    "Como você se sente hoje?",
    "Você teve febre nas últimas 24 horas?",
    "Você experienciou algúm dos seguintes sintomas (dor no peito, tosse, dor de cabeça e/ou fadiga) nas últimas 24 horas?",
    "Quantas horas de sono você teve na última noite?",
    "Você teve contato próximo com alguém que testou positivo para alguma doença transmissível recentemente?",
    "Você tomou algum medicamento nas últimas 24 horas?",
    "Você fez alguma atividade física hoje?",
    "Quantas refeições equilibradas você teve hoje?",
    "Você está se sentindo hidratado?",
    "Como está o seu nível de estresse hoje?"
]

opcoes_pergunta = {
    perguntas[0]: ["Muito bem", "Bem", "Regular", "Mal", "Muito mal"],
    perguntas[1]: ["Sim", "Não"],
    perguntas[2]: ["Sim", "Não"],
    perguntas[3]: ["Menos de 6 horas", "6-8 horas", "Mais de 8 horas"],
    perguntas[4]: ["Sim", "Não", "Não tenho certeza"],
    perguntas[5]: ["Sim", "Não"],
    perguntas[6]: ["Sim", "Não"],
    perguntas[7]: ["0-1", "2-3", "4 ou mais"],
    perguntas[8]: ["Sim", "Não"],
    perguntas[9]: ["Baixo", "Moderado", "Alto", "Muito alto"]
}

for pergunta in perguntas:
    resposta = obter_resposta_pergunta(pergunta, opcoes_pergunta[pergunta])
    formulario[pergunta] = resposta

# Exibe os resultados
print("\nRespostas do Formulário:")
for pergunta, resposta in formulario.items():
    print(f"{pergunta}: {resposta}")
