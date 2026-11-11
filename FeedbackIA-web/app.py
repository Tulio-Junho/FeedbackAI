import os
from dotenv import load_dotenv
from google import genai
from flask import Flask, render_template, request

load_dotenv()

chave = os.getenv("chave")
cliente = genai.Client(api_key=chave)

app = Flask(__name__)

@app.route('/')
def inicio():
    return  render_template("index.html")

@app.route("/Classificar", methods=["POST"])
def classificar():
    mensagem = request.get_data(as_text=True)

    if(mensagem.strip() == ""):
        return "Nenhuma mensagem recebida!"

    else:
        print("Mensagem recebida:", mensagem)

        prompt = f"""
        Classifique os feedbacks recebidos.

        Analise a mensagem e classifique-a em apenas em uma das categorias:
        Elogio, Reclamação, Dúvida ou Sugestão.

        Darei um "guia" para cada categoria:

        Elogio: mensagem que expressa satisfação, aprovação ou reconhecimento positivo.
        Reclamação: mensagem que expressa insatisfação, crítica ou relata um problema.
        Dúvida: mensagem que solicita informações, esclarecimentos ou faz uma pergunta real.
        Sugestão: mensagem que propõe melhorias, mudanças ou novas funcionalidades.

        Algumas regras que devem ser seguidas:

        Não classifique mensagens apenas por palavras isoladas, apenas se for bom, ruim, etc
        Considere o contexto e a intenção da mensagem.
        Perguntas retóricas devem ser classificadas conforme sua intenção, e não automaticamente como Dúvida.
        Mensagens incompletas ou sem intenção identificável não devem receber uma categoria.
        Caso a mensagem não se encaixe claramente em nenhuma categoria, responda "Mensagem não identificada.".
        Se houver mais de uma intenção, escolha a categoria predominante.
        Responda somente com o nome da categoria ou "Mensagem não identificada.", sem explicações adicionais.


        Feedback: {mensagem}
        """

        resposta = cliente.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt,

        )

        return resposta.text.strip()

if __name__ == "__main__":
    app.run(debug=True)
