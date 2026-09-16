# Exercise 2: Lambdas, Higher-Order Functions, Closures and List Comprehension

Programming Languages Structure (מבנה שפות תוכנה), Exercise 2.

This exercise practices using Python's built-in higher-order functions (`map`, `filter`, `functools.reduce`) and writing higher-order functions and closures yourself. Unless a question says otherwise, every solution is written in a functional style.

All solutions are in [closureListComprehension.py](closureListComprehension.py).

## Running

Requires Python 3.9 or later. Only the standard library is used (`functools`, `time`, `datetime`, `decimal`, `math`).

```bash
python closureListComprehension.py
```

When the file loads, it prints the timing comparison from question 1, the sum from question 2 and the Armstrong checks from question 3. Then `main()` asks for input three times: for question 3c, question 5b and question 7c.

## Questions

### 1. Linear function as a lambda

`Y = lambda x: x/2 + 2` implements the function Y = x/2 + 2.

1. Apply `Y` with `map` to the list 0–10000 to build a new list (`new_list`).
2. Sum the new list with a higher-order function (`reduce`).
3. Compare how long the `reduce` sum takes with an imperative `for` loop, using `time.perf_counter`.
4. Do the whole thing with a single `reduce` call that both calls `Y` and sums the results.

### 2. Splitting and folding even and odd numbers

Split the list 1–1000 into `even_list` and `odd_list` with `filter`.

1. Two lambdas:
   - `lambda_func_1` multiplies the running product by the next even number (1·2, then ·4, then ·6, and so on).
   - `lambda_func_2` uses the linear function from question 1: `x/2 + 2 + next`, where `x` is the running total and `next` is the next odd number.
2. Apply the matching lambda to each list with `reduce`.
3. Sum the two results with `reduce`. The even product has about 1,285 digits, which is too large to add to the float that the odd fold returns, so both are converted to `Decimal` first.

### 3. Armstrong numbers

A positive integer with k digits is an Armstrong number if the sum of its digits, each raised to the power k, equals the number itself. For example, 1³ + 5³ + 3³ = 153.

| Part | Function | Description |
|------|----------|-------------|
| a | `is_armstrong(n)` | Pure function; returns `True` if `n` is an Armstrong number. |
| b | `armstrong_range(n1, n2)` | Returns every Armstrong number from `n1` to `n2`. |
| c | `main()` | Reads a number and prints `armstrong_range(1, n)`. Input that is not a positive integer prints `invalid input`. |

### 4. Date generator

| Part | Function | Description |
|------|----------|-------------|
| a | `date_generator(date_str, num_of_dates, num_of_jumps)` | Takes a Gregorian date string (`YYYY-MM-DD`), the number of dates to return and the number of days between dates. Returns the list of dates, built with `map`. |
| b | — | Optional: the same for Hebrew dates. Not implemented. |

### 5. Power functions and a Taylor series

| Part | Function | Description |
|------|----------|-------------|
| a | `power_function(exponent)` | Returns a function that takes a base and returns `base ** exponent`. |
| b | `generate_power_map(n)` | Returns a `map` object of power functions [x⁰, x¹, …, xⁿ⁻¹]. `main()` reads `n`, prints the object's type, reads an integer base and prints the tuple of results. Invalid input prints `invalid input`. |
| c | `taylor_e(x, n)` | Approximates eˣ = Σ xⁿ/n! using the parts above, without loops or lists. |

Example from the assignment:

```
Enter number of powers:
5
<class 'map'>
Enter base:
2
(1, 2, 4, 8, 16)
```

### 6. Task manager (closure)

`task_manager()` keeps a dictionary of tasks inside a closure and returns a dictionary of functions that work on it. The key is the task name and the value is its status: `incomplete`, `in progress` or `complete`.

| Key | Description |
|-----|-------------|
| `add_task(task, status="incomplete")` | Adds a task, `incomplete` by default. |
| `get_tasks()` | Returns the current tasks dictionary. |
| `complete_task(task)` | Sets the task's status to `complete`. |

```python
tasks_manager = task_manager()
tasks_manager['add_task']("Write email")
tasks_manager['add_task']("Shopping", "in progress")
tasks_manager['add_task']("Homework")
print(tasks_manager['get_tasks']())
# {'Write email': 'incomplete', 'Shopping': 'in progress', 'Homework': 'incomplete'}

tasks_manager['complete_task']("Write email")
print(tasks_manager['get_tasks']())
# {'Write email': 'complete', 'Shopping': 'in progress', 'Homework': 'incomplete'}
```

### 7. Building a pipeline

**a. Text functions** (pure):

| Function | Description |
|----------|-------------|
| `clean_text(text)` | Strips surrounding whitespace (`strip`). |
| `capitalize_text(text)` | Capitalizes the first letter of each word (`title`). |
| `add_stars(text)` | Wraps the text in asterisks. |

**b. Pipeline functions** (no loops or recursion):

| Function | Description |
|----------|-------------|
| `create_pipeline()` | Returns the identity function, the base of the pipeline. |
| `add_to_pipeline(pipeline_fn, new_fn)` | Returns a new function that composes the two: `new_fn(pipeline_fn(x))`. |

**c. Main script:** creates a pipeline, adds the three text functions in order, reads a string and prints the result. Empty or whitespace-only input prints `invalid input`.

Example from the assignment:

```
enter text:
hello functional world
***Hello Functional World***
```
