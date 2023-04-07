import pytest
import os
from tdms.main import Mapping, Color, UUIDEncoder
import argparse


# Create a tables.txt file with the following content:
# table1
# table2
# table3
# For testing purposes

with open("tables.txt", "w") as f:
    f.write("table1\ntable2\ntable3")

    print("Table list: ")
    with open("tables.txt", "r") as f:
        print(f.read())

def test_color_bold():
    c = Color("Hello")
    assert c.bold() == "\033[1mHello\033[0m"

def test_color_yellow():
    c = Color("Hello")
    assert c.yellow() == "\033[93mHello\033[0m"

def test_mapping_init():
    with pytest.raises(TypeError):
        Mapping()

def test_mapping_constructor():
    p1 = Mapping("tables.txt", "public", "include", "view", "myprefix_")
    assert p1.table_list_input == "tables.txt"
    assert p1.schema_list_input == "public"
    assert p1.prefix_value == "myprefix_"
    assert p1.rule_action == "include"
    assert p1.table_types == "view"

def test_mapping_printTable():
    p1 = Mapping("tables.txt", "public", "include", "view", "myprefix_")
    assert p1.printTable() == True

# Test pring table if table path is a full path
def test_mapping_printTable_full_path():
    p1 = Mapping("/home/user/tables.txt", "public", "include", "view", "myprefix_")
    assert p1.printTable() == True

def test_mapping_printTable_no_prefix():
    p1 = Mapping("tables.txt", "public", "include", "view")
    assert p1.printTable() == True

def test_mapping_constructor_invalid_rule_action():
    with pytest.raises(ValueError):
        Mapping("tables.txt", "public", "invalid", "view", "myprefix_")

def test_mapping_constructor_invalid_table_types():
    with pytest.raises(ValueError):
        Mapping("tables.txt", "public", "include", "invalid", "myprefix_")

def test_mapping_readTableList():
    p1 = Mapping("tables.txt", "public", "include", "view", "myprefix_")
    assert p1.readTableList() == ["table1", "table2", "table3"]

# General rule uses randmon_ids to generate unique id'sm how to test this?
def test_mapping_general_rules():
    p1 = Mapping("tables.txt", "public", "include", "view")
    unique_id = p1.general_rules(0, 100)["rule-name"]

    assert p1.general_rules(0, 100) == {
        "rule-type": "selection",
        "rule-id": '100',
        "rule-name": unique_id,
        "object-locator": {
            "schema-name": "public",
            "table-name": "table1"
        },
        "rule-action": "include",
        "filters": []
    }

def test_mapping_prefix_rules():
    p1 = Mapping("tables.txt", "public", "include", "view", "myprefix_")
    unique_id = p1.prefix_rules(0, 100)["rule-name"]

    assert p1.prefix_rules(0, 100) == {
        "rule-type": "transformation",
        "rule-id": '100',
        "rule-name": unique_id,
        "rule-target": "table",
        "object-locator": {
            "schema-name": "public",
            "table-name": "table1"
        },
        "rule-action":"add-prefix",
        "value": "myprefix_"
    }

def test_mapping_createjson():
    # Test if it creates a json file
    p1 = Mapping("tables.txt", "public", "include", "view", "myprefix_")
    p1.createJSON()
    assert os.path.exists("table_mapping.json") == True
    os.remove("table_mapping.json")

def test_main_instance():
    # Create an instance of the ArgumentParser class
    parser = argparse.ArgumentParser()
    assert isinstance(parser, argparse.ArgumentParser) == True

    # Create an instance of the Mapping class
    mapping = Mapping("tables.txt", "public", "include", "view", "myprefix_")
    assert isinstance(mapping, Mapping) == True


def test_main_right_arguments():
    # Test if it creates an instance of hte mapping class
    os.system("python3 tdms/main.py -t tables.txt -s public -p myprefix_ -r include -y view")
    assert os.path.exists("table_mapping.json") == True
    os.remove("table_mapping.json")

def test_main_wrong_arguments():
    # Test if it creates an instance of hte mapping class
    os.system("python3 tdms/main.py -t tables.txt -s public -p myprefix_ -r include -y view -z")
    assert os.path.exists("table_mapping.json") == False

def test_main_except_valueerror():
    with pytest.raises(Exception) as e:
        raise e(os.system("python3 tdms/main.py -t tables.txt -s public -p s -r include -y s"))