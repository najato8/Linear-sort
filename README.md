# Linear Sort: Learning Progression

A small Python exercise for learning how counting-based sorting works, one step at a time.

## Current Progress

The `sort(T)` function currently:

1. Finds the largest value in the input list.
2. Creates a frequency table with one position for each value from `0` to that maximum.
3. Counts how many times each value appears.

For the example in `linear-sort.py`:

```python
[7, 1, 3, 1, 2, 4, 1, 5, 2, 4, 3]
```

The function prints this frequency table:

```text
[0, 3, 2, 2, 2, 1, 0, 1]
```

The index is the value, and the number at that index is its frequency. For example, the value `1` appears three times.

## What I Am Learning

- How to traverse a list and find its maximum.
- How to represent frequencies with a second list.
- How nested loops can compare a straightforward approach with a more efficient one.
- Why the range of input values affects the memory needed by counting-based algorithms.


## Run

With Python installed, run:

```bash
python linear-sort.py
```
