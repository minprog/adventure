## Step 5: Implement BACK

> Before continuing, make sure your program still works if you transition from the **Tiny** map to the **Small** map! From now on, when testing, run the game like this: `$ python adventure.py Small`. The **Small** map data file also contains items, no need to parse these just yet. You can ignore them for now.

Sometimes you make a mistake in playing Adventure and you'd like to go `BACK`. This is not always easy. We will provide a "secret" command that will take the player back to the previous room.

This is one feature that is also known as the "Undo" command in various other programs. The approach that we will take here is save references to all rooms that we pass and when asked to go `BACK`, we take the previous room and move there.

### History class

To implement this, create a class called `History` in a separate file called `history.py`, which will behave quite like a *stack ADT*. You can push a room onto it, and you can retrieve the previous room. It doesn't have to do much more! Be sure to create appropriate methods.

> Tip: You can interactively test your history class in the Python repl with `python3 -i history.py`

### Keep track of visited rooms

Have `Adventure` hold an instance of `History`. Everytime a room is *left* for another room, push the room to that history. 

### Go `BACK`

Now make the `BACK` command work. First, add a `method` to adventure for going back, `def back(self)` perhaps? Then add the `BACK` command to the main loop of your program. 
 
## Testing

Be sure to run `$ python adventure.py Small`, take a few steps, and see if you can retrace your steps with multiple by calling `BACK` multiple times.