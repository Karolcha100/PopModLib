import importlib
import pkgutil

_subpackages = {name for _, name, is_pkg in pkgutil.iter_modules(__path__) if is_pkg}

def __getattr__(name):
    if name in _subpackages:
        module = importlib.import_module(f"{__name__}.{name}")
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

def __dir__():
    return sorted(list(globals().keys()) + list(_subpackages))
