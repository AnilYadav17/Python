import os

try:
    print("Try Block")
    os._exit(0)
finally:
    print("Finally Block")
