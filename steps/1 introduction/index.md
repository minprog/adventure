# Adventure: introduction

## tl;dr

- Implement Crowther's Adventure game using OOP in Python.
- Play your game!

## Background

Back in the days, before dedicated graphics cards were a thing, text-based adventure games were incredibly popular. This type of game consists entirely out of text, and is traversed by commands much like the ones you would enter in the terminal. One such game is Colossal Cave Adventure, created by [William Crowther](https://en.wikipedia.org/wiki/William_Crowther_(programmer)) in 1975, that served as the inspiration for the text adventure game genre.

In Adventure you have to navigate between "Rooms" through commands such as "WEST" and "EAST", but also "IN" or "OUT":

    You are standing at the end of a road before a small brick
    building. A small stream flows out of the building and
    down a gully to the south. A road runs up a small hill
    to the west.
    > WEST
    You are at the end of a road at the top of a small hill.
    You can see a small building in the valley to the east.
    > EAST
    Outside building.
    >

That first part of the adventure "map" may look like this:

![](../../map.png){:.w300}

You can find the full map, including a spoiler-free version, [at this website](http://www.spitenet.com/cave/), but note that you will be implementing a portion of the full map!

But there is more than just navigating, at all times you can ask for `HELP` for an explanation of the game, or `LOOK` to get a detailed description of the room you are in.
From the previous example you could see that the second time a room is entered a shorter description was shown. If we were to enter the `LOOK` command we would again see the following:

    > LOOK
    You are standing at the end of a road before a small brick
    building. A small stream flows out of the building and
    down a gully to the south. A road runs up a small hill
    to the west.
    >

The adventure "map" is provided in a few **data files**, that contain room names and description, and in particular, information about which rooms are connected to other rooms, and using which commands.

Though Crowther originally wrote his game in Fortran, an imperative programming language that has been around since the 1950s, we will be taking a more modern approach to its implementation, using object-oriented programming (OOP). OOP is particularly suited to Adventure, because its main idea is a series of rooms that are connected. Each room will be an object, and all of these objects will point to each other.


## Specification

Implement an object-oriented version of Crowther's Adventure game using the class structure provided below. It should have the following parts:

1. implement **loading** of the map:
    * handling command line arguments to open a given datafile
    * loading map data into a series of objects
2. implement user **interaction**:
    * prompting the user for commands and execute those
    * warn about non-existent commands
    * moving the player from room to room
3. implement game **logic**:
    * forced movements
    * managing items and inventory


### Distribution

	$ wget https://github.com/minprog/adventure/raw/2020/steps/adventure.zip
	$ unzip adventure.zip
	$ rm adventure.zip
	$ cd adventure
	$ ls
	adventure.py  data/


## Understanding

### `data/`

The `data` directory contains data files with which you can create two versions of adventure. `TinyAdv.dat` is the smallest adventure game, consisting of 4 rooms. Here are its contents in full:

    1	Outside building	You are standing at the end of a road before a small brick building.  A small stream flows out of the building and down a gully to the south.  A road runs up a small hill to the west.
    2	End of road	You are at the end of a road at the top of a small hill. You can see a small building in the valley to the east.
    3	Inside building	You are inside a building, a well house for a large spring.
    4	Victory	You have found the hidden well of winning a tiny game. Congratulations!

    1	WEST	2	UP	2	NORTH	3	IN	3
    2	EAST	1	DOWN	1
    3	SOUTH	1	OUT	1	DOWN	4

    KEYS	a set of keys	3
    LAMP	a brightly shining brass lamp	2

The file comprises three parts, divided by two blank lines. The first part describes the "rooms", with on each line an identifying number, then a TAB character, then a short description, then another TAB character, and then a long description:

    1	Outside building	You are standing at the end of ...

The second part describes connections between rooms. In fact, this section defines the "commands" that players can type to navigate from one room to another. Of each line, the first part is a room identifier (the place where the connection starts) and then there are one or more connections, each having a command, then a TAB, and the number of the room it connects to.

    2	EAST	1	DOWN	1

The third and final part describes objects that may be found in the game. You will not use these in the "standard edition" of this problem.

Also included in your distribution is `SmallAdv.dat`, which is a bit larger and includes more advanced interactions, as well as `Crowther.dat`, which is the full game.


### `adventure.py`

Take a look at `adventure.py`. The file has two parts.

1. The `Adventure` class contains all methods that make the game work:

	- The `__init__` method ensures that all is set for playing an adventure game. In particular, it uses other methods to load game data and point `current_room` to the first room in the map.

	- The `room_description` method provides the description of the current room, the room the player is in.

	- Moving around in the game is handled by the `move` method, by setting the "current" room to a different one.

2. The `if __name__ == "__main__"` part, which contains the main "game loop" of the program. After introducing the game, it repeatedly asks for a command from the user, and tries to perform that command.

> A hard constraint in this program is that the `Adventure` class may not `print` anything. All other printing should be done in the `__main__` part. And in return, the `__main__` part may, aside from printing things, only call methods in the `Adventure` class. It may not access methods and/or attributes from other classes that you will be writing. As such, each class will have separate responsibilities.
