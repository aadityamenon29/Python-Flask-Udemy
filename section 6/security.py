# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from models.user import UserModel
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    with open("new_test.txt", "a") as fo:
        fo.write("AUTHENTICATE\n")
    user = UserModel.find_by_username(username)
    if user is not None and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    with open("new_test.txt", "a") as fo:
        fo.write("IDENTITY\n")
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
