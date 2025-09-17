# Day 1 — Python Basics

## Overview

You practiced Python fundamentals: printing, reading user input, string operations, f-strings, and using built-in functions like `len`. You also encountered small style and correctness considerations (semicolons, prompt punctuation, type conversion).

## Files

- `print.py`: Hello world print.
- `input.py`: Ask for a name and respond.
- `all_caps.py`: Read a word and print it in uppercase.
- `word_length.py`: Read a word and display its length in several ways.
- `main.py`: Simple story generator from multiple inputs.

## What you practiced

- Printing with `print()`
- Reading input with `input("prompt")`
- String concatenation vs f-strings
- Calling string methods like `.upper()`
- Using built-ins like `len()`
- Composing multiple inputs into one formatted output

## Debugging and style notes

- Prefer f-strings: `f"Word length is {len(word)}"`
- When concatenating non-strings, convert: `str(len(word))` (or use f-strings)
- `print("a", 1)` auto-inserts a space; `"a" + str(1)` does not
- `input()` returns a string; use `.strip()` if you need to trim whitespace
- `.upper()` only affects letters; numbers/symbols remain unchanged
- `len()` counts all characters, including spaces and punctuation
- Clean prompts and punctuation, avoid trailing semicolons (non-idiomatic in Python)

## How to run

Run any script from this folder:

```bash
python3 print.py
python3 input.py
python3 all_caps.py
python3 word_length.py
python3 main.py
```

## Example

```bash
$ python3 word_length.py
Enter a word to count its length.
hello
Word length is -> 5
Word length is -> 5
Word length is -> 5
```
