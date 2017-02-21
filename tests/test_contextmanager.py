from __future__ import absolute_import
from .models import CustomModel, PostSaveCalled
import pytest
import signal_disabler


def test_as_context_manager(db):
    obj = CustomModel()

    with pytest.raises(PostSaveCalled):
        obj.save()

    with signal_disabler.disable():
        obj.save()

    with pytest.raises(PostSaveCalled):
        obj.save()
