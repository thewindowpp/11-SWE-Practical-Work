## Lab 120.3C - Pseudocode to flowcharts
### Overview

This lab asks you to analyse a moderately complex pseudocode example with nested control structures and convert it into a complete flowchart. This task will help you understand visual algorithm representation and how each part of your logic flows from one decision to another.

### Learning objectives
- Interpret pseudocode with compound conditions, nested branches, and loops
- Draw a logically accurate flowchart using standard symbols
- Apply top-down modularity by representing subroutines visually
```text
BEGIN Main
    INPUT n
    IF n < 2 THEN
        OUTPUT "Not prime"
    ELSE
        SET prime TO true
        FOR i FROM 2 TO sqrt(n)
            IF n MOD i = 0 THEN
                SET prime TO false
                BREAK
            ENDIF
        NEXT i
        IF prime THEN
            OUTPUT "Prime"
        ELSE
            OUTPUT "Not prime"
        ENDIF
    ENDIF
END Main
```
### Instructions
1. Use a digital drawing tool to create your flowchart, including:
- proper start/end symbols
- pallelograms for I/O
-diamonds for decisions (e.g. n < 2, n % i == 0)
- reactangles for processes (i = 2, prime = true, etc.)
- a looping structure for i from 2 to sqrt(n)
2. Annotate or group your subroutine visually.
3. Upload your flowchart to your forked GitHub repository.
4. Translate your flowchart into Python and test it with various inputs.