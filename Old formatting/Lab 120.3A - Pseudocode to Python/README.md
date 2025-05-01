## Lab 120.3B - Pseudocode to Python
### Overview

In this lab, you’ll convert moderately complex pseudocode into working Python. The pseudocode involves user input, validation, a loop with selection logic, and a function call. You’ll also include comments to show how the pseudocode maps to your Python.

### Learning objectives
- Translate nested pseudocode structures into Python using functions
- Apply defensive programming techniques (e.g. input validation)
- Use iteration, selection, and modular code

### Pseudocode to convert
```text
BEGIN Main
    SET count TO 0
    REPEAT
        INPUT num
        IF num >= 0 THEN
            CALL process_number(num)
            INCREMENT count
        ELSE
            OUTPUT "Negative number entered. Ending input."
        ENDIF
    UNTIL num < 0
    OUTPUT "Numbers processed: " + count
END Main

BEGIN process_number(x)
    IF x MOD 3 = 0 AND x MOD 5 = 0 THEN
        OUTPUT "FizzBuzz"
    ELSEIF x MOD 3 = 0 THEN
        OUTPUT "Fizz"
    ELSEIF x MOD 5 = 0 THEN
        OUTPUT "Buzz"
    ELSE
        OUTPUT x
    ENDIF
END process_number
```