import sentry_sdk

z = 1234

sentry_sdk.init("http://public@localhost:5000/2")


def gen_error():
    x = get_x()
    y = get_y()
    z = x / y
    print(z)


def get_x():
    return 100


def get_y():
    return 0


gen_error()
