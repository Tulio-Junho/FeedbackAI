# FeedbackAI 🤖

Um classificador de feedbacks desenvolvido em Python, utilizando a API do Google Gemini para analisar mensagens e classificá-las automaticamente. Como exemplo de aplicação, o projeto utiliza mensagens que simulam feedbacks de clientes de um aplicativo de entrega de comida.

<p align="center">
  <img src="https://github.com/user-attachments/assets/992ba052-3953-437c-b27d-61f911ae43ba" width="250", height="250">
  <img src="https://github.com/user-attachments/assets/64860cb0-970b-499f-b1a1-8ded594acbae" width="250", height="250">
</p>


## 📌 Sobre o projeto

O FeedbackAI tem como objetivo facilitar a análise de feedbacks de clientes por meio de inteligência artificial.

O programa lê mensagens armazenadas em um arquivo `.txt` e utiliza um modelo de linguagem para classificá-las em quatro categorias:

- **Elogio**
- **Reclamação**
- **Sugestão**
- **Dúvida**

Ao final, o programa apresenta estatísticas com a quantidade e a porcentagem de mensagens de cada categoria, além de gerar um arquivo CSV estruturado, compatível com o Excel, contendo os resultados.

## 🛠️ Tecnologias utilizadas

- Python
- Google Gemini API
- Google Gen AI SDK (`google-genai`)
- Python Dotenv (`python-dotenv`)
- Biblioteca csv (`csv`)

## ⚙️ Como executar

1. Clone o repositório.
2. Instale as dependências:

   ```bash
   pip install google-genai python-dotenv
   ```

3. Crie um arquivo `.env` na pasta do projeto e adicione sua chave da API:

   ```env
   chave=sua_chave_aqui
   ```

4. Adicione os feedbacks ao arquivo `mensagens.txt`, colocando uma mensagem por linha.
5. Execute o programa:

   ```bash
   python main.py
   ```

## 📊 Exemplo de resultado

```text
============== Estatísticas ==============
elogios: 16.67% - Quantidade de Elogios: 1
Reclamações: 33.33% - Quantidade de Reclamações: 2
Sugestões: 33.33% - Quantidade de Sugestões: 2
Dúvidas: 16.67% - Quantidade de Dúvidas: 1
```

Os resultados também são registrados no arquivo `resultado.csv`.

## 📁 Estrutura do projeto

```text
FeedbackAI/
├── main.py
├── mensagens.txt
├── README.md
├── .gitignore
├── resultado.csv (gerado automaticamente)
└── .env (arquivo local, não publicado)
```

O arquivo `resultado.csv` é gerado durante a execução do programa.

## 📄 Exportação CSV 

Os resultados também são registrados no arquivo `resultado.csv`,
organizados em duas colunas: **Feedback** e **Categoria**

🌐 FeedbackAI Web

O projeto também possui uma extensão chamada FeedbackAI Web, desenvolvida com Flask, HTML, CSS e JavaScript.

Diferentemente da versão original, que lê mensagens de um arquivo .txt, a versão Web permite que o usuário digite e envie um feedback individualmente, recebendo sua classificação diretamente no navegador por meio da API do Google Gemini.

## ⚠️ Observações

O projeto depende da disponibilidade da API do Gemini e de uma chave de acesso válida. Ou seja, o serviço pode apresentar limitações ou indisponibilidade temporária, por conta por exemplo de demandas altas no momento.

O FeedbackAI é um projeto acadêmico desenvolvido exclusivamente para fins de estudo e aprendizado, com o objetivo de explorar a integração de inteligência artificial com Python.

O projeto ainda está em desenvolvimento, e novas atualizações e funcionalidades poderão ser implementadas futuramente, conforme o avanço dos estudos e o aprimoramento da aplicação.

## 🎯 Objetivo

Praticar programação em Python, integração com APIs, manipulação de arquivos, análise básica de dados e aplicação de modelos de inteligência artificial na resolução de problemas práticos.