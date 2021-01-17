import argparse
from io import FileIO

from lxml import etree

parser = argparse.ArgumentParser()


def print_hi(name):
    print(f"Hi, {name}")
    return name


def load_dtd():
    dtd = etree.DTD(FileIO("schema/coverage-04.dtd"))
    return dtd


def xml_from_file(file_path):
    tree = etree.parse(file_path)
    print(
        "{} has {} lines.".format(
            file_path,
            len(list(tree.xpath("./packages/package/classes/class/lines/line"))),
        )
    )
    return tree


if __name__ == "__main__":
    parser.add_argument("file1", help="first file to check")
    parser.add_argument("file2", help="second file to check")
    args = parser.parse_args()
    print_hi("PyCharm")
    xml_def = load_dtd()
    xml1 = xml_from_file(args.file1)
    print("{} is valid: {}".format(args.file1, xml_def.validate(xml1)))
    xml2 = xml_from_file(args.file2)
    print("{} is valid: {}".format(args.file2, xml_def.validate(xml2)))
