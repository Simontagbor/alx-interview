# 0x01. Lockboxes
`Algorithm` ` Python `

## Task
### 0. Lockboxes
I this Task I wrote a method that determeines if all boxes can be opened

#### Output
```
simontagbor@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

simontagbor@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
simontagbor@ubuntu:~/0x01-lockboxes$
```
