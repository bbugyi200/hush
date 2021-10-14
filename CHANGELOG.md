# Changelog for `hush`

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog], and this project adheres to
[Semantic Versioning].

[Keep a Changelog]: https://keepachangelog.com/en/1.0.0/
[Semantic Versioning]: https://semver.org/


## [Unreleased](https://github.com/bbugyi200/hush/compare/0.3.1...HEAD)

No notable changes have been made.

## [0.3.1](https://github.com/bbugyi200/hush/compare/0.3.0...0.3.1) - 2021-10-14

## Miscellaneous

* Refactored codebase to use new `get_plugin_modules()` function to collect
  builtin plugins.
* Prefix private module/package names with an underscore.
* Improve module design so nested imports are no longer necessary.

## [0.3.0](https://github.com/bbugyi200/hush/compare/0.2.0...0.3.0) - 2021-10-06

### Added

* Added `hush.Hush` class.

### Miscellaneous

* Factor  `pass_store.py` and `envvars.py` out of `builtin.py`.

## [0.2.0](https://github.com/bbugyi200/hush/compare/0.1.0...0.2.0) - 2021-10-04

### Added

* Add `hush.get_secret()` method.
* Add `hush` executable script.

## [0.1.0](https://github.com/bbugyi200/hush/releases/tag/0.1.0) - 2021-10-03

### Miscellaneous

* First release.
