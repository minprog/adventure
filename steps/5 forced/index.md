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

- the long room description will be printed (even if already visited),
- the player will be immediately moved back to the connected room,
- the description for the connected room will be printed (which will now be the short one).


## Hint

Currently, the `Room` class decides whether to print the short or long description. Change it to account for the specification above. You should be able to fully handle generating the right description in your code for the `Room` class.
