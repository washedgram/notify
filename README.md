# notify

Basic python function for sending toast notifications on Windows or macOS

## Installation and usage

0. Install Python 
1. Install `platform` (macOS and Windows) and `win10toast` (Windows only)

To use in another program, import the function:

```
from notify import notify
```

The function takes title (top row) and body (bottom row) arguments respectively; you should be able to feed in any type of string. 

```
notify('Hello', 'world') # should be able to feed in pretty much whatever inputs you want
```

The python file in this repo has an example function call when ran in isolation; comment out this line if you're only calling it in other files.

## Questions?

Don't contact me.
