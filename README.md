# Imersao IA Alura - xadrez-gemini-bot
Implementaçãoa simples e rápida de um bot com 3 personalidades para ser seu parceiro de xadrez. Ele faz jogadas, comenta o jogo e te dá dicas de jogo quando solicitado.

Por conta do pouco tempo disponível não foi possível implementar movimentação de peças por "arrasta e solta", e é necessário saber a notação algébrica do xadrez.

![Seleção de adversários](https://github.com/magnunleno/imersao-ia-xadrez-gemini-bot/blob/main/img/adversarios.png?raw=true)
![Personalidade 1](https://github.com/magnunleno/imersao-ia-xadrez-gemini-bot/blob/main/img/personalidade-1.png?raw=true)
![Personalidade 2](https://github.com/magnunleno/imersao-ia-xadrez-gemini-bot/blob/main/img/personalidade-2.png?raw=true)
![Personalidade 2](https://github.com/magnunleno/imersao-ia-xadrez-gemini-bot/blob/main/img/personalidade-3.png?raw=true)


## Pre-requisitos
- python 3.13
- python-chess 1.11.2
- google-genai 1.15.0
- Flask 3.1.1
- Jinja2 3.1.6
- python-dotenv 1.1.0


## Instalação

```bash
$ git clone https://github.com/magnunleno/imersao-ia-xadrez-gemini-bot.git
$ cd imersao-ia-xadrez-gemini-bot
$ python -m venv .venv
```

Ambiente Virtual no Windows:
```bash
$ .venv\Scripts\activate.bat
```

Ambiente Virtual no GNU/Linux:
```bash
$ . .venv/bin/activate
```

Instalando dependências:
```bash
$ pip install -r requirements.txt
```

## Variáveis de ambiente
```bash
$ cp .env.example .env
```

Em seguida altere a chave da API do Google.


## Rodando
Com o ambiente virtual ativado execute a seguinte linha:
```bash
$ flask run --debug
```

Em seguida acesse [http://localhost:5000](http://localhost:5000).
