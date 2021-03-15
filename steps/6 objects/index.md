## Adventure: objects

Now that you are sure the game is playable using the Tiny and Small maps, let's implement the remaining feature needed to be able to play the Crowther map as well. As seen above, the data file contains descriptions for objects that are placed in the game (each in a default room) and then picked up, taken along, and dropped again by the player. The Crowther game is designed in a way that some routes can only be taken when the player is carrying certain objects.

Seeing items in the game should look like this:

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

Listing whay you have should look like this:

    > INVENTORY
    KEYS: a set of keys
    LAMP: a brightly shining brass lamp

To do this:

- you must implement a new `Item` class that represents objects within the game (it should be obvious that it would not be advisable to name a class `Object`, hence the alternative that we propose here). Place it in its own file `item.py`.

- then you should add variables such that each `Room` object can "contain" or point to several `Item` objects. And, because a game item cannot only reside in a given room, but also be picked up and kept by the player, you should also create a place in the `Adventure` class to contain `Item` objects.

- then you need to make sure objects are loaded from the data file and place into the correct initial rooms after loading.

- and finally, you can implement user interface code for items, in particular by modifying the `LOOK` command and implementing `TAKE` and `DROP` commands. But, note that you should always call methods on the `Adventure` class to do these actions! Do not directly manipulate elements (variables) from that class or from other classes.

And to test, don't forget to load the Crowther map:

    $ python adventure.py Crowther


## Step 8: Conditional movement

Having objects in possession can allow your player to move to different rooms than without those objects, which opens up possibilities not seen before (like winning!). This is encoded in the Crowther data file. For example, room 9 has the following connections:

    9	EAST	8	WEST	12/LAMP	WEST	10

The east and west exit each connect, in normal conditions, to rooms 8 and 10, respectively. However, when holding a lamp, the behaviour of the "WEST" command is changed, moving the player into room 12.

As you can see, you will need to change your code for reading the data files a bit. Then you'll also need to make changes to your `Room` class, the `Adventure` class and the main game loop!


