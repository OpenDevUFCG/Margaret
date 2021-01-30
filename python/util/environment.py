from os import environ as env

default = {
    "PORT": 80,
    "HOST": "0.0.0.0"
}

def get_env(var_name):
    if var_name in env:
        return env[var_name]

    if var_name in default:
        return default[var_name]

    return None
