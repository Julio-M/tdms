
# Badges
[![CI](https://github.com/Julio-M/tdms/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/Julio-M/tdms/actions/workflows/test-coverage.yaml)

# DMS - Table mapping generator

This is a tool to generate table mapping files for the DMS (Data Migration Service)

Pre-requisites:

- Python 3.6
- A `.txt` file with the tables

e.g. `tables.txt`:

```txt
table1
table2
table3
```

## Usage

Type `tdms -h` to see the help:

```bash
tdms -h

usage: tdms [-h] -t TABLE_LIST_INPUT -s SCHEMA_LIST_INPUT [-p PREFIX_VALUE] -r RULE_ACTION -y TABLE_TYPES

Create a table mapping json file for DMS

options:
  -h, --help            show this help message and exit
  -t TABLE_LIST_INPUT,  --table_list_input TABLE_LIST_INPUT
                        The file that contains the list of tables to be mapped
  -s SCHEMA_LIST_INPUT, --schema_list_input SCHEMA_LIST_INPUT
                        The schema that the tables are in
  -p PREFIX_VALUE,      --prefix_value PREFIX_VALUE
                        The prefix value to be added to the table names
  -r RULE_ACTION,       --rule_action RULE_ACTION
                        The rule action to be used
  -y TABLE_TYPES,       --table_types TABLE_TYPES
                        The table types to be used
```

# Test

To run the tests, type `pytest` in the root of the project.