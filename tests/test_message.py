# pyright: reportPrivateUsage=false

"""Unit-test suite for the `oxmsg.message` module."""

from __future__ import annotations

import datetime as dt

import pytest

from oxmsg.attachment import Attachment
from oxmsg.message import Message
from oxmsg.properties import Properties
from oxmsg.recipient import Recipient
from oxmsg.storage import Storage

from .unit_util import test_file_path


class DescribeMessage:
    """Unit-test suite for `oxmsg.message.Message` objects."""

    def it_can_load_from_a_file_path(self):
        msg = Message.load(test_file_path("message.msg"))

        assert isinstance(msg, Message)
        assert isinstance(msg._storage, Storage)

    def but_it_raises_when_no_file_is_present_at_the_file_path(self):
        with pytest.raises(FileNotFoundError, match="No such file or directory"):
            Message.load(test_file_path("no-such-file-at-this-path.msg"))

    def and_it_raises_when_the_file_is_not_a_MSG_file(self):
        with pytest.raises(ValueError, match="not-a-MSG-file.msg is not an Outlook MSG file"):
            Message.load(test_file_path("not-a-MSG-file.msg"))

    def it_can_load_from_a_file_like_object(self):
        with open(test_file_path("message.msg"), "rb") as f:
            msg = Message.load(f)

        assert isinstance(msg, Message)
        assert isinstance(msg._storage, Storage)

    def but_it_raises_when_the_file_like_object_does_not_contain_a_MSG_file(self):
        with pytest.raises(ValueError, match="msg_file is not an Outlook MSG file"):  # noqa
            with open(test_file_path("not-a-MSG-file.msg"), "rb") as f:
                Message.load(f)

    def it_can_load_from_the_bytes_of_a_file_like_object(self):
        with open(test_file_path("message.msg"), "rb") as f:
            file_bytes = f.read()

        msg = Message.load(file_bytes)

        assert isinstance(msg, Message)
        assert isinstance(msg._storage, Storage)

    def but_it_raises_when_the_bytes_are_not_those_of_a_MSG_file(self):
        with pytest.raises(ValueError, match="msg_file is not an Outlook MSG file"):  # noqa
            with open(test_file_path("not-a-MSG-file.msg"), "rb") as f:
                Message.load(f.read())

    @pytest.mark.parametrize(
        ("file_name", "expected_value"),
        [("no-attachments.msg", 0), ("message.msg", 1), ("sediment.msg", 6)],
    )
    def it_knows_how_many_attachments_the_message_has(self, file_name: str, expected_value: int):
        msg = Message.load(test_file_path(file_name))
        assert msg.attachment_count == expected_value
        assert msg.attachment_count == len(msg.attachments)

    def it_provides_access_to_any_attachments_to_the_message(self):
        msg = Message.load(test_file_path("sediment.msg"))

        attachments = msg.attachments

        assert len(attachments) == 6
        assert all(isinstance(a, Attachment) for a in attachments)

    def it_provides_access_to_the_plain_text_message_body_when_present(self):
        """Plain-text body (0x1000 001f) appears to be always present on IPM.Note."""
        msg = Message.load(test_file_path("message.msg"))

        body = msg.body

        assert body is not None
        assert isinstance(body, str)
        assert body.startswith("asdfasdf\r\n")

    def it_provides_access_to_the_HTML_message_body_when_it_is_PidTagHtml(self):
        """HTML body as bytes encoded with PidTagInternetCodepage" seems to be most common.

        That's PidTagHtml (PtypBinary). There's also PidTagBodyHtml (PtypString) but I have no
        examples of that.
        """
        msg = Message.load(test_file_path("no-attachments.msg"))

        body = msg.html_body

        assert body is not None
        assert isinstance(body, str)
        assert body.startswith("This is a message")

    def it_knows_the_RFC822_message_headers(self):
        msg = Message.load(test_file_path("sediment.msg"))

        message_headers = msg.message_headers

        assert isinstance(message_headers, dict)
        assert message_headers["Content-Language"] == "en-us"
        assert message_headers["Date"] == "Tue, 11 Aug 2020 15:36:27 -0400"
        assert message_headers["Subject"].startswith("FW: Lab Results: ONE 7771 ")

    def it_knows_the_MSG_message_class(self):
        assert Message.load(test_file_path("message.msg")).message_class == "IPM.Note.Tutanota"

    def it_provides_access_to_the_Properties_object_for_the_message(self):
        msg = Message.load(test_file_path("message.msg"))
        assert isinstance(msg.properties, Properties)

    def it_provides_access_to_the_recipients_collection_for_the_message(self):
        msg = Message.load(test_file_path("sediment.msg"))

        recipients = msg.recipients

        assert len(recipients) == 4
        assert all(isinstance(r, Recipient) for r in recipients)

    def it_knows_the_message_sender(self):
        msg = Message.load(test_file_path("no-attachments.msg"))
        assert msg.sender == '"peterpan@neverland.com" <peterpan@neverland.com>'

    def it_knows_the_sent_time(self):
        msg = Message.load(test_file_path("message.msg"))
        assert msg.sent_date == dt.datetime(2020, 10, 6, 9, 57, 46, tzinfo=dt.timezone.utc)

    def it_knows_the_subject(self):
        msg = Message.load(test_file_path("message.msg"))
        assert msg.subject == "Re: test internal"
