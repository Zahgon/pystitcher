import os
import logging
import shutil
import tempfile
import urllib.request
import validators

import html5lib
import markdown

from pypdf import PdfWriter, PdfReader
from pypdf.generic import Fit
from pystitcher import __version__
from .bookmark import Bookmark

_logger = logging.getLogger(__name__)

""" Main Stitcher class """
class Stitcher:
    def __init__(self, inputBuffer):
        self.files = []
        self.currentPage = 1
        self.title = None
        self.bookmarks = []
        self.currentLevel = 0
        self.oldBookmarks = []
        self.dir = os.path.dirname(os.path.abspath(inputBuffer.name))
        # Fit complete page width by default
        DEFAULT_FIT = '/FitV'
        # Do not rotate by default
        DEFAULT_ROTATE = 0
        # Start at page 1 by default
        DEFAULT_START = 1
        # End at the final page by default
        DEFAULT_END = None

        # TODO: This is a hack
        os.chdir(self.dir)

        text = inputBuffer.read()
        md = markdown.Markdown(extensions=['attr_list', 'meta'])
        html = md.convert(text)
        self.attributes = md.Meta
        self.defaultFit = self._getAttribute('fit', DEFAULT_FIT)
        self.defaultRotate = self._getAttribute('rotate', DEFAULT_ROTATE)
        self.defaultStart = self._getAttribute('start', DEFAULT_START)
        self.defaultEnd = self._getAttribute('end', DEFAULT_END)

        document = html5lib.parseFragment(html, namespaceHTMLElements=False)
        for e in document.iter():
            self.iter(e)

    """
    Check if file has been cached locally and if
    not cached, download from provided URL. Return
    download filename
    """
    def _cacheURL(self, url):
        pass

    """
    Get the number of pages in a PDF file
    """
    def _get_pdf_number_of_pages(self, filename):
        pass

    """
    Return an attribute with a default value of None
    """
    def _getAttribute(self, key, default=None):
        pass

    def _getMetadata(self):
        pass

    """
    Iterate through the elements in the spine HTML
    and generate self.bookmarks + self.files
    """
    def iter(self, element):
        pass

    def _existingBookmarkConfig(self):
        pass

    def _removeExistingBookmarks(self):
        pass

    def _flattenBookmarks(self):
        pass

    """
    Adds the existing bookmarks into the
    self.bookmarks list
    """
    def _add_existing_bookmarks(self):
        pass

    """
    Gets the last bookmark level at a given page number
    on the combined PDF
    """
    def _get_level_from_page_number(self, page):
        pass

    """
    Recursive method to read the old bookmarks (which are nested)
    and push them to self.oldBookmarks
    """
    def _iterate_old_bookmarks(self, pdf, startPage, bookmarks, level = 1):
        pass

    """
    Insert the bookmarks into the PDF file
    Ref: https://stackoverflow.com/a/18867646
    # TODO: Interleave this into the merge method somehow
    """
    def _insert_bookmarks(self, old_filename, outputFilename):
        pass

    """
    Merge the PDF files together in order
    and iterate through the old bookmarks
    as we're reading them
    """
    def _merge(self, output):
        pass

    """
    Main entrypoint to generate the final PDF
    """
    def generate(self, outputFilename, cleanup = False):
        pass
