

#!/usr/bin/env python3

import os
import datetime
import reports
import emails

current_date = datetime.datetime.now().strftime('%Y-%m-%d')

def generate_pdf(path):
    pdf = ""
    files = os.listdir(path)
    for file in files:
        if file.endswith(".txt"):
            with open(os.path.join(path, file), 'r') as f:
                inline = f.readlines()
                name = inline[0].strip()
                weight = inline[1].strip()
                pdf += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
                # a blank line after each fruit

    return pdf

# Call the main method which will process the data and call the generate_report method from the reports module
if __name__ == "__main__":
    path = "supplier-data/descriptions/"
    title = "Process Report for {}".format(current_date)
    # Generate the package for pdf body
    package = generate_pdf(path)
    reports.generate_report("/tmp/processed.pdf", title, package)

    # Generate email information
    sender = "automation@example.com"
    receiver = "student-03-8782c17e81d1@example.com"  # Replace with the actual recipient's email
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = "/tmp/processed.pdf"

    # Generate email for the online fruit store report and pdf attachment
    message = emails.generate_email(sender, receiver, subject, body, attachment)

    # Send the email (you should have the send_email function implemented)
    try:
        emails.send_email(message)
        print("Email sent successfully.")
    except Exception as e:
        print("Email sending failed:", str(e))
