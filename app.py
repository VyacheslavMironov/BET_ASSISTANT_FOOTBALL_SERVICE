# !/usr/bin/python 
# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

from flask_cors import CORS, cross_origin
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
    JWTManager,
    set_access_cookies
)
from flask import (
    Flask,
    make_response,
    request, 
    jsonify
)


# ------------------------------------------------
# Чтение конфигурации
# ------------------------------------------------
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
# ------------------------------------------------
# JWT генератор
# ------------------------------------------------
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)
# Отправлять только файлы cookie, содержащие ваши JWT через https.
# В продакшене для этого всегда должно быть установлено значение True
app.config["JWT_COOKIE_SECURE"] = False
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this in your code!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
# ------------------------------------------------
# Добавление заголовков передачи данных с других хостов
# ------------------------------------------------

cors = CORS(app, resources={r"/*": {"origins": "*"}}, headers='Content-Type')
app.config['CORS_HEADERS'] = 'Content-Type'


@app.after_request
def refresh_expiring_jwts(response):
    """
    Используя обратный вызов `after_request`, мы обновляем любой токен, 
    который находится в пределах 30 минут истекает. Измените временные 
    дельты в соответствии с потребностями вашего приложения.
    """
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response
    

@app.route('/api', methods=['GET'])
@cross_origin()
def home():
    return jsonify({
        'response': True, 
        'message': 'Добро пожаловать!'
    })


@app.route('/api/leagues', methods=['GET'])
@jwt_required()
@cross_origin()
def get_leagues():
    return jsonify({
        'response': True, 
        'message': 'Добро пожаловать 2'
    })


if __name__ == "__main__":
    app.run(debug=True)