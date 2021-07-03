# -*- coding: utf-8 -*-
from base64 import b64decode


def atob(s):
    res = b64decode(s)
    return res.decode()
