# Adventure: final touches

Let's finish the game by adding a few commands and a synonyms feature.

## Additional commands

`HELP` and `LOOK` are two commands to make the game a bit easier to use. Implement those in the following way:

-   `HELP` prints instructions to remind the player of their commands and how to use them. It should behave as follows:

		> HELP
		You can move by typing directions such as EAST/WEST/IN/OUT
		QUIT quits the game.
		HELP prints instructions for the game.
		LOOK lists the complete description of the room and its contents.

-   `LOOK` prints a long description of the room the player is currently in, even if the room was visited earlier.

		Inside building
		> LOOK
		You are inside a building, a well house for a large spring.


## Synonyms

The file `Synonyms.dat` contains a list of shortcuts that players should be able to use when navigating the game, saving them a bit of typing. Instead of `WEST`, players should be able to enter `W`.

Implement synonyms for your game.
