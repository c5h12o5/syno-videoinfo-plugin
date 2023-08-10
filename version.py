"""Get the version of the project from git tags."""
import subprocess

__all__ = ["version"]


def version():
    cmd = "git describe --tags --match v[0-9]*".split()
    tag_describe = subprocess.check_output(cmd).decode().strip()
    tag_version = tag_describe[1:]
    if "-" in tag_version:
        tag_version = tag_version.split("-", 1)[0]
    return tag_version
