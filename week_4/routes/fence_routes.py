from fastapi import APIRouter

from ciphers.fence import Fence
from logger import logger
from models import RequestsFence

router = APIRouter()


def get_fence(text, key, mode):
    res = None
    if mode == 'encrypt':
        res = Fence.encode(text, key)
    elif mode == 'decrypt':
        res = Fence.decode(text, key)
    return {mode + '_text': res}


@router.get('/fence/encrypt')
@logger.log_call(url="/fence/encrypt", method="GET")
def fence_encrypt(text: str, key: int = 2):
    return get_fence(text, key, 'encrypt')


@router.post('/fence/decrypt')
@logger.log_call(url="/fence/decrypt", method="POST")
def fence_decrypt(body: RequestsFence):
    return get_fence(body.text, 2, 'decrypt')
