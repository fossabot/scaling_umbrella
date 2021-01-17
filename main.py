import argparse
from io import FileIO

from lxml import etree
parser = argparse.ArgumentParser()


def print_hi(name):
    print(f'Hi, {name}')
    return name


def load_dtd():
    dtd = etree.DTD(FileIO('schema/coverage-04.dtd'))
    print(dtd)
    return dtd


def xml_from_file(file_path):
    tree = etree.parse(file_path)
    print(file_path, etree.tostring(tree.getroot()))
    return tree


def validate_xml(dtd, xml):
    print(dtd.validate(xml))


if __name__ == '__main__':
    parser.add_argument('file1', help='first file to check')
    args = parser.parse_args()
    print_hi('PyCharm')
    dtd = load_dtd()
    xml = xml_from_file(args.file1)
    validate_xml(dtd, xml)

