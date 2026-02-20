import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Decorator that logs the execution of a function.
    Logs success (func_name ok) or error (func_name error: type. Inputs: args, kwargs).

    :param filename: Optional name of the file to write logs to.
                     If None, logs are printed to console.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_msg = f"{func.__name__} ok"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_msg + "\n")
                else:
                    print(log_msg)

                return result
            except Exception as e:
                log_msg = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_msg + "\n")
                else:
                    print(log_msg)

                raise e
        return wrapper
    return decorator
