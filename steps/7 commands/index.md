# Adventure: final touches

## Step 4: Additional commands

As a final step for making the game work, we'll add a few commands that make it easier to use: `QUIT`, `HELP` and `LOOK`. Implement these in the following way:

-   `HELP` prints instructions to remind the player of their commands and how to use them. It should behave as follows:

		> HELP
		You can move by typing directions such as EAST/WEST/IN/OUT
		QUIT quits the game.
		HELP prints instructions for the game.
		LOOK lists the complete description of the room and its contents.

-   `LOOK` prints a full description of the room the player is currently in, even if the room was visited earlier.

		Inside building
		> LOOK
		You are inside a building, a well house for a large spring.

For the latter, should implement a method `get_long_description` in `Adventure`, which will always return the long description.

## Step 5: Try a larger map

Before continuing, make sure your program still works if you transition from the **Tiny** map to the **Small** map! From now on, when testing, run the game like this:

    $ python adventure.py Small


## Step 7: Synonyms

Implement Synonyms. Note that your adventure game does not implement all commands in the synonyms data file! Implement it in such a way that everything still works as expected, and do not accept commands like `I` or `INVENTORY`! In this case, it's advisable to not write a full class to manage synonyms, but use a standard dictionary instead.

