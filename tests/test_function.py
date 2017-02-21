from __future__ import absolute_import
from .models import CustomModel, PostSaveCalled
import pytest
import signal_disabler


def test_function(db):
    disabler = signal_disabler.disable()
    obj = CustomModel()

    with pytest.raises(PostSaveCalled):
        obj.save()

    disabler.disconnect_all()
    obj.save()
    disabler.reconnect_all()

    with pytest.raises(PostSaveCalled):
        obj.save()
