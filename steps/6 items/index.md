# Adventure: items

Now that you are sure the game is playable using the Tiny and Small maps, let's implement the remaining feature needed to be able to play the **Crowther** map as well. As seen above, the data file contains descriptions for items that are placed in the game (each in a specific room) and then picked up, taken along, and dropped again by the player. The Crowther game is designed in a way that some routes can only be taken when the player is carrying certain items.

Items that are lying around in a room should look like this:

    You are inside a building, a well house for a large spring.
    KEYS: a set of keys

Picking up items should work like this:

    You are inside a building, a well house for a large spring.
    KEYS: a set of keys
    > TAKE KEYS
    KEYS taken.
    > TAKE KEYS
    No such item.
    > TAKE SOMETHING
    No such item.
    >

Putting down items should work like this:

    You are inside a building, a well house for a large spring.
    KEYS: a set of keys
    > TAKE KEYS
    KEYS taken.
    > DROP KEYS
    KEYS dropped.
    > DROP KEYS
    No such item.
    > TAKE KEYS
    KEYS taken.


## Implementation

- Implement a new `Item` class that represents items within the game. Place it in its own file `item.py`.

- Add an attribute to store `Item` objects in each `Room`. And, because a items can be picked up and held by the player, you should also create an attribute in the `Adventure` class to contain `Item` objects (what kind of variable would be appropriate for that?).

- Then make sure items are loaded from the data file and place into the correct initial rooms after loading.

- And finally, implement user interface code for items, in particular the `TAKE` and `DROP` commands. Do note that you should always call methods on the `Adventure` class to do these actions! Do not directly manipulate elements (variables) from that class or from other classes.

And to test, don't forget to load the Crowther map:

    $ python3 adventure.py Crowther
