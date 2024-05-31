"""Unit-test suite for the `oxmsg.recipient` module."""

from __future__ import annotations

import pytest
from olefile import OleFileIO

from oxmsg.properties import Properties
from oxmsg.recipient import Recipient
from oxmsg.storage import Storage

from .unit_util import test_file_path


class DescribeRecipient:
    """Unit-test suite for `oxmsg.recipient.Recipient` objects."""

    def it_knows_the_recipient_email_address(self, recipient: Recipient):
        assert recipient.email_address == "arne.moehle@tutao.onmicrosoft.com"

    def it_knows_the_recipient_name(self, recipient: Recipient):
        assert recipient.name == "Arne Möhle"

    def it_provides_access_to_the_Properties_object_for_the_recipient(self, recipient: Recipient):
        assert isinstance(recipient.properties, Properties)

    # -- fixtures --------------------------------------------------------------------------------

    @pytest.fixture
    def recipient(self) -> Recipient:
        with OleFileIO(test_file_path("message.msg")) as ole:
            storage = Storage.from_ole(ole)
        recipient_storage = next(storage.iter_recipient_storages())
        return Recipient(recipient_storage)
