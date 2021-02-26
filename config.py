import os


class Config:
    with open('secret_key','r') as f:
        line = f.readline()
        SECRET_KEY = line
    SECRET_KEY = os.urandom(32)
