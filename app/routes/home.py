from flask import Blueprint


bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def hello():
    response_body = {
        "Name": 'Chase Ostien',
        "About": 'I am a new developer and this is a practice application'
    }

    return response_body
