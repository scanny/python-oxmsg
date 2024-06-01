# pyright: reportPrivateUsage=false

"""Unit-test suite for the `oxmsg.properies` module."""

from __future__ import annotations

import datetime as dt
import uuid
from typing import Sequence

import pytest
from olefile import OleFileIO

from oxmsg.domain import constants as c
from oxmsg.domain import model as m
from oxmsg.properties import (
    BaseProperty,
    BinaryProperty,
    BooleanProperty,
    Float64Property,
    GuidProperty,
    Int16Property,
    Int32Property,
    Properties,
    String8Property,
    StringProperty,
    TimeProperty,
)
from oxmsg.storage import Storage
from oxmsg.util import lazyproperty

from .unit_util import test_file_path


class DescribeProperties:
    """Unit-test suite for `oxmsg.properties.Properties` objects."""

    def it_can_extract_a_binary_property_value(self, properties: Properties):
        assert properties.binary_prop_value(c.PID_SENDER_SEARCH_KEY) == (
            b"SMTP:bedfortest@tutanota.de\x00"
        )

    def but_it_returns_None_when_the_binary_property_is_not_present(self, properties: Properties):
        assert properties.binary_prop_value(c.PID_ATTACH_ENCODING) is None

    def it_can_extract_a_date_property_value(self, properties: Properties):
        assert properties.date_prop_value(c.PID_CREATION_TIME) == (
            dt.datetime(2020, 10, 21, 13, 34, 40, tzinfo=dt.timezone.utc)
        )

    def but_it_returns_None_when_the_time_property_is_not_present(self, properties: Properties):
        assert properties.date_prop_value(c.PID_DEFERRED_DELIVERY_TIME) is None

    def it_can_extract_a_int_property_value(self, properties: Properties):
        assert properties.int_prop_value(c.PID_STORE_SUPPORT_MASK) == 0x00040E79

    def but_it_returns_None_when_the_int_property_is_not_present(self, properties: Properties):
        assert properties.int_prop_value(c.PID_CONTENT_LENGTH) is None

    def it_can_extract_a_str_property_value(self, properties: Properties):
        assert properties.str_prop_value(c.PID_MESSAGE_CLASS) == "IPM.Note.Tutanota"

    def but_it_returns_None_when_the_str_property_is_not_present(self, properties: Properties):
        assert properties.str_prop_value(c.PID_ATTACH_CONTENT_ID) is None

    # -- fixtures --------------------------------------------------------------------------------

    @pytest.fixture
    def properties(self) -> Properties:
        with OleFileIO(test_file_path("message.msg")) as ole:
            storage = Storage.from_ole(ole)
        return Properties(storage, m.MSG_HDR_OFFSET)


class DescribeBaseProperty:
    """Unit-test suite for `oxmsg.properties.BaseProperty` objects."""

    def it_knows_its_PID(self):
        assert BaseProperty(b"\x1F\x00\x00\x10").pid == 0x1000

    def it_knows_the_ms_name_of_its_PID(self):
        assert BaseProperty(b"\x1F\x00\x00\x10").name == "PidTagBody"

    def it_knows_its_PTYP(self):
        assert BaseProperty(b"\x1F\x00\x00\x10").ptyp == 0x001F

    def it_knows_the_ms_name_of_its_PTYP(self):
        assert BaseProperty(b"\x1F\x00\x00\x10").ptyp_name == "PtypString"

    def it_provides_access_to_its_payload_to_help(self):
        segment = b"\x00" * 8 + b"\x01\x02\x03\x04\x05\x06\x07\x08"
        assert BaseProperty(segment)._payload == b"\x01\x02\x03\x04\x05\x06\x07\x08"


class DescribeBinaryProperty:
    """Unit-test suite for `oxmsg.properties.BinaryProperty` objects."""

    def its_value_is_the_bytes_of_its_stream(self):
        segment = b"\x02\x01" + b"\x0B\x30" + b"\x00" * 12
        storage = FakePropStorage(
            [(c.PID_SEARCH_KEY, c.PTYP_BINARY, b"\x01\x02\x03\x04\x05\x06\x07\x08")]
        )

        assert BinaryProperty(segment, storage).value == b"\x01\x02\x03\x04\x05\x06\x07\x08"


class DescribeBooleanProperty:
    """Unit-test suite for `oxmsg.properties.BooleanProperty` objects."""

    @pytest.mark.parametrize(
        ("first_byte", "expected_value"),
        [(b"\x01", True), (b"\x00", False), (b"\x02", True), (b"\x03", True), (b"\x10", True)],
    )
    def its_value_is_determined_by_the_first_byte_of_its_payload(
        self, first_byte: bytes, expected_value: bool
    ):
        """Spec says this is one byte, either `b"\x00"` or `b"\x01"`.

        But other examples interpret any non-zero value as True, so we follow suit.
        """
        segment = b"\x0B\x00" + b"\x1B\x0E" + b"\x00" * 4 + first_byte + b"\x00" * 7
        assert BooleanProperty(segment).value is expected_value


