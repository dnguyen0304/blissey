# Introduction
This document adheres to the specifications outlined in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

## Version Control
### Commit Messages
- Issue IDs **should** be included.
```
# YES
git commit --message "PROJECT-1: foo"

# No
git commit --message "foo"
```

### General
- Documentation **must** adhere to the [NumPy / SciPy specifications](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt).
- Packages **should** have `__all__` indices in their `__init__.py`.
- `__all__` indices **should** be sorted alphabetically.
- Modules **should not** have `__all__` indices.
- Modules **must** be named with an object type suffix. An exception is with Models. Model modules **must not** be named with an object type suffix.
```
# YES
/foos
    - eggs_foo.py
    - ham_foo.py

/models
    - eggs.py
    - ham.py

# No
/foos
    - eggs.py
    - ham.py

/models
    - eggs_model.py
    - ham_model.py
```
- Package base classes **must** be named with a "Base" prefix.
```
# YES
class BaseFoo:
    pass

# No
class Foo:
    pass
```
- Classes **must** follow the same naming conventions as modules.
- Classes **should** implement `__repr__()` methods.
- Methods intended for subclassing (i.e. stub methods) **could** be named `do_<method_name>()`.
- Functions or methods intended for facilitating testing **could** be named `help_<function_or_method_name>()`.
- Logging **should** be done in the Controllers.
