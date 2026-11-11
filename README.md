# FeedbackAI 🤖

Um classificador de feedbacks desenvolvido em Python, utilizando a API do Google Gemini para analisar mensagens e classificá-las automaticamente.

Como exemplo de aplicação, o projeto utiliza mensagens que simulam feedbacks de clientes de um aplicativo de entrega de comida.

<p align="center">
  <img src="https://github.com/user-attachments/assets/992ba052-3953-437c-b27d-61f911ae43ba" width="250" height="250">
  <img src="https://github.com/user-attachments/assets/64860cb0-970b-499f-b1a1-8ded594acbae" width="250" height="250">
</p>

## 📌 Sobre o projeto

O FeedbackAI tem como objetivo facilitar a análise de feedbacks de clientes por meio de inteligência artificial.

O projeto possui duas versões:

- **FeedbackAI Original:** aplicação Python executada pelo terminal, que lê mensagens de um arquivo TXT, classifica os feedbacks e gera um arquivo CSV com os resultados.
- **FeedbackAI Web:** aplicação desenvolvida com Flask, HTML, CSS e JavaScript, que permite classificar avaliações diretamente pelo navegador.

Ambas utilizam a API do Google Gemini para classificar os feedbacks em quatro categorias:

- **Elogio**
- **Reclamação**
- **Sugestão**
- **Dúvida**

O projeto também apresenta estatísticas com a quantidade e a porcentagem de avaliações de cada categoria.

## 🛠️ Tecnologias utilizadas

- Python
- Google Gemini API
- Google Gen AI SDK (`google-genai`)
- Python Dotenv (`python-dotenv`)
- Biblioteca CSV (`csv`)
- Flask
- HTML
- CSS
- JavaScript

## 🌐 FeedbackAI Web

A versão web foi desenvolvida para permitir a classificação de feedbacks por meio de uma interface simples e organizada.

Suas principais funcionalidades são:

- **Classificação individual:** permite digitar uma avaliação e receber sua classificação.
- **Upload de arquivos TXT:** permite enviar arquivos contendo várias avaliações, com uma mensagem por linha.
- **Arrastar e soltar:** permite selecionar arquivos TXT diretamente pela interface.
- **Classificação automática:** utiliza a API do Gemini para analisar cada avaliação.
- **Resumo das avaliações:** apresenta a quantidade e a porcentagem de cada categoria.
- **Filtros por categoria:** permite visualizar apenas avaliações classificadas em determinada categoria.
- **Tratamento básico de erros:** identifica falhas durante o processamento e permite continuar a classificação das demais mensagens.

As avaliações e estatísticas são armazenadas temporariamente no navegador durante a utilização da página. Ao atualizar a página, os resultados são reiniciados.

A versão Web não utiliza banco de dados e não realiza exportação de arquivos.

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/Tulio-Junho/FeedbackIA.git
cd FeedbackIA
```

### 2. FeedbackAI Original

Entre na pasta da versão original:

```bash
cd FeedbackAI-Original
```

Instale as dependências:

```bash
pip install google-genai python-dotenv
```

Crie um arquivo `.env` dentro da pasta `FeedbackAI-Original` e adicione sua chave da API:

```env
chave=sua_chave_aqui
```

Adicione os feedbacks ao arquivo `mensagens.txt`, colocando uma mensagem por linha.

Execute o programa:

```bash
python main.py
```

### 3. FeedbackAI Web

A partir da pasta principal do repositório, entre na pasta da versão Web:

```bash
cd FeedbackIA-web
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` dentro da pasta `FeedbackIA-web` e configure sua chave da API:

```env
chave=sua_chave_aqui
```

Execute a aplicação:

```bash
python app.py
```

Acesse o endereço local informado pelo Flask no terminal.

## 📊 Exemplo de resultado

Na versão original, as estatísticas são apresentadas no terminal:

```text
============== Estatísticas ==============
Elogios: 16.67% - Quantidade de Elogios: 1
Reclamações: 33.33% - Quantidade de Reclamações: 2
Sugestões: 33.33% - Quantidade de Sugestões: 2
Dúvidas: 16.67% - Quantidade de Dúvidas: 1
```

Na versão web, as estatísticas são apresentadas diretamente na interface, junto à lista de avaliações classificadas.

## 📁 Estrutura do projeto

```text
FeedbackIA/
├── FeedbackAI-Original/
│   ├── main.py
│   ├── mensagens.txt
│   └── resultado.csv
│
├── FeedbackIA-web/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   └── style.css
│   ├── requirements.txt
│   └── .gitignore
│
├── README.md
└── .gitignore
```

Cada versão utiliza seu próprio arquivo `.env`, que deve ser criado localmente e não deve ser enviado ao GitHub.

## 📄 Exportação CSV

A versão original registra os resultados no arquivo `Resultado.csv`, organizado em duas colunas:

- **Feedback:** mensagem analisada.
- **Categoria:** classificação atribuída pelo gemini.

Esse arquivo pode ser aberto em programas como o Excel.

A versão web não possui exportação CSV.

## ⚠️ Observações

O projeto depende da disponibilidade da API do Gemini e de uma chave de acesso válida. O serviço pode apresentar limitações, erros ou indisponibilidade temporária.

O processamento de arquivos txt na versão web realiza uma requisição para cada avaliação, portanto arquivos maiores podem levar mais tempo para serem classificados.

O FeedbackAI é um projeto desenvolvido para fins de estudo e aprendizado, com o objetivo de explorar a integração de inteligência artificial com Python e desenvolvimento web.

Novas melhorias poderão ser implementadas futuramente conforme o avanço dos estudos.

## 🎯 Objetivo

Praticar programação em Python, integração com APIs, manipulação de arquivos, análise básica de dados e desenvolvimento web.

A versão web também permitiu trabalhar com Flask, requisições HTTP e JavaScript, utilizando essas tecnologias para conectar a interface do usuário ao sistema de classificação por inteligência artificial.