class DescribeFloat64Property:
    """Unit-test suite for `oxmsg.properties.Float64Property` objects."""

    def its_value_is_determined_by_the_eight_bytes_of_its_payload(self):
        ptag = b"\x05\x00" + b"\x0D\x80"
        reserved = b"\x00" * 4
        payload = b"\x18\x2D\x44\x54\xFB\x21\x09\x40"
        segment = ptag + reserved + payload

        assert 3.1415 < Float64Property(segment).value < 3.1416


class DescribeGuidProperty:
    """Unit-test suite for `oxmsg.properties.GuidProperty` objects."""

    def its_value_is_a_UUID_object(self):
        segment = b"\x48\x00" + b"\x34\x12" + b"\x00" * 12
        stream_bytes = b"\x78\x56\x34\x12\xBC\x9A\xF0\xDE\x12\x34\x56\x78\x9A\xBC\xDE\xF0"
        storage = FakePropStorage([(0x1234, c.PTYP_GUID, stream_bytes)])

        guid_prop = GuidProperty(segment, storage)

        assert guid_prop.value == uuid.UUID("{12345678-9abc-def0-1234-56789abcdef0}")
        assert guid_prop.value.bytes_le == stream_bytes
        assert str(guid_prop) == "12345678-9abc-def0-1234-56789abcdef0"


class DescribeInt16Property:
    """Unit-test suite for `oxmsg.properties.Int16Property` objects."""

    def its_value_is_determined_by_the_first_two_bytes_of_its_payload(self):
        ptag = b"\x02\x00" + b"\xAA\xAA"
        reserved = b"\x00" * 4
        payload = b"\x34\x12" + b"\xAA" * 6
        segment = ptag + reserved + payload

        assert Int16Property(segment).value == 0x1234


class DescribeInt32Property:
    """Unit-test suite for `oxmsg.properties.Int32Property` objects."""

    def its_value_is_determined_by_the_first_four_bytes_of_its_payload(self):
        ptag = b"\x03\x00" + b"\x21\x0E"
        reserved = b"\x00" * 4
        payload = b"\x78\x56\x34\x12" + b"\xAA" * 4
        segment = ptag + reserved + payload

        assert Int32Property(segment).value == 0x12345678


class DescribeStringProperty:
    """Unit-test suite for `oxmsg.properties.StringProperty` objects."""

    def its_value_is_the_str_of_its_UTF_16LE_stream(self):
        """A PtypString property is always UTF-16LE encoded unicode."""
        segment = b"\x1F\x00" + b"\x04\x37" + b"\x00" * 12
        stream_bytes = "Abcdefg hijklm nopqr stuvw xyz.".encode("utf-16-le")
        storage = FakePropStorage([(c.PID_ATTACH_FILENAME, c.PTYP_STRING, stream_bytes)])

        assert StringProperty(segment, storage).value == "Abcdefg hijklm nopqr stuvw xyz."


class DescribeString8Property:
    """Unit-test suite for `oxmsg.properties.String8Property` objects."""

    def its_value_is_the_str_of_its_str_prop_encoded_stream(self):
        """A PtypString8 property uses an 8-bit character encoding that must be specified."""
        ptag = b"\x1E\x00" + b"\x1A\x00"
        reserved = b"\x00" * 4
        # -- payload normally contains string length but it's not used, just zero out payload --
        payload = b"\x00" * 16
        segment = ptag + reserved + payload
        stream_bytes = b"\xD6abcdefg hijklm nopqr stuvw xyz.\xA9"
        storage = FakePropStorage([(c.PID_MESSAGE_CLASS, c.PTYP_STRING8, stream_bytes)])

        value = String8Property(segment, storage, "iso-8859-1", "utf-8").value

        assert value == "Öabcdefg hijklm nopqr stuvw xyz.©"


class DescribeTimeProperty:
    """Unit-test suite for `oxmsg.properties.TimeProperty` objects."""

    def its_value_is_the_count_of_hundred_nanosecond_intervals_since_Jan_1_1601(self):
        ptag = b"\x40\x00" + b"\x07\x30"
        reserved = b"\x00" * 4
        payload = b"\xE4\xE3\x5B\xF6\x4C\xF5\xD4\x01"
        segment = ptag + reserved + payload

        value = TimeProperty(segment).value

        assert value.isoformat() == "2019-04-17T18:40:00+00:00"


# -- module-level fixtures -----------------------------------------------------------------------


class FakePropStorage:
    """Implements PropStorageT."""

    def __init__(self, prop_stream_values: Sequence[tuple[int, int, bytes]]):
        self._prop_stream_values = prop_stream_values

    @lazyproperty
    def properties_stream_bytes(self) -> bytes:
        raise NotImplementedError

    def property_stream_bytes(self, pid: int, ptyp: int) -> bytes:
        for pid_, ptyp_, bytes_ in self._prop_stream_values:
            if pid == pid_ and ptyp == ptyp_:
                return bytes_
        raise ValueError(f"no property stream for {pid=:04X}, {ptyp=:04X}")
