from importlib import import_module
import pkgutil







for _, name, is_pkg in pkgutil.iter_modules(__path__):
    if is_pkg:
        module = import_module(f"{__name__}.{name}")
        globals()[name] = module

