# Adventure: moving around

Now that we have a couple of rooms, we can start implementing the game itself. We'll start by implementing a `move` method for the `Adventure` class. This methods defines an action in the game. Then, we'll write code for the game loop, where a player can actually enter commands, after which the game loop will call upon the methods of an `Adventure` object.


## Movement

The most elementary function of this game is moving around between rooms. The following steps allow a text-based game such as Adventure to simulate movement:

1. The current room has a description, which is printed to the screen to allow the player to understand where they are.

2. The player enters a direction they want to head into, such as "DOWN".

3. The game changes the "current room" internally.

4. The now-current room's description is printed, so the player feels that they have moved to another location inside the game "world".

5. Go to 2.

Let's implement the `move()` method for the `Adventure` class, and then allow players to actually move around using this method.

The `move` method has one parameter, `direction`, which should be connected to another room in the game graph.

As an implementation detail, `move` should also return a boolean `True` or `False` depending on whether the move was possible (when is the move not possible?). The main program can use this result to notify the user if the move could not be performed.


## Prompting for commands

Now check out the part of `adventure.py` that starts with `if __name__ == '__main__'`. Currently, if you run `adventure.py`, you will be shown the description of the first room, you can even enter commands, but nothing will happen as you enter them.

We're going to support a few different commands, but first of all, let's allow players to move around in the game using directions like "IN" or "WEST".

- First connect the `main` input loop to the `move` method, by passing the entered `command` to the adventure class's `move` method.

- Write code in `move` to change the game state such that the player is moved to the next room, and then display the new room's description.

- Note that the `command` is immediately converted to lowercase in the main loop, so it's also passed in lowercase to `move`. Make sure that `move` correctly finds connections when given a lowercase direction!

- Finally, build in some feedback to your player in the `main` loop. If they attempt a command that is not a valid direction, tell them they entered an "Invalid command." and prompt for another command using the '>'.

		> OUT
		Invalid command.
		>


## Short and long descriptions

When a player enters a room they've already seen, the short description will be displayed instead of the long one. How should we keep track of that?

To handle this, you can add a **flag** variable to the `Room` class. A flag is another name for a boolean value, but in this case it can be used to determine if the room has already been visited and whether to display the short description.

Add the flag to the `Room` initializer and change `description` to return the correct description depending on the flag. Also add a method to allow the visited flag to be set to `True` and call this method **right before leaving the room**.


## Testing

Now that you have implemented moving around, you can test the game by playing (part of) it!

Also, make sure your program still works if you transition from the **Tiny** map to the **Small** map. So try the game again, but like this:

    $ python3 adventure.py Small
