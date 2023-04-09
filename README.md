
# Badges
[![Test and coverage](https://github.com/Julio-M/tdms/actions/workflows/test-coverage.yaml/badge.svg?branch=main)](https://github.com/Julio-M/tdms/actions/workflows/test-coverage.yaml)

# Table of Contents
- [DMS - Table mapping generator](#dms---table-mapping-generator)
  - [Usage](#usage)
  - [Example](#example)
- [Options](#options)
- [Installation](#installation)
- [Test](#test)
- [Coverage](#coverage)
- [License](#license)

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

## Example

```bash
tdms -t tables.txt -s public -p myprefix_ -r include -y view
```

Output example:

```bash
Values used: 

Table List Input     Schema List Input    Prefix Value         Rule Action          Table Types         
--------------------------------------------------------------------------------------------------------
tables.txt           public               myprefix_            include              view                
                                                                                                        
Prefix rule added-> myprefix_ in front of -> table1
Prefix rule added-> myprefix_ in front of -> table2
Prefix rule added-> myprefix_ in front of -> table3
```

Table mapping file generated:

```json
{
  "rules": [
    {
      "rule-type": "transformation",
      "rule-id": "85",
      "rule-name": "fc7099f456104bef9e0f9b2f811b63ba",
      "rule-target": "table",
      "object-locator": {
        "schema-name": "public",
        "table-name": "table1"
      },
      "rule-action": "add-prefix",
      "value": "myprefix_"
    },
    {
      "rule-type": "selection",
      "rule-id": "85",
      "rule-name": "fc7099f456104bef9e0f9b2f811b63ba",
      "object-locator": {
        "schema-name": "public",
        "table-name": "table1"
      },
      "rule-action": "include",
      "filters": []
    },
    {
      "rule-type": "transformation",
      "rule-id": "925",
      "rule-name": "fc7099f456104bef9e0f9b2f811b63ba",
      "rule-target": "table",
      "object-locator": {
        "schema-name": "public",
        "table-name": "table2"
      },
      "rule-action": "add-prefix",
      "value": "myprefix_"
    },
    {
      "rule-type": "selection",
      "rule-id": "925",
      "rule-name": "fc7099f456104bef9e0f9b2f811b63ba",
      "object-locator": {
        "schema-name": "public",
        "table-name": "table2"
      },
      "rule-action": "include",
      "filters": []
    },
    {
      "rule-type": "transformation",
      "rule-id": "609",
      "rule-name": "fc7099f456104bef9e0f9b2f811b63ba",
      "rule-target": "table",
      "object-locator": {
        "schema-name": "public",
        "table-name": "table3"
      },
      "rule-action": "add-prefix",
      "value": "myprefix_"
    },
    {
      "rule-type": "selection",
      "rule-id": "609",
      "rule-name": "fc7099f456104bef9e0f9b2f811b63ba",
      "object-locator": {
        "schema-name": "public",
        "table-name": "table3"
      },
      "rule-action": "include",
      "filters": []
    }
  ]
}
```

# Options

| Option | Description | Example | Required |
| --- | --- | --- | --- |
| `-t` | The file that contains the list of tables to be mapped | `tables.txt` | Yes |
| `-s` | The schema that the tables are in | `public` | Yes |
| `-p` | The prefix value to be added to the table names | `myprefix_` | No |
| `-r` | The rule action to be used | `include` | Yes |
| `-y` | The table types to be used | `view` | Yes |


# Test

To run the `tests`, in the root of the project, run:

```bash
make test
```

# Coverage
To run the `coverage`, in the root of the project, run:
  
```bash
make coverage
```

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details