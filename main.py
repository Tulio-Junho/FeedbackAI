import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

chave = os.getenv("chave")

cliente = genai.Client(api_key = chave)

arquivo = open("mensagens.txt", "r", encoding= "utf-8")

resultado = open("resultado.csv", "w", encoding= "utf-8")


elogios = 0
duvidas = 0
reclamações = 0
sugestões = 0

for feedback in arquivo:

    prompt = f"""
    Classifique o feedback em apenas uma categoria: Elogio, Reclamação, Sugestão ou Dúvida.

    Responda somente com o nome da categoria, sem explicações ou comentários adicionais.

    Feedback: {feedback}
    """

    resposta = cliente.models.generate_content(
        model = "gemini-3.5-flash-lite",
        contents=prompt
    )

    print("Feedback:", feedback.strip())    
    print ("Classificação:", resposta.text)
    print("=================================")

    categoria = resposta.text.strip()
    resultado.write(f"{feedback.strip()} -> {categoria}\n")

    if categoria == "Elogio":
        elogios += 1

    elif categoria == "Reclamação":
        reclamações += 1    

    elif categoria == "Sugestão":
        sugestões += 1

    elif categoria == "Dúvida":
        duvidas += 1


arquivo.close()    
resultado.close()

print ("\n============== Resumo das Classificações ==============")

print("Elogios:" , elogios)
print("Reclamações:" , reclamações)
print("Sugestões:" , sugestões)
print("Dúvidas:" , duvidas)


