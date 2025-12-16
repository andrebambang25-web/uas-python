import sqlite3
import os

def get_connection():
    if not os.path.exists("data"):
        os.makedirs("data")
    return sqlite3.connect("data/esport.db")
