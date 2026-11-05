# FeedbackAI 🤖

Um classificador de feedbacks desenvolvido em Python, utilizando a API do Google Gemini para analisar mensagens e classificá-las automaticamente. No exemplo que usei no código, mensagens como se fosse em um aplicativo de entrega de comida.

<p align="center">
  <img src="https://github.com/user-attachments/assets/64860cb0-970b-499f-b1a1-8ded594acbae" width="250">
  <img src="(https://github.com/user-attachments/assets/992ba052-3953-437c-b27d-61f911ae43ba)" width="250">
</p>


## 📌 Sobre o projeto

O FeedbackAI tem como objetivo facilitar a análise de feedbacks de clientes por meio de inteligência artificial.

O programa lê mensagens armazenadas em um arquivo `.txt` e utiliza um modelo de linguagem (LLM) para classificá-las em quatro categorias:

- **Elogio**
- **Reclamação**
- **Sugestão**
- **Dúvida**

Ao final, o programa apresenta um resumo com a quantidade de mensagens de cada categoria e gera um arquivo CSV com os resultados.

## 🛠️ Tecnologias utilizadas

- Python
- Google Gemini API
- Google Gen AI SDK (`google-genai`)
- Python Dotenv (`python-dotenv`)

## ⚙️ Como executar

1. Clone o repositório.
2. Instale as dependências:

   ```bash
   pip install google-genai python-dotenv
   ```

3. Crie um arquivo `.env` na pasta do projeto e adicione sua chave da API:

   ```env
   GEMINI_API_KEY=sua_chave_aqui
   ```

4. Adicione os feedbacks ao arquivo `mensagens.txt`, colocando uma mensagem por linha.
5. Execute o programa:

   ```bash
   python main.py
   ```

## 📊 Exemplo de resultado

```text
Feedback: O atendimento foi excelente!
Classificação: Elogio
=================================
Feedback: Meu pedido chegou atrasado.
Classificação: Reclamação
=================================

============== Resumo das classificações ==============
Elogios: 1
Reclamações: 1
Sugestões: 0
Dúvidas: 0
```

Os resultados também são registrados no arquivo `resultado.csv`.

## 📁 Estrutura do projeto

```text
FeedbackAI/
├── main.py
├── mensagens.txt
├── README.md
├── .gitignore
└── .env (arquivo local, não publicado)
```

O arquivo `resultado.csv` é gerado durante a execução do programa.

## ⚠️ Observações

O projeto depende da disponibilidade da API do Gemini e de uma chave de acesso válida. Ou seja, o serviço pode apresentar limitações ou indisponibilidade temporária, por conta por exemplo de demandas altas no momento.

## 🎯 Objetivo

Projeto desenvolvido para praticar programação em Python, integração com APIs e aplicação de modelos de inteligência artificial em um problema prático.
