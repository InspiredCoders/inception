import sys
import os
import pytest
sys.path.append(os.path.join(os.path.dirname(__file__),
                             os.pardir, "inception"))
import config


def test_type_read_config():
    config_file = os.path.join(os.path.dirname(__file__),
                               os.pardir, "inception",
                               "config.json")
    result = config.read_config(config_file)
    assert type(result) is dict


def test_type_get_mapping_dictionary():
    config_data = {
        "Documents": "docx, doc, pdf, xls, xlsx",
        "Music": "mp3, ogg, wav",
        "Pictures": "jpg, jpeg, png, bmp",
        "Videos": "mp4, mov, mkv",
        "torrent_files": "torrent",
        "linux_packages": "deb, rpm",
        "compressed": "zip, rar, tar.gz, tar",
        "Python Codes": "py, ipynb"
    }
    result = config.get_mapping_dictionary(config_data)
    assert type(result) is dict
