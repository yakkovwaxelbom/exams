from fastapi import APIRouter
from logger import logger

router = APIRouter()


def write_name(name):
    with open('data/names.txt', 'a') as f:
        f.write(name + '\n')
        f.flush()


@router.get('/test')
@logger.log_call(url="/test", method="GET")
def test():
    return {"msg": "hi from test"}


@router.get('/test/{name}')
@logger.log_call(url="/test/{name}", method="GET")
def test_name(name: str):
    write_name(name)
    return {"msg": "saved user"}
