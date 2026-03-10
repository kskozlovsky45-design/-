from typing import Union, List, Dict, Any

def function_name(search: str, status: bool, *args: Any, **kwargs: Any) -> Union[List[int], str]:
    result_list: List[int] = []  # для целых чисел
    result_str: str = ""  # для строки

    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result_list.append(i)
            return result_list
        else:
            for i in args:
                result_str += f"{i}"
            return result_str
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_str += f"Key: {k}, Value: {v}"
        return result_str
    else:
        raise ValueError("Недопустимое значение search")

print(function_name("args", True, 1, 2, 3, "hello", 4))
print(function_name("args", False, 1, 2, 3, "hello"))
print(function_name("kwargs", False, a=1, b=2, c=3))