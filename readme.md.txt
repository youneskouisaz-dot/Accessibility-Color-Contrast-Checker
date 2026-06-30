# Accessibility Color Contrast Checker

## Project Description

This project is a simple Python application that checks the contrast ratio between a text color and a background color using hexadecimal color codes.

The program calculates the contrast ratio and determines whether the selected colors meet the Web Content Accessibility Guidelines (WCAG) for accessibility.

## Why This Project Matters

Many people with low vision, color blindness, or other visual impairments have difficulty reading websites with poor color contrast.

This program helps demonstrate how developers can test color combinations to create websites that are easier for everyone to read.

## Technologies Used

- Python 3
- Functions
- User Input
- Conditional Statements
- Mathematical Calculations

## How to Run

### Requirements

- Python 3 installed

### Steps

1. Download or clone this repository.
2. Open `contrast_checker.py` in Python IDLE.
3. Press **F5** (Run Module).
4. Enter a text color and a background color using hexadecimal color codes.

Example:

Text color:
```
#000000
```

Background color:
```
#FFFFFF
```

Example output:

```
Contrast Ratio: 21.00:1
Passes WCAG AAA standard.
```

## Example Results

### Example 1

Text Color:
```
#FFFFFF
```

Background Color:
```
#FFFFFF
```

Output:
```
Contrast Ratio: 1.00:1
Fails accessibility contrast standards.
```

### Example 2

Text Color:
```
#000000
```

Background Color:
```
#FFFFFF
```

Output:
```
Contrast Ratio: 21.00:1
Passes WCAG AAA standard.
```

## Project Files

- `contrast_checker.py` – Python program
- `README.md` – Project documentation
- `Project_Brief.md` – One-page project brief
- `output.png` – Screenshot showing the program running

## Author

Created as a Computer Science course project on digital accessibility.