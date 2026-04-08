---
title: "Installing and Managing Python"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/10/python"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "ol10"
  - "development"
type: "oracle-doc"
sensitivity: public
---

## Oracle Linux 10

Installing and Managing Python

G14607-02

January 2026

---

[Title and Copyright Information](#copyright-information)

Oracle Linux 10 Installing and Managing Python

G14607-02

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2025, 2026, Oracle and/or its affiliates.

Documentation License

The content in this document is licensed under the (CC-BY-SA) license. In accordance with
CC-BY-SA, if you distribute this content or an adaptation of it, you must provide attribution
to Oracle and retain the original copyright notices.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/python/python-Preface.html -->

## Preface

[Oracle Linux 10: Installing and Managing
Python](https://docs.oracle.com/en/operating-systems/oracle-linux/10/python/) describes how to install and
configure a Python runtime environment so that you can run applications and scripting tools
that require a Python interpreter to function.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/python/python-AboutPython.html -->

## 1 About Python

Python is a high-level general purpose programming language that relies on an interpreter to
fulfill scripted functions. On Oracle Linux 10, many system utilities, tools for data analysis and web applications rely on the
presence of a Python runtime environment to function.

Python 2 is no longer maintained by the Python community; Python 2 is also not supported or
available on Oracle Linux 10. Any
existing Python 2 scripts must be migrated to Python 3 or run inside a container. For more
information about running scripts inside containers, see [Oracle Linux: Podman User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/podman/).

You can read more information about creating Python scripts at <https://www.python.org/doc/>.

Note:

Unversioned Python commands are aliased to Python 3.12 by default in Oracle Linux 10.

For more information, see [Installing Python](python-InstallingPython.html#installing-python3).


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/python/python-InstallingPython.html -->

## 2 Installing Python

To install Python 3.12 on an Oracle Linux 10 system:

```
sudo dnf install python3
```

The `python3` command points to Python 3.12 if it's installed on the system. To
verify that behavior, run the following command:

```
python3 --version
```

In Oracle Linux 10, all unversioned Python commands point to Python 3.12 and can't be
configured to run on newer Python versions by using the `alternatives`
command.

To optionally enable the unversioned `python` command, install the
`python-unversioned-command` package:

```
sudo dnf install /usr/bin/python
```

Note:

Python 3.12
is maintained for the full lifespan of Oracle Linux 10.

Application Stream packages, such as more recent versions of Python 3, have their own major version releases and have shorter maintenance lifespans. For more information, see [Oracle Linux: Product Life Cycle Information](https://docs.oracle.com/en/operating-systems/oracle-linux/product-lifecycle/).

Note:

Newer versions of Python might be available in the `ol10_developer_EPEL` yum repository. Those packages are intended for development purposes only, so we recommend that you only install them in development environments. In that scenario you could optionally use `pip` to install extra Python libraries that haven't been packaged yet. For more information, see [Installing Third-Party Packages](python-InstallingThirdPartyPackages.html#installing-third-party-packages).

### Installing Extra Python Libraries

You can also install extra dependencies from the Oracle Linux yum server. For example, to
install the `requests` library for the default runtime version of Python 3, you
would install the `python3-requests` package:

```
sudo dnf install python3-requests
```

Dependencies that are installed in this way are available for any compatible Python
installations on the same system. In addition, any matching packages can also be removed
without also removing existing Python installations.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/python/python-InstallingThirdPartyPackages.html -->

## 3 Installing Third-Party Packages

Before installing a third-party package, verify if you can install the Python library you
need from the Oracle Linux yum server. For example, to check if the `requests`
library has been provided for Python 3.12, run the following command:

```
sudo dnf search python3-requests
```

For more information about installing extra Python libraries from the Oracle Linux yum
server, read [Installing Extra Python Libraries](python-InstallingPython.html#installing-python-libraries).

If you can't find a particular dependency on the Oracle Linux yum server, or if the script
that you need to run requires a newer version of the dependency than the installed package
already provides, you can optionally use the `pip` package manager to install
it from a third-party source.

To ensure that the system remains supported, for each project you can install
and run third-party packages in an isolated virtual environment created with the
`venv` Python module.

To learn more about installing third-party packages inside Python virtual environments,
visit <https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>.

### Installing Pip Libraries With Python 3

1. Install base packages for the `pip3` command:

   ```
   sudo dnf install python3-pip python3-setuptools python3-pip-wheel
   ```
2. Create a Python virtual environment. For example, the following command creates a Python
   3 virtual environment named `example3`:

   ```
   python3 -m venv --system-site-packages example3
   ```
3. You can now activate the `example3` environment and begin installing
   third-party dependencies. For example, to install a newer version of the
   `requests` library for Python 3:

   ```
   source example3/bin/activate
   ```

   ```
   python3 -m pip install --user requests
   ```

   Attention:

   Using the `pip` and `pip3` commands outside of a Python virtual environment
   applies changes system-wide, and that can impact compatibility with some installed
   packages in an Oracle Linux 10 installation.

   Add the `--user` flag to any `pip3 install`
   commands to ensure that dependency packages are only available to the
   current user.
4. To run compatible scripts with the third-party packages that have been installed, run
   them from within the same Python virtual environment.