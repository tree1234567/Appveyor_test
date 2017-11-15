import xmltodict, smtplib, os, sys

from urllib.request import urlopen
from pyappveyordemo.extension import some_function
from nose.tools import assert_equal
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
    smtp.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
    smtp.starttls() #Puts connection to SMTP server in TLS mode
    smtp.ehlo()
    smtp.login('armando.amador@hotmail.com', '97znwftp6!')

    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()

def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj



def test_some_function():
    storedDict = eval(open("C:\\projects\\appveyor-test\\pyappveyordemo\\tests\\my_dict.txt", "r").read())  
    
    flag = False

    for key, value in storedDict.items():
        sys.stdout.write("Testing Url: %s" % key)
        with urlopen(key) as conn_2:
            string = conn_2.read().decode('utf-8')
            
            string = re.sub('<apiReturn.*<apiResults>','',string,flags=re.DOTALL)
            string = string.replace('</apiResults></apiReturn>', "")
            # print(string_2)
            check =  computeMD5hash(string)

            if check == value["hash"]:
                sys.stdout.write("PASSED: %s" % key)
            
            else:
                xml_to_dict = xmltodict.parse(string)
                ordered_dict = ordered(xml_to_dict)
                ordered_dict_hash = computeMD5hash(str(ordered_dict))
                if (ordered_dict_hash == value[orderedObjecthash]):
                    sys.stdout.write("PASSED: %s" % key) 
                else:
                    sys.stdout.write("FAILED: %s" % key)
                    flag = True
    # test_extension.py
    # cwd = os.path.dirname(__file__)
    if flag:
        send_mail("armando.amador@hotmail.com", ["armando.amador@hotmail.com"], "This is a test", "SOMETHING DUN FUCKED UP!")        
        assert_equal(0,1)
        
    else:
        assert_equal(0,0)
