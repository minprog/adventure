# Adventure: moving around

Now that we have a couple of rooms, we can start implementing the game itself. We'll start by implementing a `move` method for the `Adventure` class. This methods defines an action in the game. Then, we'll write code for the game loop, where a player can actually enter commands, after which the game loop will call upon the methods of an `Adventure` object.


## Implement "move"

The most basic function of this game is moving around between rooms. Remember that the `Adventure` class has a variable that keeps track of the "current room" for the game. It also has a still-empty `move` method that's supposed to set the current room to a new one.

The `move` method has one parameter, `direction`, which should let you lookup (via the `current_room`) which room we're going to move on to. Just set `current_room` to that room and you're done.

`move` should also return a boolean `True` or `False` depending on whether the move was possible. The main program can use this result to notify the user if the move could not be performed.


## Prompting for commands

Now check out `if __name__ == '__main__'` at the bottom of `adventure.py`. Currently, if you run `adventure.py`, you will be shown the description of the first room, you can even enter commands, but nothing will happen as you enter them.

We're going to support a few different commands, but first of all, let's allow your use to move around in the game using directions like "IN" or "WEST".

- Start by passing the entered `command` to the adventure class's `move` method.

- Make sure that the `move` method displays the room description after processing the move, so it feels like moving around in the map. (Currently a description is already printed once, at the start of the game.)

- Following the description we'll again prompt the player for a command. The '>' will mark this prompt. It should look like this:

		You are standing at the end of a road before a small brick
		building.  A small stream flows out of the building and
		down a gully to the south.  A road runs up a small hill
		to the west.
		>

- Not all users read the docs! Be sure to allow for both UPPER and lower case directions.

- If the player attempts a command that cannot be executed tell them they attempted an "Invalid command." and prompt for another command using the '>'.

		> OUT
		Invalid command.
		>


## Short and long descriptions

If a player enters a room they've already seen, only give them the short description. How should we keep track of that?

- First, add a new attribute to `Room.__init__`: self.visited. It should be `False` when the room is first initialized.

- Then, add a `set_visited()` method to `Room`, which marks it as visited. Also, add a `is_visited()` method, which returns False or True depending on the current state of the room.

- Having done that, you can change `Adventure`'s `move` method to set a room to visited **right before moving to another room**. Use the new `set_visited` method to do that.

- And finally, you can now use `is_visited()` in `Adventure.get_description` to return either the room `name` or the room `description`, depending on whether it was visited before.


## Testing

Now that you have implemented moving around, you can test the game by playing (part of) it!
