# Strip Whitespace
```python
1. s.rstrip()
```
removes trailing whitespace

```python
2. s.lstrip()
```
removes leading whitespace

```python
3. s.strip()
```
removes leading and trailing whitespace

# Searching for text
```python
1. s.find(pattern)
```
returns first position in s where pattern occurs, -1 if no occurrence of pattern

```python
2. s.find(pattern, start, end)
```
search for pattern in slice s[start:end]
s.index(pattern), s.index(pattern,l,r)
pattern would be found, or raise ValueError if pattern not found

 # Search and replace
 ```python
s.replace(fromstr, tostr)
```
returns copy of s with each occurence of fromstr replaced by tostr

```python
s.replace(fromstr,tostr,n)
```
replace at most first n copies
