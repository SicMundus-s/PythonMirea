import inspect


def func(func_to_inspect):
    func_name = func_to_inspect.__name__

    signature = inspect.signature(func_to_inspect)

    param_info = []
    for param_name, param in signature.parameters.items():
        param_type = param.annotation
        if param_type is inspect.Parameter.empty:
            param_type = "не указан"

        if param.default is param.empty:
            param_info.append(f"{param_name} ({param_type})")
        else:
            param_info.append(f"{param_name} ({param_type}, по умолчанию {param.default})")

    print(f"Имя функции: {func_name}")
    print(f"Параметры функции: {', '.join(param_info)}")


def subfunc(x: int, y: float):
    pass


func(subfunc)