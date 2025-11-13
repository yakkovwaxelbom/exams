from fastapi import APIRouter

from ciphers.caesar import Caesar
from logger import logger
from models import RequestsCaesar

router = APIRouter()


def get_caesar(text, offset, mode):
    res = None
    if mode == 'encrypt':
        res = Caesar.encode(text, offset)
    elif mode == 'decrypt':
        res = Caesar.decode(text, offset)
    return {mode + '_text': res}


@router.post('/caesar')
@logger.log_call(url="/caesar", method="POST")
def caesar(body: RequestsCaesar):
    return get_caesar(body.text, body.offset, body.mode)
