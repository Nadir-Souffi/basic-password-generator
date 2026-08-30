import random
import string
import tkinter as tk

def generate_password(length=16):
    lowercases="abcdefghijklmnopqrstuvwxyz"
    upercases=lowercases.upper()
    symbols = r"""`~!@#$%^&*()_+{}|:"<>?-=[]\;',./"""
    numbers="0123456789"
    all_char=lowercases+upercases+symbols+numbers
    password="".join(random.choice(all_char) for _ in range(length))
    return password
 
print(generate_password())


