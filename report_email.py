#!/usr/bin/env python3

import os
import datetime
import reports
import emails

date = datetime.datetime.now().strftime("%Y-%m-%d")


def main():
    """ Script generates PDF file and emails it"""
    descr_path = "supplier-data/descriptions/"
    title = "Processed Update on" + date
    pdf_summary = ""
    for root, folders, files in os.walk(descr_path):
        for file in files:
            print(file)
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                pdf_file = generate_pdf(file_path)
                pdf_summary += pdf_file
    reports.generate_report("/tmp/processed.pdf", title, pdf_summary)
    make_email()


def generate_pdf(file_path):
    """ Function creates text data for PDF file"""
    with open(file_path, "r") as file:
        data = file.readlines()
        name = data[0].strip()
        weight = data[1].strip()
        pdf = "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
        return pdf


def make_email():
    """ Function sends the email """
    sender = "automation@example.com"
    reciever = "student-01-9605b3a73d76" + "@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email"
    attachment = "/tmp/processed.pdf"

    message = emails.generate_email(sender, reciever, subject, body, attachment)
    emails.send_email(message)


main()
