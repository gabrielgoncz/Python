# Lista de perguntas. Cada pergunta é um dicionário.
perguntas = [
    {
        "pergunta": "Qual é a capital da França?",
        "opcoes": ["A) Madrid", "B) Paris", "C) Berlim", "D) Lisboa"],
        "resposta": "B"
    },
    {
        "pergunta": "Quantos planetas existem no Sistema Solar?",
        "opcoes": ["A) 7", "B) 8", "C) 9", "D) 10"],
        "resposta": "B"
    },
    {
        "pergunta": "Quem pintou a Mona Lisa?",
        "opcoes": ["A) Van Gogh", "B) Picasso", "C) Leonardo da Vinci", "D) Monet"],
        "resposta": "C"
    },
    {
            "pergunta": "Quantos meses tem 1 Ano?",
            "opcoes": ["A) 8", "B) 10", "C) 9", "D) 12"],
            "resposta": "D"
        },
        {
                "pergunta": "Como é chamado quem tem habilidade de entender 2 líguas distintas?",
                "opcoes": ["A) Poliglota", "B) Bílingue", "C) Trílingue", "D) Analfabeto"],
                "resposta": "B"
            }
]

pontuacao = 0

print("=== BEM-VINDO AO QUIZ PYTHON ===\n")

# Loop para rodar cada pergunta
for i, p in enumerate(perguntas, 1):
    print(f"Pergunta {i}: {p['pergunta']}")
    
    # Mostra as opções de resposta
    for opcao in p["opcoes"]:
        print(opcao)
        
    # Pede a resposta do usuário e padroniza para maiúscula
    resposta_usuario = input("Sua resposta (A, B, C ou D): ").strip().upper()
    
    # Valida se a resposta está correta
    if resposta_usuario == p["resposta"]:
        print("✨ Correto!\n")
        pontuacao += 1
    else:
        print(f"❌ Errado! A resposta correta era a letra {p['resposta']}.\n")

# Resultado final
print("================================")
print(f"Fim do jogo! Você acertou {pontuacao} de {len(perguntas)} perguntas.")
print("================================")
