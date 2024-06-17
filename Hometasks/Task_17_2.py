def upp(str):
    def wrapper(*args, **kwargs):
        val = str(*args, **kwargs)
        return val.upper()
    return wrapper()

# @upp
