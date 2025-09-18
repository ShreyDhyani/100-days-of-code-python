## Day 2 — Python Exercises Summary

**Concepts Practised**

- **Python primitive data types**: `int`, `float`, `str`
- **Type errors, checking, conversion**: `type()`, `int()`, `float()`, `str.strip()`
- **Mathematical operations**: addition, multiplication, modulo, exponent basics
- **Number manipulation**: `round()` and precision
- **F-strings**: formatted output with expressions

### Scripts Overview

- **`type_check.py`**: Reads input and prints its Python type.
- **`square.py`**: Reads a number, converts to `float`, prints its square.
- **`age_in_months.py`**: Converts age in years (`int`) to months (`years * 12`).
- **`debug.py`**: Simple arithmetic with type conversion; prints age in 5 years.
- **`even_odd.py`**: Uses modulo `% 2` to classify an integer as Even/Odd.
- **`bmi.py`**: Calculates Body Mass Index as `weight / (height * height)` with rounding.
- **`tip.py`**: Splits a bill including tip among people; demonstrates percentage, rounding, and f-strings.

### How to Run

From this `day2` folder, run any script with Python 3 and follow the prompts:

```bash
python3 type_check.py
python3 square.py
python3 age_in_months.py
python3 debug.py
python3 even_odd.py
python3 bmi.py
python3 tip.py
```

### Notable Learnings Reflected in Code

- **Whitespace cleanup** before conversion via `.strip()` to avoid input errors.
- **Type conversion** before math: `int()`/`float()` on user input.
- **Rounding** to specific precision: `round(value, 4)`.
- **Concise conditionals** within f-strings (e.g., Even/Odd message).

### Example I/O

- `even_odd.py`
  - Input: `7`
  - Output: `Number is Odd`
- `bmi.py`
  - Inputs: `1.75`, `70`
  - Output: `Your BMI is 22.8571`
- `tip.py`
  - Inputs: `Bill: 120`, `People: 3`, `Tip: 15`
  - Output: `Tip: 18.0` and `Each person should pay: 46.0`

### Next Ideas

- Add input validation and friendly error messages.
- Extract computations into functions and add basic tests.
- Format currency for monetary outputs.
