# python_text_search
# Full Text Search Implementation  using Python 

# "BlazeIndex" exposes a very simple command line interface for storing and searching documents:
There are 2 commands:

$ blazeindex add '{"id":"123","text":"We are going to build a HUUUUUGEEE
wall"}'
Added '{"id":"123","text":"We are going to build a HUUUUUGEEE wall"}'
$ blazeindex add '{"id":"124","text":"Another brick in the wall"}'
Added '{"id":"124","text":"Another brick in the wall"}'
Clients post a unique identifier("id") with each document. “text” field contains all the text to be indexed.

$ blazeindex query 'WALL'
{"count":1,"documents":[{"id":"123","text":"We are going to build a
HUUUUUGEEE wall"}]}
$ blazeindex query 'WALL BRICK'
{"count":2,"documents":[{"id":"123","text":"We are going to build a
HUUUUUGEEE wall"}, 
 {"id":"124","text":"Another brick in the
wall"}]}

Search command returns all documents that match the query text as a json result 
The secret to search engine’s low latency is it's in-memory index. The search engine "tokenises" and "normalises" all search input.
A tokeniser is a program that takes a input and emits one or more tokens. Default tokeniser would spilt on spaces. For example for input "We are
going to build a HUUUUUGEEE wall", tokeniser would generate 8 tokens, namely: "We", "are", "going", "to", "build", "a", "HUUUUUGEEE", "wall".
A normaliser converts the input to a normalised form. Default normaliser would convert all strings to lowercase. For example for token
"HUUUUUGEEE" will be normalised to "huuuuugeee".

Steps to run the  code :
I have run the code on Windows machine. The following steps are windows specific :
1)	Install python 2.7
2)	Use a suitable text editor (Pycharm, Sublime). 
3)	Mark your Python file as executable - On Windows, the standard Python installer already associates the .py extension with a file type (Python.File) and gives that file type an open command that runs the interpreter (C:\Python27\python.exe "%1"%*). This is enough to make scripts executable from the command prompt as ‘foo.py’.
4)	Add .py to the PATHEXT environment variable.
5)	Documents.csv and InvertedIndex.csv files will be created at location in the Constant.py file.     
6)	Execute the commands as follows :
blazeindex add '{"id":"123","text":"We are going to build a HUUUUUGEEE wall"}' 
blazeindex query 'WALL'


