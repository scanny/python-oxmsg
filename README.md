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

## Changelog

The release history including a chronicle of notable changes with each release is
recorded in [CHANGELOG.md](https://github.com/scanny/python-oxmsg/blob/master/CHANGELOG.md).
