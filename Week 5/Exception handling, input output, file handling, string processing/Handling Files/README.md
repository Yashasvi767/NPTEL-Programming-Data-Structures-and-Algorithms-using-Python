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
1. contents = fh.read()
```
Reads through file into name as a single string


```python
2. contents = fh.readline()
```
Reads only line into names-lines end with '\n', string includes '\n', unlike input()

```python
3. contents = fh.readlines()
```
Reads entire file as lists of strings, each string is one line, endling with '\n' 

```python
4. fh.seek(n)
```
moves pointer to position n

eg. 
```python 
block=fh.read(12)
```
reads a fixed number of characters

## End of file
- when fh.read() or fh.readlines() return empty string "", that means that the file has ended.

## Writing to a file
```python
1. fh.write(s)
```
write string s to file, returns number of characters written, include '\n' explicitly to go to a new line

```python
2. fh.writelines(l)
```
write a list of lines l to file, must include '\n' explicitly for each string

```python
3. fh.close()
```
 flushes output buffer and decouples file handle, all pending writes copied to disk

 ```python
4. fh.flush()
```
manually forces write to disk

# Examples
1. Copying a file
   ```python
   infile = open("input.txt", "r")
   outfile = open("output.txt","w")
   contents = infile.readlines()
   outfile.write(contents)
   infile.close()
   outfile.close()
   ```
