# -- coding: utf-8 --

import sys

if sys.platform == 'windows':  # CHECK ENVIRONMENT
    print("Perfecto estoy en el entorno adecuado")
    pass
else:
    print("This script is intended to run only on Windows, Detected platform: ", sys.platform)
    sys.exit("Failed")
