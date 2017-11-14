from pyappveyordemo.extension import some_function
from nose.tools import assert_equal
import xmltodict

import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def send_mail(send_from, send_to, subject, text, files=None,
              server="smtp.live.com"):
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


    smtp = smtplib.SMTP(server, 587)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()




def test_some_function():
    send_mail("armando.amador@hotmail.com", ["armando.amador@hotmail.com"], "This is a test", "SOMETHING DUN FUCKED UP!")
    assert_equal(some_function(0, 0), 0)
    assert_equal(some_function(0, 42), 0)
    assert_equal(some_function(41, 2), 1)
    assert_equal(some_function(1, 2), 1)
