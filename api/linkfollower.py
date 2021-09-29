import requests
from constants import MAX_REDIRECT_DEPTH, REDIRECT_CODES, UA


def is_redirect(status_code: int) -> bool:
    return status_code in REDIRECT_CODES


def follow(url: str) -> dict:
    headers = {
        'User-Agent': UA,
        'Accept': 'text/html'
    }

    resp = requests.get(url, allow_redirects=False, headers=headers)
    print(f'Status code is: {resp.status_code}')
    if is_redirect(resp.status_code):
        loc = resp.headers.get('location')
        if not loc:
            raise Exception(
                f'{url} returned {resp.status_code} but no location header...')

        return {'OriginalURL': url, 'Redirect': True, 'Status': resp.status_code, 'RedirectLocation': loc}
    else:
        return {'OriginalURL': url, 'Redirect': False, 'Status': resp.status_code}


def go_follow(url: str) -> list:
    results = []
    count = 1
    keep_going = True

    while keep_going:
        if count > MAX_REDIRECT_DEPTH:
            raise Exception("Exceeded maximum redirect depth")

        try:
            resp = follow(url)
            count += 1
            results.append(resp)
            keep_going = resp.get('Redirect')
            url = resp.get('RedirectLocation')
        except Exception as e:
            keep_going = False
            failed = {'OriginalURL': url,
                      'Redirect': False, 'Status': f'Error: {e}'}
            results.append(failed)

    return results
