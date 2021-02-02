# logger - The simplest Python logging out there!

With logger, you can track events that happen when software runs with just one line of code. logger is super easy to use and handles everything for you. Just specify log filename , message that you want to pass ,level(importance which developer ascribes to the event;), and format of logs(which is totally Optional) and the rest is done for you.

# Usage
In the following paragraphs, I am going to describe how you can get and use Scrapeasy for your own projects.

# Getting it

To download logger, either fork this github repo or simply use Pypi via pip.

$ pip install logger

# Using it

logger was programmed with ease-of-use in mind. First, import loggerClass from logger

from logger import loggerClass 

# Print onScreen

it will print the message on console.

loggerClass.WritetoScreen(loggerClass,logging.INFO,"testing...",'%(levelname)s:%(message)s')

--> logging.INFO - level or severity of events they are used to track

--> "testing..." - Message

--> '%(levelname)s:%(message)s' - specify the order, structure, and content of the log message.




it will store the message in logFile.

loggerClass.Writetofile(loggerClass,'sample.log',logging.WARNING,"testing...",'%(asctime)s:%(levelname)s:%(message)s')

--> 'sample.log' - Log Filename 

--> logging.WARNING - level or severity of events they are used to track

--> "testing..." - Message

--> '%(asctime)s:%(levelname)s:%(message)s' - specify the order, structure, and content of the log message.

# License
MIT License

Copyright (c) 2021 PAYAL KUTANA

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Hire us: Software Entwickler in Zürich!
