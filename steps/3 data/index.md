# Adventure: reading data files

Take another look at the data in `TinyAdv.dat`. **Parsing** is the task of loading this information into memory in a structured way. You are going to read the room information from the first section of the file, and the connections information from the second section of the file. We'll leave the third section, with game items, for later.


## Background

You will need to implement parsing in two **phases**: first create all room objects, then make all connections between the rooms. This is because any two rooms may be connected, and they both have to exist as objects in memory before setting a connection. Best, then, to first create all objects and then make all connections.


## Getting started

- Create a file called `loader.py`, which will define a `load_room_graph` function (this is just a helper function, so you do not create a class).

- The file needs access to the `Room` class (so it can create `Room`-type objects), so it needs to specify `from room import Room` right at the top.

- According to the instructions below, write a function `load_room_graph` that creates a graph of all room objects pointing to each other and returns a reference to the "first" room.


## A small intermezzo on reading files

You may have seen that it's possible to load information from a file using a `for`-loop:

    for line in file:
        # do something for each line

However, in this assignment, we can't easily use this idea, because there are several sections in the datafile and each section has a different structure.

What we can do is write our own loops that read lines for one section each. We then read only a single line of the file per iteration. This is done using the `readline()` method.

Here's an example for opening a file, reading two lines, and only printing the second line:

    with open("TinyAdv.dat") as f:
        for i in range(2):
            line = f.readline()
        print(line)

As you might imagine, this short piece of code will print something like `2	End of road...` etc.

When using `readline`, note that it can be used to distinguish between data lines, empty lines and the end of the file:

1. a line containing text, for which `readline` returns the content, ending in a newline character
2. an empty line, for which `readline` returns just the newline character (`"\n"`)
3. the end of the file, for which `readline` returns an empty string (`""`)

By making use of this particular behavior of `readline` we can parse the data file, section by section.


## Phase 1: creating rooms

Now implement the first phase of `load_room_graph` in `adventure.py`. You will store room information in a **dictionary** that maps a room number to a room object.

> We use a dictionary because room numbers start at 1 and are not guaranteerd to be sequential. Also, we do not know in advance how many rooms are going to be needed. Hence, it may become too tricky to use a **list** for collecting rooms. So instead, we use a dictionary. Because we use integers as keys, it will almost *look* like we're using a list, but with a lot more flexibility.

Start by opening the file and then write a loop to read the room data:

1. read a line
2. `split()` it into a list, making sure you split on the TAB character (written as `"\t"`)
3. create a new room object using the data from the list
4. add the room to a `rooms` dictionary for later use
5. go to 1

Make sure the loop ends as soon as `readline` returns *just* a newline character. Also, don't forget to clean the data. Each line has a newline character at the end, and this character should *not* end up in the room object description! Recall how to remove a stray newline from the end of a string?

Having done the above should lead to a fully initialized `rooms` dictionary:

    {
        1: <room.Room object at 0x7f325cbc4d68>,
        2: <room.Room object at 0x7f325cbc4fd0>
    }

Finally, below that code, add a few assertions you know to be true:

    assert 1 in rooms
    assert rooms[1]._short_description == "Outside building"

The starter version of `adventure.py` already calls the `load_room_graph()` function, so you can now run `adventure.py`, and then make sure none of the assertions fail. (Remember to later remove any assertions that depend on particular descriptions, because your program may be used using a different data file!)


## Phase 2: making connections

Because all rooms have now been saved into memory, we can read the connection data from the data file and make the actual in-memory connections between the rooms.

We leave designing this loop up to you, but remember that each line starts with the room number that the connection starts from, and that each line may contain *multiple* other rooms to connect to. This is good moment to take out pen and paper and design the algorithm.

To actually connect rooms, you will have to look them up in `rooms` by number, and then make a connection:

    source_room = rooms[1]
    destination_room = rooms[2]
    source_room.add_connection("WEST", destination_room)


## The result of loading: objects in memory

So when all is done, we have rooms and their connections. What can we find in memory now that everything has been loaded? How can we get to each of the objects in the room graph?

1. The variable `rooms` in `load_room_graph()` is a dictionary, which maps each room number to a single object of the `Room` class. This way you have access to **all** rooms directly. The variable will disappear as soon as the function returns, but that's fine.

2. The attribute `_current_room` of `Adventure` points to a single object of the `Room` class, which is normally the first room, at least when the game has just been loaded.

3. Once you have such a `Room` object, you can reach any connected rooms through the `get_connection()` method. Hence, you should be able to reach any room from the first one---that is, if the data files are correct.


## Testing

Also add a few assertions to `load_room_graph()` that should be true after making connections.

    assert rooms[1].has_connection("WEST")
    assert rooms[2].get_connection("EAST")._short_description == "Outside building"

You can again run `adventure.py` and make sure none of the assertions fail.
