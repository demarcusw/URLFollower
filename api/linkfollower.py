import requests
import re

from constants import REDIRECT_CODES

def follow(url: str):
    pass

def is_redirect(status_code: int) -> bool:
    return status_code in REDIRECT_CODES

