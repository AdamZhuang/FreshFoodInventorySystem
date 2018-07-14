import json
import signal, functools


#####################
# json转字典
#####################
def json_str_to_dict(str):
    return json.loads(str)



########################
# 超时装饰器
########################
class TimeoutError(Exception): pass

def timeout(seconds, error_message="Timeout Error: user-defined error"):
    def decorated(func):
        result = ""

        def _handle_timeout(signum, frame):
            global result
            result = error_message
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            global result
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)

            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
                return result
            return result

        return functools.wraps(func)(wrapper)

    return decorated