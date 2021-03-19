# Adventure: conditional movement

Having items in possession isn't just for fun. Items can allow access to connections that would be unavailable otherwise. For a game like Adventure, this opens up new possibilities, making the game more like a puzzle.

Conditional connections are already present in the Crowther data file. For example, room `9` has the following connections:

    9	EAST	8	WEST	12/LAMP	WEST	10

Normally, the `EAST` direction provides access to room 8, and the `WEST` direction to room 10. Now, when holding a `LAMP` item, the behaviour of the "WEST" command is changed, moving the player into room 12 instead.

Note that order *does* matter in deciding which connection to take. In the example above, there are two `WEST` connections, and the connection that requires a `LAMP` is specified first.


## What to do

Implement conditional movement. As you might imagine, you will need to change your code for reading the data files. And you'll also need to make changes to your `Room` class, the `Adventure` class and the main game loop, probably!
