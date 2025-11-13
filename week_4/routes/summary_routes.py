import json

from fastapi import APIRouter
from logger import logger

router = APIRouter()


def read_summary(summary_path="data/summary.json"):
    try:
        with open(summary_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


@router.get('/summary')
@logger.log_call(url="/summary", method="GET")
def summary():
    return read_summary()
