from __future__ import print_function

from eyex.api import EyeXInterface

eye_api = EyeXInterface()

eye_api.on_event += [lambda x: print(x)]

while True:
    pass