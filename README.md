[![MIT License](https://img.shields.io/badge/License-MIT-orange.svg)](LICENSE.txt)
[![on PyPI](https://img.shields.io/badge/pypi-0.0.1-blue.svg)](https://pypi.org/project/python-oxmsg/0.0.1/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-brightgreen.svg)](https://www.python.org/downloads/)

# python-oxmsg

Parse Outlook MSG (.msg) files to extract email messages and attachments.

The target use case is extracting Outlook message text and accessing attachments. There is no support for modifying messages or creating them from scratch. In addition to message text, other message properties such as sent-date, etc. are also accessible.


## Documentation

Documentation for this project is on [GitHub Pages](https://scanny.github.io/python-oxmsg).


## Installation
```bash
pip install python-oxmsg
```
Occasionally it can be useful to install from a GitHub branch, perhaps to try out a version that has not yet been released. This command would install from the `develop` branch:
```bash
pip install git+https://github.com/scanny/python-oxmsg@develop
```

## Usage
```python
>>> from oxmsg import Message
>>> msg = Message.load("message.msg")
>>> msg.message_class
'IPM.Note'
>>> msg.attachment_count
1
>>> attachment = msg.attachments[0]
>>> attachment.attached_by_value  # -- attachment bytes only available when True --
True
>>> attachment.file_name
'q1-objectives.pptx'
>>> attachment.mime_type
'application/vnd.openxmlformats-officedocument.presentationml.presentation'
>>> attachment.size
96407
>>> attachment.last_modified.isoformat()
'2023-11-18T16:08:17+00:00'
>>> with open(attachment.file_name, "wb") as f:
...     f.write(attachment.file_bytes)
```

## CLI

`python-oxmsg` includes a CLI that may be useful for diagnostic purposes.
```bash
$ oxmsg
Usage: oxmsg [OPTIONS] COMMAND [ARGS]...

  Utility CLI for `python-oxmsg`.

  Provides the subcommands listed below, useful for exploratory or diagnostic
  purposes.

Options:
  --help  Show this message and exit.

Commands:
  dump     Write a summary of the MSG file's properties to stdout.
  storage  Summarize low-level "directories and files" structure of MSG...

```

The `dump` sub-command displays all properties available in the message along with the
PID and PTYP information required to access those properties from a `Properties` object.

```bash
$ oxmsg dump message.msg

------------------
Message Properties
------------------

header-properties
-----------------
recipient_count:    1

distinguished-properties
------------------------
attachment_count:         0
internet_code_page:       utf-8
message_class:            IPM.Note
sender:                   from@domain.com
...

other properties
-----------------------------------------+---------------+--------------------
property-id                              | type          | value
-----------------------------------------+---------------+--------------------
0x0017 - PidTagImportance                | PtypInteger32 | 00 00 00 01
0x001A - PidTagMessageClass              | PtypString8   | 'IPM.Note'
0x0036 - PidTagSensitivity               | PtypInteger32 | 00 00 00 00
0x0037 - PidTagSubject                   | PtypString8   | 'A test message'
0x003B - PidTagSentRepresentingSearchKey | PtypBinary    | 21 bytes
0x003D - PidTagSubjectPrefix             | PtypString8   | ''
0x0042 - PidTagSentRepresentingName      | PtypString8   | 'from@domain.com'
...
```

## Changelog

The release history including a chronicle of notable changes with each release is
recorded in [CHANGELOG.md](https://github.com/scanny/python-oxmsg/blob/master/CHANGELOG.md).
