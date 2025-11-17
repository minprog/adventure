# Adventure: winning

Now that you have implemented:

- movement
- forced movement
- conditional movement

... it's time to tie up loose ends, so you have a playable game.

To allow someone to actually win the game, you need to take a good look at your logic and change it a little.

Near the end of the Crowther game (take a look at the data file!) there is a series of FORCED movements between rooms that should be automatically followed through all the rooms. And to make it even more complicated, these FORCED exits are also conditional. After a series of conditional forced movements, the player could be automatically dropped in room 77, but unfortunately they could also end up room 3 again.

> When looking at the data file, you might realize that having two conditional exits in a room works a little bit like an if-else statement!

Chances are that you did not fully implement that yet, so check the data file and your code thoroughly. If all is well, you should be able to play and win the game... and your code will pass through the checks!
