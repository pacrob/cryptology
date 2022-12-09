import json
import argon2

from argon2.exceptions import (
    VerifyMismatchError,
    )

TIME_COST = 16
MEMORY_COST = 2**15
PARALLELISM = 2

users = {
        # password
        "angus": "$argon2id$v=19$m=32768,t=16,p=2$Fb3QVrmmVYtUS3hjC36Y2w$EF3CyAdw4xSyoNG/7xOGmJbpgEU9XImpNhVogeXIVwY",
        # dragon
        "bradley": "$argon2id$v=19$m=32768,t=16,p=2$jfUg1O5O70dJX1Ni5hodmw$7hvtqyVbH7o3LIuPCqH/D+LLUWUrPXqHj8R1AgFsEQ4"
}



argon2Hasher = argon2.PasswordHasher(
    time_cost=16, memory_cost=2**15, parallelism=2, hash_len=32, salt_len=16)

'''
Implement "Register User"
Input: username + password + JSON holding all current accounts.
Output: modified JSON file or "user exists" exception.
'''
def register_user(username, password):

    if username in users.keys():
        raise Exception("user name exists")

    user_hash = argon2Hasher.hash(password)
    users[username] = user_hash

    print("user added")
    print(f"current users: {users}")

    
'''
Implement "User Login"
Input: username + password + JSON holding all current accounts.
Output: correct / incorrect login.
'''
def user_login(username, password):

    if username not in users.keys():
        return "incorrect login"

    try:
        pwd_correct = argon2Hasher.verify(users[username], password)
    except VerifyMismatchError as err:
        return "incorrect login"

    if pwd_correct:
        return "you're in!" 

    else:
        return "i don't know what happened"
'''
Implement "Change Password"
Input: username + old password + new password + JSON holding all current accounts.
Output: modified JSON file or "user exists" exception.
'''
# TODO
'''
Implement "Reset Password"
Input: username + new password + JSON holding all current accounts.
Output: modified JSON file or "user exists" exception.
'''
# TODO


