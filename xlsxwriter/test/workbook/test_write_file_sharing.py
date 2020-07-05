###############################################################################
#
# Tests for XlsxWriter.
#
# Copyright (c), 2013-2020, John McNamara, jmcnamara@cpan.org
#

import unittest
from ...compatibility import StringIO
from ...workbook import Workbook


class TestWriteReadonlyRecommended(unittest.TestCase):
    """
    Test the Workbook _write_workbook_pr() method.

    """

    def setUp(self):
        self.fh = StringIO()
        self.workbook = Workbook()
        self.workbook._set_filehandle(self.fh)

    def test_write_file_sharing_default(self):
        """Test the _write_workbook_pr() method with default settings"""

        self.workbook._write_file_sharing()

        exp = ""
        got = self.fh.getvalue()

        self.assertEqual(exp, got)

    def test_write_file_sharing_false(self):
        """Test the _write_workbook_pr() method with explicit False"""

        self.workbook.set_readonly_recommended(False)
        self.workbook._write_file_sharing()

        exp = ""
        got = self.fh.getvalue()

        self.assertEqual(exp, got)

    def test_write_file_sharing_true(self):
        """Test the _write_workbook_pr() method with explicit True"""

        self.workbook.set_readonly_recommended(True)
        self.workbook._write_file_sharing()

        exp = """<fileSharing readOnlyRecommended="1"/>"""
        got = self.fh.getvalue()

        self.assertEqual(exp, got)

    def tearDown(self):
        self.workbook.fileclosed = 1
