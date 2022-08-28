from collections import defaultdict
from django.db.models.signals import (pre_init, post_init, pre_save, post_save,
                                      pre_delete, post_delete, pre_migrate, post_migrate)
import functools


class disable(object):
    def __init__(self, disabled_signals=None):
        self.stashed_signals = defaultdict(list)
        self.disabled_signals = disabled_signals or [
            pre_init, post_init,
            pre_save, post_save,
            pre_delete, post_delete,
            pre_migrate, post_migrate,
        ]

    def __call__(self, fn=None):
        if not fn:
            raise AttributeError('To use this decorator, instantiate it first: `@disable()`, not `@disable`')

        @functools.wraps(fn)
        def decorated(*args, **kwargs):
            self.disconnect_all()
            try:
                fn(*args, **kwargs)
            finally:
                self.reconnect_all()
        return decorated

    def __enter__(self):
        self.disconnect_all()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.reconnect_all()

    def disconnect_all(self):
        for signal in self.disabled_signals:
            self.disconnect(signal)

    def reconnect_all(self):
        for signal in self.stashed_signals:
            self.reconnect(signal)
        self.stashed_signals = defaultdict(list)

    def disconnect(self, signal):
        self.stashed_signals[signal] = signal.receivers
        signal.receivers = []

    def reconnect(self, signal):
        signal.receivers = self.stashed_signals.get(signal, [])
