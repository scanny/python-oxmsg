"""Unit-test suite for the `oxmsg.attachment` module."""

from __future__ import annotations

import datetime as dt
import hashlib

import pytest
from olefile import OleFileIO

from oxmsg.attachment import Attachment
from oxmsg.properties import Properties
from oxmsg.storage import Storage

from .unit_util import test_file_path


class DescribeAttachment:
    """Unit-test suite for `oxmsg.attachment.Attachment` objects."""

    def it_knows_whether_attachment_is_linked_or_embedded(self, attachment: Attachment):
        assert attachment.attached_by_value is True

    def it_provides_access_to_the_bytes_of_the_attached_file(self, attachment: Attachment):
        assert (file_bytes := attachment.file_bytes) is not None
        assert hashlib.sha1(file_bytes).hexdigest() == "c18fe5f2aeae76c40908a4f441d698bcb4c4b4f8"

    def it_knows_the_original_file_name_of_the_attachment(self, attachment: Attachment):
        assert attachment.file_name == "serveimage.jpg"

    def it_knows_when_the_attached_file_was_last_modified(self, attachment: Attachment):
        assert attachment.last_modified == dt.datetime(
            2020, 10, 6, 9, 57, 52, tzinfo=dt.timezone.utc
        )

    def it_knows_the_mime_type_of_the_attached_file(self, attachment: Attachment):
        assert attachment.mime_type == "image/jpeg"

    def it_provides_access_to_the_Properties_object_for_the_attachment(
        self, attachment: Attachment
    ):
        assert isinstance(attachment.properties, Properties)

    def it_knows_the_size_of_the_attachment_in_bytes(self, attachment: Attachment):
        assert attachment.size == 36739

    # -- fixtures --------------------------------------------------------------------------------

    @pytest.fixture
    def attachment(self) -> Attachment:
        with OleFileIO(test_file_path("message.msg")) as ole:
            storage = Storage.from_ole(ole)
        attachment_storage = next(storage.iter_attachment_storages())
        return Attachment(attachment_storage)
