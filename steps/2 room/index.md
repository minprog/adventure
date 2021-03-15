# Adventure: the Room class

The first step in building the game is creating a class that describes "Room" objects. The objects of this class will have two main responsibilities:

1. Storing information about one room; in particular its short description and long description. These are stored in a few object variables.

2. Storing information about the connections to other rooms, and the commands typed to go there. These should ideally be stored in a dictionary.


## Implementation

To store information about the room itself, implement a basic data class. Create a file called `room.py`, with a class called `Room`. The initializer should accept and store:

- room name (string)
- room description (string)

To store information about the connections, you will need to create a new empty dictionary in the initializer. After loading the game map, a connections dictionary inside a `Room` object might look like this:

	connections = {
		"WEST": <room.Room object at 0x7f325cbc4d68>,
		"EAST": <room.Room object at 0x7f325cbc4fd0>
	}

This means that the dictionary maps a **direction** (string) to another `Room` object. This is very important! The description above means that `Room` objects will point to each other, meaning that when the game map is loaded, a [**graph**](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)) is created of rooms and connections. The goal of the game is to *navigate that graph*. A graph, incidentally, is one kind of Abstract Data Type!

For example, if we load the **Tiny** game map, the result should be that we have 4 objects in memory, all pointing to each other:

![](../../tiny.png)
    
Then you need to add three methods for managing and looking up connections:

- `add_connection` which accepts a direction (string) and a room (another Room object), and stores those in the dictionary
- `has_connection` which accepts a direction (string), and checks whether there is a connection in the dictionary under that name
- `get_connection` which accepts a direction (string), and retrieves the actual Room object that it connects to

Now, implement the three methods for managing connections. You might need to read up on [dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).

> A hard constraint in this program is that the `Room` class may not access (use) other classes. Its methods may only manipulate `self` and any access only objects that are passed to it as arguments to method calls.


## Testing

After implementing, you should test the class by starting Python and creating `Room` objects:

	$ python3 -i room.py
	>>> r1 = Room(1, "Room 1", "Description 1")
	>>> r2 = Room(2, "Room 2", "Description 2")
	>>> r2.add_connection("WEST", r1)
	>>> r2.has_connection("EAST")
	False
	>>> r2.has_connection("WEST")
	True
	>>> r2.get_connection("WEST")
	<__main__.Room object at 0x7f36f65076a0>

In that last line, you find the Python description of a `Room` object, along with its assigned memory address. Seems to work! (The address on your computer will most likely be different.)

Be sure to test manually, like above, before continuing!
