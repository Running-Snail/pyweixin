import HTMLParser
import xml.etree.ElementTree as ET


def unescape(text):
    if isinstance(text, str):
        text = text.decode('utf-8')
    return HTMLParser.HTMLParser().unescape(text)


def xml2dict(xml_string):
    ret = {}
    root = ET.fromstring(xml_string)
    for child in root:
        if child.text is not None:
            ret[child.tag] = child.text
        else:
            ret[child.tag] = ''
    return ret
