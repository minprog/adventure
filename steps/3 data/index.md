# Adventure: reading data files

Take another look at the data in `TinyAdv.dat`. **Parsing** is the task of loading this information into memory in a structured way. You are going to read the room information from the first section of the file, and the connections information from the second section of the file. We'll leave the third section, with game objects, for later.


## Background

You will need to implement parsing in two **phases**: first create all room objects, then make all connections between the rooms. This is because any two rooms may be connected, and they both have to exist as objects in memory before setting a connection. Best, then, to first create all objects and then make all connections.


## Getting started

- Create a file called `loader.py`, which will define a `load_rooms()` function.

- The file needs access to the `Room` class (so it can create `Room`-type objects), so it needs to specify `from room import Room` right at the top.

- Write a function `load_rooms()` that creates a graph of all room objects pointing to each other and returns a reference to the first room in the game.


## A small intermezzo on reading files

You may have seen that it's possible to load information from a file using a `for`-loop:

    for line in file:
        # do something for each line

However, in this assignment, we can't easily use this idea, because there are several sections in the datafile and each section has a different structure.

What we can do is write our own loops that read lines for one section each. We then read only a single line of the file per iteration. This is done using the `readline()` method. Here's an example for opening a file and reading two lines:

    with open("TinyAdv.dat") as f:
        for i in range(2):
            line = f.readline()
        print(line)

As you might imagine, this short piece of code will print something like `2	End of road...` etc.

When using `readline`, note that it can be used to distinguish between data lines, empty lines and the end of the file:

1. a line containing text, for which `readline` returns the content, ending in a newline character
2. an empty line, for which `readline` returns just the newline character (`"\n"`)
3. the end of the file, for which `readline` returns an empty string (`""`)

By making use of this particular behavior of `readline` we can parse section by section of our datafile.


## Phase 1: creating rooms

Now implement the first phase of `load_rooms` in `adventure.py`. Start by opening the file:

    with open(filename) as f:

Then write a loop to read the room data:

1. read a line
2. `split()` it into a list, making sure you split on the TAB character ("\t")
3. create a new room object using the data from the list
4. add the room to a `rooms` variable for later use
5. go to 1

Make sure the loop ends as soon as `readline` returns *just* a newline character. Also, don't forget to clean the data. Each line has a newline character at the end, and this character should *not* end up in the room object description! Recall how to remove a stray newline from the end of a string?

Having done the above should lead to a fully initialized `self.rooms` dictionary:

	self.rooms = {
		1: <room.Room object at 0x7f325cbc4d68>,
		2: <room.Room object at 0x7f325cbc4fd0>
	}

Finally, below that code, add a few assertions you know to be true:

    assert 1 in rooms
    assert rooms[1].name == "Outside building"

You can then run `adventure.py` and make sure none of the assertions fail. (You should later remove any assertions that depend on particular descriptions, because your program may be used using a different data file!)


## Phase 2: making connections

Because all rooms have now been created, we can read the connection data and make the actual connections between the rooms.

We leave designing the loop up to you, but remember that each line starts with the room number that the connection starts from, and that each line may contain *multiple* other rooms to connect to. This is good moment to take out pen and paper and design the algorithm!

To actually connect rooms, you will have to look them up in `self.rooms` by number, and then make a connection:

    source_room = self.rooms[1]
    destination_room = self.rooms[2]
    source_room.add_connection("WEST", destination_room)


## Objects in memory

So we have rooms and connections. What can we find in memory now that everything has been loaded? How can we get to each of the objects in the room graph?

1. The attribute `current_room` of `Adventure` points to a single object of the `Room` class, which should be the first room when the game is first loaded.

2. The attribute `_rooms` of `Adventure` is a dictionary, which maps each room number to a single object of the `Room` class. This way you have access to **all** rooms directly, but you will not actually need this after loading everything.

3. Once you have a `Room` object, you can reach any connected rooms through the `get_connection()` method. Hence, you should be able to reach any room from the first one---that is, if the data files are correct!


## Testing

When finished, add a few assertions that should be true after making connections.

    assert self.rooms[1].has_connection("WEST")
    assert self.rooms[2].get_connection("EAST").name == "Outside building"

You can again run `adventure.py` and make sure none of the assertions fail.
