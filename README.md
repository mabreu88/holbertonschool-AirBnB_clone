# AirBnB clone - The console

## Description:

The AirBnB clone: the goal of the project is to deploy on our server a simple copy of the AirBnB website.
We won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

## The command Interpreter/Console:

This console its a command interpreter that will be a tool to validate the storage engine by creating our own data model and managing (create, update, destroy, etc) objects via a console/command interpreter to strore and persist objects to a file (JSON file).

## Requirements of the project: Python Scripts.

* Allowed editors: `vi, vim, emacs`.
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
* All your files should end with a new line.
* The first line of all your files should be exactly `#!/usr/bin/python3`.
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable.
* The length of your files will be tested using `wc`.
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)

## Requirements for the project: Python Unit Test.

* Allowed editors: `vi, vim, emacs`.
* All your files should end with a new line.
* All your test files should be inside a folder `tests`.
* You have to use the `unittest module`.
* All your test files should be python files (extension: `.py`).
* All your test files and folders should start by `test_`.
* Your file organization in the tests folder should be the same as your project.
*  For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`.
* All your tests should be executed by using this command: `python3 -m unittest discover tests`.
* You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`.
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).

# The task of the project:

* 0. README, AUTHORS.
* 1. Be pycodestyle compliant!: Write beautiful code that passes the pycodestyle checks.
* 2. Unittests: All your files, classes, functions must be tested with unit tests.
* 3. BaseModel: Write a class BaseModel that defines all common attributes/methods for other classes.
* 4. Create BaseModel from dictionary: re-create an instance with this dictionary representation.
* 5. Store first object: recreate a BaseModel from another one by using a dictionary representation.
* 6. Console 0.0.1: Write a program called console.py that contains the entry point of the command interpreter.
* 7. Console 0.1: Update your command interpreter.
* 8. First User: Write a class User that inherits from BaseModel.
* 9. More classes!: Write all those classes that inherit from BaseModel.
* 10. Console 1.0: Update FileStorage to manage correctly serialization and deserialization of all our new classes.

## Usage:

To use this console follow these steps:
- Clone this repository to your local machine.
```
$ git clone https://github.com/mabreu88/holbertonschool-AirBnB_clone.git
```
- Execute the console file by using this line
```
$ ./console.py
```
- This is the following output:
```
(hbnb)
```
- Then you should be able to use the console commands, example:
```
root@user:~/holbertonschool-AirBnB_clone$ ./console.py
(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) quit
root@user:~/holbertonschool-AirBnB_clone$
```

## Commands:

* `quit`: Exits the console.
* `EOF`: Exits the console by using ctrl + d.
* `help`: Explains the use of all the commands by using help and `command`
* `create`: Creates a new instance of a class and prints its id by using create and `class name`
* `show`: Shows an existing instance with all it's information by using show, `class name` and `existing id`.
* `destroy`: Deletes an existing instance by using deletes, `class name` and `existing id`.
* `all`: Shows all instances, or all instances of specific class by using all and `class name`.
* `update`: Updates the information of a class instance by using update `class name`, `id`, `attribute name` and `value`.

## Examples:

```
root@user:~/holbertonschool-AirBnB_clone$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) [BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) quit
root@user:~/holbertonschool-AirBnB_clone$ 
```

## Contributing:

Pull request are welcome. If you have any idea for improvement let us know!
You can open a issue and discuss it with us.

## Support:

For any issue, bug or assistance, you can find us on GitHub:
* [Martín Abreu](https://github.com/mabreu88)
* [Noelia Micaela Viera Larrosa](https://github.com/MicaViera)

## Authors:

**Martín Abreu & Noelia Micaela Viera Larrosa.**
