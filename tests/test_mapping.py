import pytest
import os
from tdms.main import Mapping, Color, UUIDEncoder


# Create a tables.txt file with the following content:
# table1
# table2
# table3
# For testing purposes

with open("tables.txt", "w") as f:
    f.write("table1\ntable2\ntable3")


def test_color_bold():
    c = Color("Hello")
    assert c.bold() == "\033[1mHello\033[0m"

def test_color_yellow():
    c = Color("Hello")
    assert c.yellow() == "\033[93mHello\033[0m"

def test_mapping_constructor():
    p1 = Mapping("tables.txt", "public", "include", "view", "myprefix_")
    assert p1.table_list_input == "tables.txt"
    assert p1.schema_list_input == "public"
    assert p1.prefix_value == "myprefix_"
    assert p1.rule_action == "include"
    assert p1.table_types == "view"

def test_mapping_constructor_invalid_rule_action():
    with pytest.raises(ValueError):
        Mapping("tables.txt", "public", "invalid", "view", "myprefix_")

def test_mapping_constructor_invalid_table_types():
    with pytest.raises(ValueError):
        Mapping("tables.txt", "public", "include", "invalid", "myprefix_")

def test_readTableList():
    p1 = Mapping("tables.txt", "public", "include", "view", "myprefix_")
    assert p1.readTableList() == ["table1", "table2", "table3"]

def CreateJSON():
    p1 = Mapping("tables.txt", "public", "include", "view", "myprefix_")
    p1.createJSON()
    assert os.path.exists("mapping.json")