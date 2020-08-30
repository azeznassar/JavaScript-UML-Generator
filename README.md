# JavaScript to UML Generator - js2uml

By Azez Nassar & Ethan Bray

## Problem Domain
Create a Python 3 program, which can generate a UML 2 diagram based on the source code of an ES6+ (ECMAScript  2015+) program  in  a  file/files  under  a  directory  by  using  Python  package(s).

## Installation / Setup

Clone the repo:

```sh

$ git clone https://github.com/azeznassar/JavaScript-UML-Generator.git

$ cd JavaScript-UML-Generator

```

Create and activate a virtual environment:

```sh

$ python -m venv venv

$ source venv/bin/activate # OR venv\Scripts\Activate.ps1 for windows/PS

```


Install the Python package dependencies:

```sh

$ pip install -r requirements.txt

```

Install the NPM dependency (standardjs):

```sh

$ npm install

```

Run the program:

```sh

$ python src/input_handler.py

```

## Usage

```sh
python src/input_handler.py [0] or [1]
```
0 and 1 are optional arguments which start the program within Azez's or Ethan's implementation (Opens within Azez's by default when no argument is given)

#### Commands

    =========================================================================
    available commands: create_uml, deserialize, info, switch_cmd, help, quit


    create_uml:
            usage: create_uml js_input
            Generate an image of an UML class diagram from inputted JavaScript source code file(s)

            positional arguments:
                js_input	input JavaScript file or directory of JavaScript files


    deserialize:
            usage: deserialize [-d]
            Display the deserialized JavaScript class information that is serialized from the create_uml command

            optional arguments:
                -d		Deletes the serialized data file after deserializing and display it


    info:
            usage: info
            Displays information about the software, such as version number and authors.


    switch_cmd:
            usage: switch_cmd
            Switchs from the current cmd implementation to the other available implementation.
            (all commands are the same)


    help:
            usage: help
            Displays help information about each available command, such as, usage and possible arguments


    quit:
            usage: quit
            Exits from the program 

 <p align="center"> 
    <img src="https://i.imgur.com/pe00DnH.gif" alt="Demo of command usage">
 </p>
