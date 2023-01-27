import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

# in this example we store the API key inside environment variables that can be set like:
# export APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Linux or macOS
# set APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Windows
# you can just set the API key directly to it's value like:
# api_key="1abc234de56fab7c89012d34e56fa7b8"

api_key = os.getenv('1abc234de56fab7c89012d34e56fa7b8', '6fb9ea7a06972a82eb9fa0c432dd033e')


config = {
            'server':           '2captcha.com', # can be also set to 'rucaptcha.com'
    		'apiKey':           api_key,
    		'softId':            123,
    		'callback':         'https://secure.similarweb.com/account/login?returnUrl=%2fm', # if set, sovler with just return captchaId, not polling API for the answer
    		'defaultTimeout':    120,
    		'recaptchaTimeout':  600,
    		'pollingInterval':   10,
	    }

solver = TwoCaptcha(**config)

try:
    result = solver.recaptcha(
        sitekey='6Ld9tP8SAAAAAKgr5QDjmeSkBXDIIy6aDRFdgYa8',
        url='https://secure.similarweb.com/account/login?returnUrl=%2fm',
        version='v3',
        enterprise=0,
        action='verify',
        score=0.7
#        proxy={
#            'type': 'HTTPS',
#            'uri': 'login:password@IP_address:PORT'
#        }
        )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))