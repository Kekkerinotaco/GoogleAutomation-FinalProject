#!/usr/bin/env python3

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer


def generate_report(file_name, title, file_info):
    """ Script builds report file """
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(file_name)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(file_info, styles["BodyText"])
    empty_line = Spacer(1, 10)
    report.build([report_title, empty_line, report_info, empty_line])
