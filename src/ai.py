#!/usr/bin/env python
# encoding: utf-8

import json

from google import genai
from google.genai import types
from src.personalidades import Personalidade

CLIENT = genai.Client()

INSTRUCAO_BASE1 = (
    'Você será meu adversário no xadrez e jogará de {cor}. '
    'Você sempre responderá com sua jogada e um comentário '
    'sobre o que está acontecendo no jogo. Suas '
    'respostas serão no formato JSON conforme esse exemplo: '
    '{{"movimento": "XYN", "comentario": "Seu comentário"}}\n\n '
)
INSTRUCAO_BASE2 = (
    'Quando solicitado você deverá dar dicas sobre como eu '
    'posso jogar. Suas dicas devem ser também no formato JSON, '
    'conforme exemplo: {"dica": "Sua dica"}'
)


class Bot:
    def __init__(
        self, cor: str, personalidade: Personalidade | None,
        model: str = 'gemini-2.0-flash',
    ):
        self._cor = cor
        self._model = model
        self._personalidade = personalidade
        if personalidade:
            self._system_instruction = (
                INSTRUCAO_BASE1.format(cor=cor)
                + self._personalidade.personalidade + '\n\n'
                + INSTRUCAO_BASE2
            )
        else:
            self._system_instruction = (
                INSTRUCAO_BASE1.format(cor=cor) + INSTRUCAO_BASE2
            )

        self._chat = CLIENT.chats.create(
            model=self._model,
            config=types.GenerateContentConfig(
                system_instruction=self._system_instruction
            ),
        )

    def _send(self, message: str) -> dict:
        resp = self._chat.send_message(message)
        data = resp.text.replace('```json', '').replace('```', '').strip()
        return json.loads(data)

    def pedir_dica(self):
        return self._send('Me dê uma dica')

    def informar_jogada(self, jogada: str):
        return self._send(jogada)
