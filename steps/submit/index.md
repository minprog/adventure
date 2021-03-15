# Adventure: submit

Take another look at the constraints we noted earlier:

- A hard constraint in this program is that the `Room` class may not access (use) other classes. Its methods may only manipulate `self` and any access only objects that are passed to it as arguments to method calls.

- A hard constraint in this program is that the `Adventure` class may not `print` anything. And in return, the `__main__` part may, aside from printing things, only call methods in the `Adventure` class. It may not ever directly access methods and/or attributes from the `Room class`!

- Remember that only a few things work with the Tiny map. You should normally test the game using the Crowther map. `check50` will certainly do so!


## check50

	check50 -l minprog/adventure/2020/more


## style50

	style50 adventure.py
	style50 room.py
	style50 item.py
