django-disable-signals
======================
A small utility package for temporarily disabling django signals

Installation
------------
`pip install django-signal-disabler`

Usage
-----
There are three ways to use this package:
1. As a function:
```python
disabler = signal_disabler.disable()
obj = Model()

disabler.disconnect_all()
obj.save()  # will not call any signals
disabler.reconnect_all()
```

2. As a context manager
```python
obj = Model()

with signal_disabler.disable():
    obj.save()  # will not call any signals
```

3. As a decorator
```python
@signal_disabler.disable():
def save(obj)
    obj.save()

save(Model())  # will not call any signals
```
