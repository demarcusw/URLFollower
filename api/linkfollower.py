import requests
import re

from constants import REDIRECT_CODES, META_REFRESH_REGEX

def follow(url: str):
    pass

def is_redirect(status_code: int) -> bool:
    return status_code in REDIRECT_CODES

def find_meta_refresh(html: str):
    m = re.match(META_REFRESH_REGEX, html)