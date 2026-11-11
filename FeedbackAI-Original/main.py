import os
import csv
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

chave = os.getenv("chave")

cliente = genai.Client(api_key = chave)

arquivo = open("mensagens.txt", "r", encoding= "utf-8")

resultado = open("Resultado.csv", "w", encoding= "utf-8-sig", newline="")

escritor = csv.writer(resultado, delimiter=";")
escritor.writerow(["Feedback", "Categoria"])

elogios = 0
duvidas = 0
reclamações = 0
sugestões = 0
erros = 0
contador = 1

for feedback in arquivo:

    prompt = f"""
    Classifique o feedback em apenas uma categoria: Elogio, Reclamação, Sugestão ou Dúvida.

    Responda somente com o nome da categoria, sem explicações ou comentários adicionais.

    Leve em consideração perguntas retóricas, ironia e sarcasmo ao classificar o feedback.

    Feedback: {feedback}
    """

    categoria = "Erro"

    for tentativa in range(3):
        
        try:

            resposta = cliente.models.generate_content(
                model = "gemini-3.1-flash-lite",
                contents=prompt
            )

            categoria = resposta.text.strip()

            print("Entrada:", resposta.usage_metadata.prompt_token_count)
            print("Saída:", resposta.usage_metadata.candidates_token_count)
            print("Total:", resposta.usage_metadata.total_token_count)
            break

        except Exception as erro:
            print(f"Erro na tentativa {tentativa + 1} de 3.")

            if tentativa < 2:

                if "429" in str(erro):
                    print("Erro 429: Limite de requisições atingido no momento. Aguardando 45 segundos...")
                    time.sleep(45)

                else:
                    print ("Erro inesperado. Aguardando 5 segundos...")
                    time.sleep(5)

            else:
                print("Todas as tentativas falharam. Pulando mensagem.")    
                

    print(contador, "º", "Feedback:", feedback.strip())    
    print ("Classificação:", categoria)
    print("=================================")
    contador += 1


    escritor.writerow([feedback.strip(), categoria])

    if categoria == "Elogio":
        elogios += 1

    elif categoria == "Reclamação":
        reclamações += 1    

    elif categoria == "Sugestão":
        sugestões += 1

    elif categoria == "Dúvida":
        duvidas += 1

    else:
        erros += 1

    time.sleep(4.5)



arquivo.close()    
resultado.close()

total = elogios + reclamações + sugestões + duvidas + erros

if total > 0:

    print ("\n============== Estatísticas ==============")

    print(f"elogios: {elogios / total * 100:.2f}% - Quantidade de Elogios: {elogios}")
    print(f"Reclamações: {reclamações / total * 100:.2f}% - Quantidade de Reclamações: {reclamações}")
    print(f"Sugestões: {sugestões / total * 100:.2f}% - Quantidade de Sugestões: {sugestões}")
    print(f"Dúvidas: {duvidas / total * 100:.2f}% - Quantidade de Dúvidas: {duvidas}")
    print(f"Erros: {erros / total * 100:.2f}% - Quantidade de Erros: {erros}")

else:
    print("Nenhum feedback válido foi processado.")