# Adventure: submit

Here are the constraints that we noted earlier:

- A hard constraint in this program is that the `Room` class may not access (use) other classes. Its methods may only manipulate `self` and any access only objects that are passed to it as arguments to method calls.

- A hard constraint in this program is that the `Adventure` class may not `print` anything. And in return, the `__main__` part may, aside from printing things, only call methods in the `Adventure` class. It may not ever directly access methods and/or attributes from the `Room` or other classes!

- Remember that only a few things work with the Tiny and Small maps. You should normally test the game using the Crowther map. `check50` will certainly do so!

Keep these in mind before submitting your final solution.

## Punten

Let op de punten die je kan krijgen deze week! Die staan vermeld in het overzicht.

## Zipping and submitting

To submit, you will need a zip-file containing just the Python files for your solution. These files may not be located in a subfolder inside the zip! So please follow the steps below.

`cd` into the folder that contains `adventure.py` and then run this command to zip your solution:

    zip adventure-submit.zip *.py

<!--
## check50

    check50 -l minprog/adventure/2020/more


## style50

    style50 adventure.py
    style50 room.py
    style50 loader.py
    style50 item.py
 -->

## That's it!

Phew, what a week. You've been thoroughly practicing with using objects and classes. We're glad that you have come this far. Now go ahead and play your own Adventure!
