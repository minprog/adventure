# Adventure: the Room class

The first step in building the game is creating a class that describes "Room" objects. You're going to do that now in complete isolation of the code in the `adventure.py` starter. Objects of the `Room` class will have two main responsibilities:

1.  Storing information about the room itself:

    - a short description
    - a long description
    - whether the room has been visited before

    Along with this information must come helper methods to manage the "visitedness" of the room and to provide the room description that must be printed depending on the state of the room.

2.  Storing information about the connections to other rooms, along with methods to change and request such information.


## A graph of rooms

Because each room will point to other rooms, together they will form a [**graph**](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)). The goal of the game is to navigate the rooms, and in our code, that means navigating a graph of room objects. For example, when we load the **Tiny** game map, the result is that we have four objects in memory, all pointing to each other:

![](../../tiny.png)

Compare this to the hand-drawn map fragment that was shown in the introduction. What we're doing is to model the idea of the game into a network of objects. The structure of both is quite alike.


## Room class

- To store information about the room itself, implement a class. Create a file called `room.py` to define a class called `Room`.

- Write an initializer. When created, a room is required to have two descriptions, so an intializer is needed to enforce that requirement.

- A "new" room has not been visited before, so that's why you should also set a variable in the initializer to represent that (such a variable is called a "flag").

- Write a method `set_visited` that allows us to mark the room as visited when that happens.

- Write a method `description` that returns the short/long description depending on whether the room thas been visited before.


## Connections

- Create an intance variable in `Room` to keep track of connections. Connections combine a string representing a direction such as `"WEST"` with a reference to another room object. What Python data structure is best to store such mappings? Create an empty variable in the initializer to prepare this.

- Write a method `add_connection`, which accepts a direction and a room object, and saves it in the connection storage.

- Write a method `has_connection` that can determine if there is a connection available from the room to another room, given the direction.

- Write a method `get_connection` that retrieves the actual `Room` object that is found given a specific direction.

> A hard constraint in this program is that the `Room` class may not access (use) other classes. Its methods may only manipulate `self` and any access only objects that are passed to it as arguments to method calls.


## Testing

After implementing the `Room` class, you should test the class by starting Python interactively (so you can enter Python commands) and creating a few `Room` objects:

    $ python3 -i room.py
    >>> r1 = Room(1, "Room 1", "Long description 1")
    >>> r2 = Room(2, "Room 2", "Long description 2")
    >>> r2.add_connection("WEST", r1)
    >>> r2.has_connection("EAST")
    False
    >>> r2.has_connection("WEST")
    True
    >>> r2.get_connection("WEST")
    <__main__.Room object at 0x7f36f65076a0>
    >>> r1.description()
    "Long description 1"
    >>> r1.set_visited()
    >>> r1.description()
    "Room 1"

(The memory address shown on your computer will be different.)

Be sure to test manually, like above, before continuing.
