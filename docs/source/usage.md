# Usage

Hush can be thought of as a secrets manager, but it is more appropriate to
think of it as a _manager_ of other secret managers.

Keep in mind the following notes while reading the rest of the documentation:

* This package provides both a library and an executable, named `hush`, that
  can be used to test this package's functionality.
* Hush has multiple builtin plugins which are enabled by default (i.e. we will
  attempt to use them, by default, when a user requests secret retrieval).
* In the examples in this documentation, we will make use of a builtin plugin
  that reads secrets from environment variables.


## Using the Library

The `hush` library provides two public methods to access its functionality: the
`hush.get_secret()` function and the `hush.Hush()` class. We demonstrate how
each can be used in the examples below.

### Examples

```python
import os

from hush import Hush, get_secret


# To retrieve a secret we must provide Hush with a key to associate with that
# secret. Below, that key is 'foobar'.
os.environ["FOOBAR"] = "Kung Fooooo!"
secret = get_secret("foobar")
print(secret)  # output: Kung Fooooo!

# A secret can optionally belong to a particular namespace. A namespace is a
# listing of names that are generally combined with the key somehow, but
# ultimately it is up to each plugin to decide how it wants to handle namespaces
# (if it chooses to handle them at all).
os.environ["DB_DEV_FOOBAR"] = "Database in Development!"
secret = get_secret("foobar", ["db", "dev"])
print(secret)  # output: Database in Development!

# The Hush class can be used to constrain the context (i.e. paramaters) for the
# `get_secret()` function (which the `Hush.get_secret()` method wraps).
hush = Hush(namespace=["db", "dev"])
secret = hush.get_secret("foobar")
print(secret)  # output: Database in Development!
```


## Using the `hush` Script

This package also comes with an executable script, `hush`, that can be used to
invoke Hush from the command-line.

### Examples

Add secrets using environment variables:

```console
$ export FOOBAR="Kung Fooooo!"
$ export DB_DEV_FOOBAR="Database in Development!"
```

Use `hush` to retrieve those secrets:

```console
$ hush foobar
Kung Fooooo!

$ hush --namespace=db,dev foobar
Database in Development!
```
