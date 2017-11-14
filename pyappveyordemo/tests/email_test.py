import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def send_mail(send_from, send_to, subject, text, files=None,
              server="webmail.stats.com"):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)


    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()


if __name__ == "__main__":
    send_mail("aamador@stats.com", ["aamador@stats.com"], "This is a test", "SOMETHING DUN FUCKED UP!", files=["test.txt"])


















































# ##############################################################
# # Variable values from configuration.py (config)
# # *** Notification constants
# email_from = 'aamador@stats.com'
# email_to = ['aamador@stats.com']  # , 'jsiddall@stats.com', 'aamador@stats.com']
# email_subject = 'Automated Database Testing Results'
# smtp_server = 'webmail.stats.com'
# # *** End of Notification section ****

# # *** Constants used throughout the testing modules ***
# relative_log_directory = '../../logs'
# ##############################################################


# from smtplib import SMTP
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # Since all files in the current package are test files, with the exception of "this" file and __init__.py,
# # a list is created of file names to NOT include in from the tests package
# # To be clear, if a test module should NOT be executed, ADD the file name with extension to the following list
# test_omission_filter = ['__init__.py', '__pycache__', 'soccer_qsl_team_benchmark_report_tests.py']

# # variables used for formatting and storing test result contents in an html format
# base_table_header = '<table border=1 bordercolor=black cellspacing=0 cellpadding=5>\n ' \
#                     '<tr>\n<th width=400>Test</th>\n'
# time_column_headers = '<th>Start Time</th>\n<th>End Time</th>\n'
# error_column_header = '<th>Error Count</th>\n'
# # list_table_header will be used for the Pass and Exception list as they have the same columns
# list_table_header = base_table_header + time_column_headers + '</tr>\n'
# fail_list_table_header = base_table_header + time_column_headers + error_column_header + '</tr>\n'
# table_footer = '</table>'
# exception_list = ['<h2 style="color:red;">Exception</h2>', list_table_header]
# fail_list = ['<h2 style="color:orangered;">Fail</h2>', fail_list_table_header]
# pass_list = ['<h2 style="color:green;">Pass</h2>', list_table_header]
# omission_list = ['<h2 style="color:blue;">Omitted</h2>', base_table_header]
# # Add all the py file names in the test_omission_filter to the omission list, formatted as an html table row
# # omission_list.extend('<tr><th align=left>' + test.split('.py')[0] + '</th></tr>' for test in test_omission_filter[2:])

# # storing the testing start time in a variable to be used later on for test result and logging purposes
# # test_suite_start_time = strftime('%I:%M:%S %p')


# # Code block that appends to the exception_list, fail_list, pass_list and omission_list lists
# # Not included here
# # 		code
# # 		code
# # 		code



# try:
#     # Configure an email message with an html body
#     email_message = MIMEMultipart()
#     email_message['From'] = email_from
#     email_message['To'] = ', '.join(email_to)
#     email_message['Subject'] = email_subject
#     # Initial part of email text stating some overall Test Suite data
#     email_text_msg_header = '<table>' + \
#                             '<tr><th align=left>Database</th><td>' + \
#                             str(config.db_alias.split('_USR')[0].lower()) + '</td></tr>' + \
#                             '<tr><th align=left>Test Suite Start Time</th><td>' + test_suite_start_time + \
#                             '</td></tr>' + \
#                             '<tr><th align=left>Test Suite End Time</th><td>' +strftime('%I:%M:%S %p') + \
#                             '</td></tr>' + \
#                             '</table>'
#     # Take the testing status lists and create a html page string
#     # out of all the messages, which will be the text of the email
#     email_text = "<html><body>This is a test</body></html>"


#     # """'<html>\n<body>\n' + \
#     #                 '\n<br>\n' + \
#     #                 email_text_msg_header + \
#     #                 '\n<br>\n<br>\n<br>\n' + \
#     #                 '\n'.join(exception_line for exception_line in exception_list) + \
#     #                 '\n<br>\n' + \
#     #                 '\n'.join(fail_line for fail_line in fail_list) + \
#     #                 '\n<br>\n' + \
#     #                 '\n'.join(pass_line for pass_line in pass_list) + \
#     #                 '\n<br>\n' + \
#     #                 '\n'.join(omission_line for omission_line in omission_list) + \
#     #                 '</body>\n</html>'"""
#     email_message.attach(MIMEText(email_text, 'html'))

#     # Create email attachment, which is the log of these test results
#     log_path_and_file = os_curdir + '\\' + config.relative_log_directory + '\\' + module_base_name + '.' + \
#                         str(datetime.today().strftime('%m-%d-%Y')) + '.log'
#     log_file_object = open(log_path_and_file, 'r')
#     email_file_attachment = MIMEText(log_file_object.read())
#     log_file_object.close()

#     email_file_attachment_name = module_base_name + '.' + str(datetime.today().strftime('%m-%d-%Y')) + '.log'
#     email_file_attachment.add_header("Content-Disposition", "attachment", filename=email_file_attachment_name)
#     email_message.attach(email_file_attachment)
# except Exception as exc:
#     logger.error(type(exc).__name__ + ' exception was caught in the notification section', exc_info=True)
# finally:
#     # Configure mail server and send the email with the message and log file attachment
#     smtp_server = SMTP(smtp_server)
#     smtp_server.send_message(email_message)
#     smtp_server.quit()
#     print("Yay")