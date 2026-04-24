"""
This is the entry script

References:
    - https://setuptools.readthedocs.io/en/latest/userguide/entry_point.html
"""

import argparse
import logging
import sys
from .stitcher import Stitcher
from pystitcher import __version__

__author__ = "Nemo"
__copyright__ = "Nemo"
__license__ = "MIT"

_logger = logging.getLogger(__name__)


# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.


def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    pass


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    pass


def main(args):
    """Main CLI function
    """
    pass

def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`
    """
    pass


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html

    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m pystitcher.skeleton 42
    #
    run()
