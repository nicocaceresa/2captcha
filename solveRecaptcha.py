import os
from twocaptcha import TwoCaptcha


def solveRecaptcha(sitekey, url):
    solver = TwoCaptcha('6fb9ea7a06972a82eb9fa0c432dd033e')

    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url=url)

    except Exception as e:
        print(e)

    else:
        return result