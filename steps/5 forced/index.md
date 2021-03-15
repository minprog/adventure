## Adventure: forced movement

Sometimes a player will attempt a movement they cannot make. For example, in the Small adventure, when going WEST from the "Outside grate" room (6), one finds oneself at the edge of an "unpassable stream". The only way is going back the "Outside grate" room.

The adventure game has a special feature called `FORCED` movements. If a player enters a room that has a direction named `FORCED`, the full room description will be printed, but then the player will be immediately moved back to the connected room. After moving back, the connected room should print the short description, as usual for a room that has already been visited.

- You'll most likely want to do a check each time you move to a new room. If there's a `FORCED` connection in the new room, take a good look around and follow the forced route.

- As you're going to have to print the description, handle this in the main game loop and not in the `move` method! To accomplish this, you have to add a new method to the `Adventure` class:

    - `is_forced` will allow us to check if the current room has a forced connection

    - note that you can use the existing `get_long_description`!
