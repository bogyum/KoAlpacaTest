from fastapi import FastAPI
from KoAlpacaFunc import ask

app = FastAPI() # FastAPI 객체 생성

def get_answer(prompt):
    output = ask(prompt)
    return output


@app.get('/')
def root():
    return {'message': 'Hello User!'}


@app.post('/chat')
def test(param: dict={}):
    user_message = param.get('user_message', '')
    return {'message': get_answer(user_message)}