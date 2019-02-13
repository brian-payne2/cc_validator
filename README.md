# cc_validator
Python utility to parse potential credit card numbers. Checks the following conditions::
1. It must start with a 4, 5 or 6 
2. It must contain exactly 16 digits
3. It must only consist of digits (0-9)
4. It may have digits in groups of 4, separated by one hyphen "-"
5. It must NOT use any other separator like ' ' , '_', etc. 
6. It must NOT have 4 or more consecutive repeated digits

### Requirements
Python 3.6 installed and configured in your path

### Use
1. Navigate your CLI to the directory where this script is cloned.

2. Run the script

```
python CSV_Importer csv_file_name.csv
```

3. Enter the number of CC numbers to parse

4. Enter each CC number to parse, one per line.

This will output if each number entered is valid or not.

## Built With
* Python 3.6

## Author
Brian Payne - [brian.payne2@gmail.com](mailto:brian.payne2@gmail.com)
