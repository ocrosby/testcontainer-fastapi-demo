import xml.dom.minidom


def beautify_junit_xml(xml_string: str, indent: int) -> str:
    """
    Beautify a JUnit XML string.
    """

    dom = xml.dom.minidom.parseString(xml_string)
    return dom.toprettyxml(indent=" " * indent)
