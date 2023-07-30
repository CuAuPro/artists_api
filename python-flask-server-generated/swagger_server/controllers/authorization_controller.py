from typing import List
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
PASSWD = {"admin": "secret", "foo": "bar"}

def check_BasicAuth(username, password, required_scopes):
    if PASSWD.get(username) == password:
        return {"sub": username}
    # optional: raise exception for custom error response
    return None


