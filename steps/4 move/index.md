# Adventure: moving around

Now that we have a couple of rooms, we can start implementing the game itself. We'll start by implementing a `move` method for the `Adventure` class. This methods defines an action in the game. Then, we'll write code for the game loop, where a player can actually enter commands, after which the game loop will call upon the methods of an `Adventure` object.


## Movement

The most elementary function of this game is moving around between rooms. The following steps allow a text-based game such as Adventure to simulate movement:

1. The "current room" has a description, which is printed to the screen to allow the player to understand where they are.

2. The player enters a direction they want to head into, such as "DOWN".

3. The game changes the "current room" internally.

4. The now-current room's description is printed, so the player feels that they have moved to another location inside the game "world".

5. Go to 2.

Implement the `move` method for the `Adventure` class. The `move` method has one parameter, `direction`, which should help you find the room to move to. As an implementation detail, `move` should also return a boolean `True` or `False` depending on whether the move was possible (when is the move not possible?). The main program can use this result to notify the user when the move could not be performed.


## Prompting for commands

Now check out the part of `adventure.py` that starts with `if __name__ == '__main__'`. Currently, if you run `adventure.py`, you will be shown the description of the first room, you can even enter commands, but nothing will happen as you enter them.

We're going to support a few different commands, but first of all, let's allow players to move around in the game using directions like "IN" or "WEST".

-   First connect the `main` input loop to the `move` method, by passing the entered `command` to the `Adventure` class's `move` method.

-   Write code to display the new room's description.

-   Finally, build in some feedback to your player in the `main` loop. If they attempt a command that is not a valid direction, tell them they entered an "Invalid command." and prompt for another command using the '>'.

        > OUT
        Invalid command.
        >

    You can use the **return value** of the `move` method to know if you need to print an error message.

## Testing

Now that you have implemented moving around, you can test the game by playing it!

When you have verified that the game works correctly using the **Tiny** map, check that it also works when you load the **Small** map:

    $ python3 adventure.py Small
