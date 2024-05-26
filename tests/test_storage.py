"""Unit-test suite for the `oxmsg.storage` module."""

from __future__ import annotations

import hashlib

import pytest
from olefile import OleFileIO

from oxmsg.domain import constants as c
from oxmsg.storage import Storage, Stream

from .unit_util import test_file_path


class DescribeStorage:
    """Unit-test suite for `oxmsg.storage.Storage` objects."""

    def it_can_load_the_storage_tree_from_an_olefile_root_directory(self):
        with OleFileIO(test_file_path("message.msg")) as ole:
            root_storage = Storage.from_ole(ole)

        # -- the root storage is a Storage --
        assert isinstance(root_storage, Storage)
        # -- its streams are Stream instances (it really does have 42 streams :) --
        assert len(root_storage.streams) == 42
        assert all(isinstance(s, Stream) for s in root_storage.streams)
        # -- its sub-storages are all Storage objects --
        assert len(root_storage.storages) == 3
        assert all(isinstance(s, Storage) for s in root_storage.storages)

    def it_has_an_informative_str_representation(self, storage: Storage):
        assert repr(storage) == "Storage(path='', 42 streams, 3 storages)"

    def it_provides_access_to_its_attachment_storages(self, storage: Storage):
        attachment_storages = storage.iter_attachment_storages()

        # -- this storage contains exactly one attachment --
        attachment_storage = next(attachment_storages)
        assert isinstance(attachment_storage, Storage)
        assert attachment_storage.name.startswith("__attach_version1.0_#")
        with pytest.raises(StopIteration):
            next(attachment_storages)

    @pytest.mark.parametrize(
        ("path", "expected_value"),
        [
            # -- root storage name is the empty string --
            ("", ""),
            ("__attach_version1.0_#00000000", "__attach_version1.0_#00000000"),
            ("foo/bar/baz", "baz"),
        ],
    )
    def it_knows_the_storage_name(self, path: str, expected_value: str):
        assert Storage(path, (), ()).name == expected_value

    def it_provides_access_to_its_properties_stream_bytes(self, storage: Storage):
        properties_stream_bytes = storage.properties_stream_bytes

        assert isinstance(properties_stream_bytes, bytes)
        assert len(properties_stream_bytes) == 1152
        assert hashlib.sha1(properties_stream_bytes).hexdigest() == (
            "7a803029a23197ad14336779aa597c6c85ba7135"
        )

    def it_provides_access_to_the_bytes_of_one_of_its_streams_by_pid_and_ptyp(
        self, storage: Storage
    ):
        stream_bytes = storage.property_stream_bytes(c.PID_MESSAGE_CLASS, c.PTYP_STRING)

        assert isinstance(stream_bytes, bytes)
        assert len(stream_bytes) == 34
        # -- string property is encoded UTF-16LE ("utf-16-le") --
        assert stream_bytes == (
            b"I\x00P\x00M\x00.\x00N\x00o\x00t\x00e\x00.\x00T\x00u\x00t\x00a\x00n\x00"
            b"o\x00t\x00a\x00"
        )

    # -- fixtures --------------------------------------------------------------------------------

    @pytest.fixture
    def storage(self) -> Storage:
        with OleFileIO(test_file_path("message.msg")) as ole:
            return Storage.from_ole(ole)


class DescribeStream:
    """Unit-test suite for `oxmsg.storage.Stream` objects."""

    def it_has_an_informative_str_representation(self, stream: Stream):
        assert repr(stream) == "Stream(path='__substg1.0_1000001F', 432 bytes)"

    @pytest.mark.parametrize(
        ("path", "expected_value"),
        [
            ("__substg1.0_003D001F", "__substg1.0_003D001F"),
            ("__attach_version1.0_#00000000/__substg1.0_003D001F", "__substg1.0_003D001F"),
        ],
    )
    def it_knows_the_stream_name(self, path: str, expected_value: str):
        assert Stream(path, b"abcde").name == expected_value

    def it_provides_access_to_its_bytes(self, stream: Stream):
        bytes_ = stream.bytes_

        assert isinstance(bytes_, bytes)
        assert len(bytes_) == 432
        assert hashlib.sha1(bytes_).hexdigest() == "6fbf22c8ef66b2cb707b478def7f7378a57d1baf"

    # -- fixtures --------------------------------------------------------------------------------

    @pytest.fixture
    def stream(self) -> Stream:
        path = "__substg1.0_1000001F"
        with OleFileIO(test_file_path("message.msg")) as ole, ole.openstream(path) as f:
            bytes_ = f.read()
        return Stream(path, bytes_)
