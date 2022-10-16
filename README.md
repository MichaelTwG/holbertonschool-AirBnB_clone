![image text](https://user-images.githubusercontent.com/105667144/196003373-c103b426-3eb8-418b-827b-c4a12c81745d.png)

#  AirBnB clone - The console



This team project is part of the Holberton School Full-Stack Software Engineer program. It's the first step towards building a first full web application: an AirBnB clone. 

IT consists of a custom command-line interface for data management, and the base classes for the storage of this data.

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

## Models

The folder  **models**  contains all the classes used in this project.

File | Description | Attributes
-----|---------------|---------------------------------|
base_model.py |BaseModel class for all the other classes | id, created_at, updated_at |
user.py | User class for future user information | email, password, first_name, last_name |
amenity.py | Amenity class for future amenity information | name |
city.py | City class for future location information | state_id, name |
state.py | State class for future location information | name |
place.py | Place class for future accomodation information | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids |
review.py | Review class for future user/host review information | place_id, user_id, text
-----------------

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


## Examples

## Examples

### Primary Command Syntax ###

***Example 0: Create an object***

Usage: **create <class_name>**
``` 
(hbnb)  create BaseModel
b516158e-17fa-4ba2-b51e-5cb3970214d5
(hbnb)

```
***Example 1: Show an object***

Usage: **show <class_name> <_id>**
```
(hbnb) show BaseModel b516158e-17fa-4ba2-b51e-5cb3970214d5
[BaseModel] (b516158e-17fa-4ba2-b51e-5cb3970214d5) {'id': 'b516158e-17fa-4ba2-b51e-5cb3970214d5', 'created_at': datetime.datetime(2022, 10, 16, 13, 53, 18, 26109), 'updated_at': datetime.datetime(2022, 10, 16, 13, 53, 18, 26168)}
(hbnb)

```



***Example 2: Destroy an object***

Usage: **destroy <class_name> <_id>**
```
(hbnb) destroy  BaseModel b516158e-17fa-4ba2-b51e-5cb3970214d5
(hbnb) show  BaseModel b516158e-17fa-4ba2-b51e-5cb3970214d5
** no instance found **
(hbnb)
```


***Example 3: Update an object***

Usage: **update <class_name> <_id>**

```
(hbnb) create BaseModel
520284ba-06c5-445a-9549-996b58ac5b7a
(hbnb) update BaseModel 520284ba-06c5-445a-9549-996b58ac5b7a first_name "person"
(hbnb) show BaseModel 520284ba-06c5-445a-9549-996b58ac5b7a
[BaseModel] (520284ba-06c5-445a-9549-996b58ac5b7a) {'id': '520284ba-06c5-445a-9549-996b58ac5b7a', 'created_at': datetime.datetime(2022, 10, 16, 13, 59, 39, 441724), 'updated_at': datetime.datetime(2022, 10, 16, 13, 59, 39, 441778), 'first_name': '"person"'}
(hbnb)
```



## Tests

All the code is tested with the  **unittest**  module. The test for the classes are in the **test_models** folder.

## Authors


- ***Micheal Gonia*** [Github] (https://github.com/MichaelTwG) 
-   ***Marcelo Rodriguez***  -  [Github] https://github.com/Marcelorb1) 
