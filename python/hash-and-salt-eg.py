# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 22:37:35 2023
@author: Ye Kyaw Thu, LST, NECTEC, Thailand
"""

import hashlib
import os
import json
import time
import getpass

# This is our "database" of users
USER_DATA = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
}

def create_salted_hash(password, salt=None):
    if salt is None:
        # Generate a random salt
        salt = os.urandom(16)
    # Create the salted hash
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt, hashed_password

def save_user_data(filename):
    salted_hashes = {}
    for username, password in USER_DATA.items():
        salt, salted_hash = create_salted_hash(password)
        salted_hashes[username] = {
            'salt': salt.hex(),
            'hash': salted_hash.hex()
        }
    with open(filename, 'w') as f:
        json.dump(salted_hashes, f)

def load_user_data(filename):
    with open(filename, 'r') as f:
        salted_hashes = json.load(f)
    return salted_hashes

def login_user(username, salted_hashes):
    for i in range(3):
        password = getpass.getpass("Enter your password: ")
        salt = bytes.fromhex(salted_hashes[username]['salt'])
        entered_hash = create_salted_hash(password, salt)[1]
        stored_hash = bytes.fromhex(salted_hashes[username]['hash'])
        if entered_hash == stored_hash:
            print("Login successful!")
            return
        else:
            print("Incorrect password.")
    print("Too many failed attempts. Try again later.")
    time.sleep(600)

def main():
    save_user_data('user_data.json')
    salted_hashes = load_user_data('user_data.json')
    username = input("Enter your username: ")
    if username in salted_hashes:
        login_user(username, salted_hashes)
    else:
        print("User not found.")

if __name__ == "__main__":
    main()
