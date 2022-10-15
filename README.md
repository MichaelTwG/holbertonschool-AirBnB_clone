[readmelogo](https://user-images.githubusercontent.com/105667144/196003373-c103b426-3eb8-418b-827b-c4a12c81745d.png)
#  AirBnB clone - The console





This team project is part of the Holberton School Full-Stack Software Engineer program. It's the first step towards building a first full web application: an AirBnB clone. IT consists of a custom command-line interface for data management, and the base classes for the storage of this data.
This repository contains the initial stage of the above mentioned project. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.


## Function

The console works both in interactive mode and non-interactive mode, much like a Unix shell. It prints a prompt **(hbnb)** and waits for the user for input.

| Action | Command |
|--------------|------|
| Run the console |```./console.py```|
| Quit the console | ```(hbnb) quit``` |
| Display the help for a command | ```(hbnb) help <command>``` |
| Create an object (prints its id)|```(hbnb) create <class>``` |
| Show an object | `(hbnb) show <class> <id>` or `(hbnb) <class>.show(<id>)` |
| Destroy an object | `(hbnb) destroy <class> <id>` or `(hbnb) <class>.destroy(<id>)` |
| Show all objects, or all instances of a class | `(hbnb) all` or `(hbnb) all <class>` |
| Update an attribute of an object | `(hbnb) update <class> <id> <attribute name> "<attribute value>"` or `(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")` |
___________________________________________________________________

Non-interactive mode example:

```$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show update
```

## File storage

The folder  **engine** manages the serialization and deserialization of all the data, following a JSON format.

A FileStorage class is defined in  **file_storage.py**  with methods to follow this flow:  `<object> -> to_dict() -> <dictionary> -> JSON dump -> <json string> -> FILE -> <json string> -> JSON load -> <dictionary> -> <object>`

The  **_init_.py** file contains the instantiation of the FileStorage class called  **storage**, followed by a call to the method reload() on that instance. This allows the storage to be reloaded automatically at initialization, which recovers the serialized data.

## 

All your files and folders are presented as a tree in the file explorer. You can switch from one to another by clicking a file in the tree.

## Usage
1.  First clone this repository.
    
2.  Once the repository is cloned locate the "console.py" file and run it as follows:
    

```
/AirBnB_clone$ ./console.py

```

4.  When this command is run the following prompt should appear:

```
(hbnb)

```

5.  This prompt means you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands

```
* create - Creates an instance based on given class

* destroy - Destroys an object based on class and UUID

* show - Shows an object based on class and UUID

* all - Shows all objects the program has access to, or all objects of a given class

* update - Updates existing attributes an object based on class name and UUID

* quit - Exits the program (EOF will as well)

```

***Alternative Syntax***

Users are able to issue a number of console command using an alternative syntax:

```
Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])

```



## Examples

### Primary Command Syntax ###

***Example 0: Create an object***

Usage: **create <class_name>**

```
(hbnb) create BaseModel

```

```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   

```

***Example 1: Show an object***

Usage: **show <class_name> <_id>**

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  

```

***Example 2: Destroy an object***

Usage: **destroy <class_name> <_id>**

```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   

```

***Example 3: Update an object***

Usage: **update <class_name> <_id>**

```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)

```
***Alternative Syntax***

***Example 0: Show all User objects***

Usage: **<class_name>.all()**

```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]

```

***Example 1: Destroy a User***

Usage: **<class_name>.destroy(<_id>)**

```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]

```

***Example 2: Update User (by attribute)***

Usage: **<class_name>.update(<_id>, <attribute_name>, <attribute_value>)**

```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]

```

***Example 3: Update User (by dictionary)***

Usage: **<class_name>.update(<_id>)**

```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]

```

## Tests

All the code is tested with the  **unittest**  module. The test for the classes are in the **test_models** folder.

## Authors


- ***Micheal Gonia*** [Github] (https://github.com/MichaelTwG) 
-   ***Marcelo Rodriguez***  -  [Github] https://github.com/Marcelorb1) 
