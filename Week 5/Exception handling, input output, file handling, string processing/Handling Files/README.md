# Disk Buffers
- Disk data is read/written in large blocks
- "Buffer" is temporary parking place for disk data

## Reading/writing disk data
- Open a file- create file handle to file on disk
   - Like setting up a buffer for the file
- Read and write operatios are to file handle
- Close a file
   - Write out buffer to disk (flush)
   - Disconnect file handle 

## Opening a file
```python
 fh = open("gcd.py","r")
```
- Read "r" : opens a file for reading only
- Write "w" : creates an empty file to write to 
- Append "a" : append to an existing file

## Read through file handle
```python
contents = fh.read()
```
- Reads through file into name as a single string

```python
contents = fh.readline()
```
- Reads onle line into names-lines end with '\n'
  - String includes '\n', unlike input()

```python
contents = fh.readlines()
```
- Reads entire file as lists of strings
  - Each string is one line, endling with '\n' 
