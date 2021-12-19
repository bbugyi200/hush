# hush

**A Python library that helps manage secrets using tools specified by plugin hooks.**

project status badges:

[![CI Workflow](https://github.com/bbugyi200/hush/actions/workflows/ci.yml/badge.svg)](https://github.com/bbugyi200/hush/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/bbugyi200/hush/branch/master/graph/badge.svg)](https://codecov.io/gh/bbugyi200/hush)
[![Documentation Status](https://readthedocs.org/projects/hush/badge/?version=latest)](https://hush.readthedocs.io/en/latest/?badge=latest)
[![Package Health](https://snyk.io/advisor/python/python-hush/badge.svg)](https://snyk.io/advisor/python/python-hush)

version badges:

[![Project Version](https://img.shields.io/pypi/v/python-hush)](https://pypi.org/project/python-hush/)
[![Python Versions](https://img.shields.io/pypi/pyversions/python-hush)](https://pypi.org/project/python-hush/)
[![Cookiecutter: cc-python](https://img.shields.io/static/v1?label=cc-python&message=2021.10.03&color=d4aa00&logo=cookiecutter&logoColor=d4aa00)](https://github.com/bbugyi200/cc-python)
[![Docker: bbugyi/python](https://img.shields.io/static/v1?label=bbugyi%20%2F%20python&message=2021.09.25&color=8ec4ad&logo=docker&logoColor=8ec4ad)](https://github.com/bbugyi200/docker-python)


## Installation 🗹

To install `python-hush` using [pip][9], run the following
commands in your terminal:

``` shell
python3 -m pip install --user python-hush  # install hush
```

If you don't have pip installed, this [Python installation guide][10] can guide
you through the process.


## CLI Usage

<!-- [[[[[kooky.cog
import subprocess

popen = subprocess.Popen(["hush", "--help"], stdout=subprocess.PIPE)
stdout, _ = popen.communicate()
print("```", stdout.decode().strip(), "```", sep="\n")
]]]]] -->
```
usage: hush [-h] [-L [FILE[:LEVEL][@FORMAT]]] [-v] [-n NAMESPACE] [-u USER]
            key

A Python library that helps manage secrets.

Uses the secret management tools (e.g. pass) specified by (internal and
external) plugin hooks.

positional arguments:
  key                   The key that corresponds with the secret that we wish
                        to retrieve.

optional arguments:
  -h, --help            show this help message and exit
  -L [FILE[:LEVEL][@FORMAT]], --log [FILE[:LEVEL][@FORMAT]]
                        This option can be used to enable a new logging
                        handler. FILE should be either a path to a logfile or
                        one of the following special file types: [1] 'stderr'
                        to log to standard error (enabled by default), [2]
                        'stdout' to log to standard out, [3] 'null' to disable
                        all console (e.g. stderr) handlers, or [4] '+[NAME]'
                        to choose a default logfile path (where NAME is an
                        optional basename for the logfile). LEVEL can be any
                        valid log level (i.e. one of ['CRITICAL', 'DEBUG',
                        'ERROR', 'INFO', 'TRACE', 'WARNING']) and FORMAT can
                        be any valid log format (i.e. one of ['color', 'json',
                        'nocolor']). NOTE: This option can be specified
                        multiple times and has a default argument of '+'.
  -n NAMESPACE, --namespace NAMESPACE
                        The namespace the secret is apart of. This argument
                        should be a comma-separated list of namespace parts.
  -u USER, --user USER  Run secret retrieving commands as this user instead of
                        the current user.
  -v, --verbose         How verbose should the output be? This option can be
                        specified multiple times (e.g. -v, -vv, -vvv, ...).
```
<!-- [[[[[end]]]]] -->

## Useful Links 🔗

* [API Reference][3]: A developer's reference of the API exposed by this
  project.
* [cc-python][4]: The [cookiecutter][5] that was used to generate this project.
  Changes made to this cookiecutter are periodically synced with this project
  using [cruft][12].
* [CHANGELOG.md][2]: We use this file to document all notable changes made to
  this project.
* [CONTRIBUTING.md][7]: This document contains guidelines for developers
  interested in contributing to this project.
* [Create a New Issue][13]: Create a new GitHub issue for this project.
* [Documentation][1]: This project's full documentation.
* [Usage][14]: How do I use Hush?
* [Writing Plugins][15]: How do I write my own plugins for Hush?


[1]: https://hush.readthedocs.io/en/latest
[2]: https://github.com/bbugyi200/hush/blob/master/CHANGELOG.md
[3]: https://hush.readthedocs.io/en/latest/modules.html
[4]: https://github.com/bbugyi200/cc-python
[5]: https://github.com/cookiecutter/cookiecutter
[6]: https://docs.readthedocs.io/en/stable/
[7]: https://github.com/bbugyi200/hush/blob/master/CONTRIBUTING.md
[8]: https://github.com/bbugyi200/hush
[9]: https://pip.pypa.io
[10]: http://docs.python-guide.org/en/latest/starting/installation/
[11]: https://github.com/pypa/pipx
[12]: https://github.com/cruft/cruft
[13]: https://github.com/bbugyi200/hush/issues/new/choose
[14]: https://hush.readthedocs.io/en/latest/usage.html
[15]: https://hush.readthedocs.io/en/latest/plugins.html
