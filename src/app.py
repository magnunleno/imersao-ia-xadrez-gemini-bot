#!/usr/bin/env python
# encoding: utf-8

import os
import chess
import chess.svg

from dotenv import load_dotenv
from flask import Flask, render_template, request, send_from_directory

from src.ai import Bot
from src.personalidades import PERSONALIDADES, MAP_PERSONALIDADES

load_dotenv()
app = Flask(__name__)
board = chess.Board()
BOT = None
JOGADAS = []
PERSONALIDADE = None


def reset_all():
    global BOT
    global JOGADAS
    BOT = Bot('negras', personalidade=PERSONALIDADE)
    JOGADAS = []
    board.reset()


@app.route('/')
def get_root():
    global BOT
    if BOT is None:
        BOT = Bot('negras', personalidade=PERSONALIDADE)
    return render_template('index.html')


@app.route('/reset')
def get_reset():
    reset_all()
    return ''


@app.route('/board')
def get_board():
    return chess.svg.board(board, size=500)


@app.route('/jogada', methods=['POST', 'GET'])
def post_jogada():
    if request.method == 'POST':
        global JOGADAS
        if 'jogada' not in request.json:
            return {'success': False, 'message': 'Informe um movimento'}
        jogada_san = request.json['jogada']
        pos = len(JOGADAS) + 1
        JOGADAS.append((pos, jogada_san))
        try:
            jogada = board.parse_san(jogada_san)
            if jogada in board.legal_moves:
                board.push(jogada)
                movimento_bot = BOT.informar_jogada(jogada_san)
                jogada_bot_san = movimento_bot['movimento']
                pos = len(JOGADAS) + 1
                JOGADAS.append((pos, jogada_bot_san))
                jogada_bot = board.parse_san(jogada_bot_san)
                board.push(jogada_bot)

        except chess.InvalidMoveError:
            return {'success': False, 'message': 'Movimento inválido'}
        except chess.IllegalMoveError:
            return {'success': False, 'message': 'Movimento ilegal'}
        except chess.AmbiguousMoveError:
            return {'success': False, 'message': 'Movimento ambiguo'}
        except ValueError as e:
            print(e)
            return {'success': False, 'message': 'Erro ao mover'}
        return {
            'success': True, 'message': 'Movimento realizado com sucesso',
            'bot': movimento_bot,
        }

    return {'jogadas': JOGADAS}


@app.route('/dica')
def get_dica():
    return BOT.pedir_dica()


@app.route('/jogadores', methods=['GET', 'POST'])
def get_jogadores():
    if request.method == 'POST':
        if 'personalidade' not in request.json:
            return {'success': False, 'message': 'Informe uma personalidade'}
        personalidade_id = request.json['personalidade']
        global PERSONALIDADE
        PERSONALIDADE = MAP_PERSONALIDADES[personalidade_id]
        reset_all()
        return {
            'message': 'Personalidade selecionada.',
            'personalidade': PERSONALIDADE.to_dict(),
        }

    personalidades = []
    for p in PERSONALIDADES:
        personalidades.append(p.to_dict())

    return {
        'personalidades': personalidades,
        'selecionado': (
            None if PERSONALIDADE is None else PERSONALIDADE.to_dict()
        ),
    }


@app.route('/avatars/<path:path>')
def send_avatar(path):
    return send_from_directory('avatars', path)
