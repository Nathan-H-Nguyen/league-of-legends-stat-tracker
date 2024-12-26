from flask import render_template, request
from . import lol_bp

@lol_bp.route('/', methods=['POST', 'GET'])
def lol_home():
    # Need to somehow get information that can link to their puuid
    if request.method == 'POST':
        game_name = request.form('game_name')
        tag_line = request.form('tag_line')