django-disable-signals
======================
[![travis](https://travis-ci.org/RobertKolner/django-signal-disabler.svg?branch=master)](https://travis-ci.org/RobertKolner/django-signal-disabler)
[![codecov](https://codecov.io/gh/RobertKolner/django-signal-disabler/branch/master/graph/badge.svg)](https://codecov.io/gh/RobertKolner/django-signal-disabler)

A small utility package for temporarily disabling django signals

Installation
------------
`pip install django-signal-disabler`

Usage
-----
There are multiple ways to use this package:

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
    @signal_disabler.disable()  # note the parenthesis
    def save(obj)
        obj.save()

    save(Model())  # will not call any signals
    ```

Limitations
-----------
Not all signals are disabled. The default includes:

- `pre_init`, `post_init`
- `pre_save`, `post_save`
- `pre_delete`, `post_delete`
- `pre_migrate`, `post_migrate`

To disable other signals, one has to provide their list when instantiating disabler. Let's say we
have a signal called `email_sent`. To disable it use:

```python
email = Email()
with signal_disabler.disable(email_sent):
    email.send()
```