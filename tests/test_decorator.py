from __future__ import absolute_import
from .models import CustomModel, PostSaveCalled
import pytest
import signal_disabler


def test_as_decorator(db):
    obj = CustomModel()

    @signal_disabler.disable()
    def save():
        obj.save()

    with pytest.raises(PostSaveCalled):
        obj.save()

    save()

    with pytest.raises(PostSaveCalled):
        obj.save()


def test_fail_as_uninstantiated_decorator(db):
    obj = CustomModel()

    @signal_disabler.disable
    def save():
        obj.save()

    with pytest.raises(AttributeError):
        save()


def test_signals_reconnected_after_exception(db):
    obj = CustomModel()

    @signal_disabler.disable()
    def fails():
        raise Exception

    try:
        fails()
    except:
        pass

    with pytest.raises(PostSaveCalled):
        obj.save()

