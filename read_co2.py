import mh_z19
from time import datetime


def read():
    co2 = mh_z19.read()
    now_time = datetime.datetime.now()
    time_str = now_time.strftime("%Y-%m-%d %H-%M-%S.%f")

    return time_str, co2