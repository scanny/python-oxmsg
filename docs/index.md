# python-oxmsg

Extract text and attachments from Outlook MSG (.msg) files.

## Install
```bash
pip install python-oxmsg
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
