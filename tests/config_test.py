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
    print(config_file)
    result = config.read_config(config_file)
    assert type(result) is dict
