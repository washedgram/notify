# notify

Basic Python script for sending toast notifications on Windows, macOS, or Linux. If you're like me, you'd rather see a nice little disappearing notification on your computer screen to update you on a script's progress instead of watching the console all the time, so I made this to cover all my bases (since I alternate regularly between working on my PC, MacBook, and lab servers).

For Linux to work you need to make a Slack webhook to receive notifications. You can find more information on how to do that [here](https://slack.com/help/articles/115005265063-Incoming-Webhooks-for-Slack).

## Installation and usage

0. Install Python / Pip
1. Install the rest of the python packages if you don't already have them
2. Paste webhook in line 3 if necessary

To use in another program, import the function:

```python
from notify import notify
```

The function takes title (top row) and body (bottom row) arguments respectively. 

```python
notify('Hello world', 'this will be a notification!') 
```

The script file in this repo has an example function call (commented out) when ran in isolation. 

This repository is populated with an `__init__.py` file already, so calling this function in other directories should work out of the box. If you're having trouble importing the folder with this script, you can insert the path at the beginning of your file (after importing everything else) and then import the function.

```python
import sys
sys.path.insert(0, 'path/to/cloned/repo/folder/notify/')
from notify import notify

```

## Questions?

Figure it out.
