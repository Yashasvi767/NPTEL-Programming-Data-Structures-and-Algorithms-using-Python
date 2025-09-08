# When things go wrong
- Some errors are anticipated others are unexpected.
- The predictable errors are called exception.
- Contingency plan - exception handling

# Types of errors
- Some errors while code is executing (run-time errors)
  
1. Name used before values is defined
   NameError: name 'x' is not defined
2. Divison by zero in arithmetic expression
   ZeroDivisionError: divison by zero
3. Invalid index error

# Handling exceptions

```python
try:
...   //(code where error may occur)
...
except IndexError:
...   //(what to do if IndexError occurs)
except (NameError, KeyError)
...   //(common code to handle multiple errors)
except:
...   //(catch all other exceptions)
else:
...   //(Execute if try terminates normally, no errors)
```

Traditional approach
```python
if b in scores.keys():
  scores[b].append(s)
else:
  scores[b]=[s]
```

Using exceptions
```python
try:
  scores[b].append(s)
except keyError:
  scores[b] = [s]
```


   
