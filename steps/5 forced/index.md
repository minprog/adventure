# Adventure: forced movement

Sometimes a player will attempt a movement that lands them in a bad place. For example, in the Small adventure, when going WEST from the "Outside grate" room (number 6), one finds oneself at the edge of an "unpassable stream".

    You are in a 25-foot depression floored with bare dirt. Set into
    the dirt is a strong steel grate mounted in concrete.  A dry 
    streambed leads into the depression from the north.
    > WEST
    You find yourself at the edge of a impassible stream. You head
    back to the depression.

The only way is going back the "Outside grate" room. In the description above you find a hint that the player is about to be moved automatically: "You head back to the depression." And indeed, this is what the forced movement feature is about to do.

Whenever a room contains a connection labeled `FORCED`, and a player enters the room, they will be **automatically** be transferred to that connection. The game data files have been written to take advantage of this feature.


## Specification

If a player enters a room that has a direction named `FORCED`:

- the long room description will be printed (always),
- the player will be immediately moved back to the connected room,
- the default description for the connected room will be printed.


## Hints

- You'll most likely want to do a check each time you move to a new room. If there's a `FORCED` connection in the new room, take a good look around and follow the forced route.

- As you're going to have to print the description, handle this in the main game loop and not in the `move` method! To accomplish this, you have to add a new method to the `Adventure` class:

    - `is_forced` will allow us to check if the current room has a forced connection

    - note that you can use the existing `get_long_description`!
