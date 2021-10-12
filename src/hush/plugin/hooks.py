"""Contains the pluggy decorators used to mark impls and specs."""

from pluggy import HookimplMarker, HookspecMarker


hookimpl = HookimplMarker("hush")
hookspec = HookspecMarker("hush")
