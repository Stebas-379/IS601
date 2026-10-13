# Dosa Restaurant Order Processor

## Description

This project processes restaurant order data stored in a JSON file. The program reads customer orders from an input file and generates two output files:

- customers.json
- items.json

## Design

The program uses Python and the json module to read order data from a file provided as a command-line argument.

Each order contains:

- Customer name
- Phone number
- Ordered items
- Item prices
- Notes

The program performs the following tasks:

1. Reads orders from a JSON file.
2. Creates customers.json containing customer phone numbers as keys and customer names as values.
3. Creates items.json containing item names as keys and objects containing the item price and total number of times ordered.
4. Writes the results to JSON files.

## Usage

Run the program from the terminal:

```bash
python process_orders.py example_orders.json
```

## Output Files

### customers.json

Stores customer phone numbers and names.

### items.json

Stores item information including price and total orders.

## Files

- process_orders.py
- example_orders.json
- customers.json
- items.json

## Requirements

- Python 3.x

## Author

Steven Espinoza

IS601 Midterm Project