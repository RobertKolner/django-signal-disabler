from __future__ import absolute_import
from .models import CustomModel, PostSaveCalled
import pytest


def test_configuration(db):
    """This is merely a smoke test. If this fails, something is really wrong."""
    obj = CustomModel()
    with pytest.raises(PostSaveCalled):
        obj.save()
