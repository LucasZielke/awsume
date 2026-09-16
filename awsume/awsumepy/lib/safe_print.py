import os
import sys

import colorama
import yaml

from .constants import AWSUME_CONFIG


def safe_print(message: str, color: str = "", end: str | None = None):
    """Safely print so no data is interfering with the shell wrapper"""
    with open(str(AWSUME_CONFIG)) as acf:
        config = yaml.safe_load(acf) or {}
    if not config:
        config = {"colors": True}
    if os.name == "nt" or not config.get("colors"):
        color = ""
    print(
        str(color) + str(message) + colorama.Style.RESET_ALL, end=end, file=sys.stderr
    )
