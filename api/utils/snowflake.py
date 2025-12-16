from os import getpid
from time import time

def snowflake_id(entity=0):
    worker = getpid() % 4096 
    ts = int(time() * 1000)
    return (ts << 22) | (entity << 17) | (worker << 12)
