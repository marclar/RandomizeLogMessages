# "RandomizeLogMessages" for SublimeText 2

This package looks for log messages in your code and appends a randomized string to help during debugging.

For example:

```
console.log('My log message');
```

becomes:

```
console.log('My log message (6785428)');
```

... which makes it much easier to search your codebase from your logs.


## NOTES:

* This plugin only looks in *.js files.
* It looks for calls to `log` wherein the first parameter is surrounded by SINGLE quotes.
* It appends a random 7-digit number in parentheses.
* Feel free to edit RandomizeLogMessages.py for your specific needs.


## License

All of RandomizeLogMessages is licensed under the MIT licence.

  Copyright (c) 2013 Michael Kane

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.