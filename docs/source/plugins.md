# How to write your own plugin for Hush?

Hush uses [pluggy][1] to manage its plugin system. As such, the instructions
for creating a new external plugin for Hush are mostly the same as they are for
any other application with a plugin-architecture that uses pluggy (e.g.
[pytest][2]).

## Examples

A good, general-purpose (i.e. not specific to Hush) example of writing external
plugins using pluggy can be found [here][3]. The example below is very similar
but is specific to Hush. Namely, the `hush-tmp-secrets` plugin defined below
allows users to start storing secrets in plain-text files under the
`/tmp/secrets` directory.

#### hush-tmp-secrets/hush\_tmp\_secrets.py

```python
"""This module contains the hush-tmp-secrets Hush plugin's implementation."""

from pathlib import Path
from typing import Optional

from hush.plugin import hookimpl


@hookimpl
def get_secret(key: str) -> Optional[str]:
    """Get secrets by searching through the /tmp/secrets directory."""
    key_filename = f"{key}.txt"

    key_full_path = Path("/tmp/secrets") / key_filename
    if key_full_path.exists():
        return key_full_path.read_text().strip()

    return None
```

> **WARNING**: This is just a toy example. A better, more realistic
> implementation of this plugin would probably (at the very least) verify the
> `/tmp/secrets` directory's permissions and use some form of encryption
> instead of storing secrets in unencrypted text files.

#### hush-tmp-secrets/setup.py

```python
from setuptools import setup


setup(
    name="python-hush-tmp-secrets",
    install_requires="python-hush",
    entry_points={"hush": ["tmp_secrets = hush_tmp_secrets"]},
    py_modules=["hush_tmp_secrets"],
)
```

#### Using the hush-tmp-secrets Plugin

```console
$ python3 -m pip install --editable /path/to/hush-tmp-secrets
$ echo "MOOOOO!" > /tmp/secrets/cow.txt
$ hush cow
MOOOOO!
```

> **NOTE**: See the [Usage][4] section of this documentation for more
> information on the `hush` script, which is used in the code-block above.


[1]: https://pluggy.readthedocs.io/en/stable/
[2]: https://github.com/pytest-dev/pytest
[3]: https://pluggy.readthedocs.io/en/stable/#the-plugin
[4]: https://hush.readthedocs.io/en/latest/usage.html
