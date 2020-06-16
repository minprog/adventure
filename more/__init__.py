import check50
import sys


less = check50.import_checks("../less")
from less import *

RUN_CROWTHER = f"{sys.executable} adventure.py Crowther"


room_3_description = ("You are inside a building, a well house for a large "
                      "spring. The exit door is to the south.  There is "
                      "another room to the north, but the door is barred by "
                      "a shimmering curtain.")
room_3_items = ["KEYS", "a set of keys", "\n", "WATER", "a bottle of water"]


@check50.check()
def item_exists():
    """item.py exists."""
    check50.exists("item.py")


@check50.check(game_over)
def find_items():
    """Finds items in rooms."""
    # Check initial description
    try:
        check = check50.run(RUN_CROWTHER).stdin("in")
        check.stdout(room_3_description, regex=False)

        for item in room_3_items:
            check.stdout(item, regex=False)
    except check50.Failure as error:
        raise check50.Failure(f"Could not find items upon first entering room.\n"
                              f"    Remember to seperate multiple items by a "
                              f"single newline.\n"
                              f"    {error}")

    # Check for look command
    try:
        check = check50.run(RUN_CROWTHER)
        moves = ["IN", "OUT", "IN", "LOOK"]

        for move in moves:
            check.stdout("> ")
            check.stdin(move, prompt=False)

        for item in room_3_items:
            check.stdout(item, regex=False)
    except check50.Failure as error:
        raise check50.Failure(f"Could not find items when using LOOK.\n"
                              f"    {error}")


@check50.check(find_items)
def handle_items():
    """Take and drop items."""
    # Take keys check
    check = check50.run(RUN_CROWTHER)
    moves = ["IN", "TAKE keys"]

    for move in moves:
        check.stdout("> ")
        check.stdin(move, prompt=False)

    check.stdout("KEYS taken", regex=False)

    # Drop keys check then look for dropped keys check
    check = check50.run(RUN_CROWTHER)
    moves = ["IN", "TAKE keys", "OUT", "DROP keys"]

    for move in moves:
        check.stdout("> ")
        check.stdin(move, prompt=False)

    check.stdout("KEYS dropped", regex=False)
    check.stdin("look").stdout("KEYS", regex=False)
    check.stdout("a set of keys", regex=False)

@check50.check(handle_items)
def handle_invalid_items():
    """Take and drop nonexistent items."""
    # Take a non-existent item.
    check = check50.run(RUN_CROWTHER).stdin("TAKE kes")
    check.stdout(no_item, regex=False)

    # Take an item twice.
    check = check50.run(RUN_CROWTHER)
    moves = ["IN", "TAKE keys", "TAKE keys"]

    for move in moves:
        check.stdout("> ")
        check.stdin(move, prompt=False)
    check.stdout(no_item, regex=False)

    # Drop non-existent item.
    check = check50.run(RUN_CROWTHER).stdin("DROP something")
    check.stdout(no_item, regex=False)


@check50.check(handle_items)
def inventory():
    """Using the INVENTORY command."""
    # Check empty inventory.
    try:
        check = check50.run(RUN_CROWTHER).stdin("INVENTORY")
        check.stdout("Your inventory is empty", regex=False)
    except check50.Failure as error:
        raise check50.Failure(f"Let the player know they have no items.\n"
                              f"    {error}")

    # Check having keys.
    check = check50.run(RUN_CROWTHER)
    moves = ["IN", "TAKE keys", "INVENTORY"]

    for move in moves:
        check.stdout("> ")
        check.stdin(move, prompt=False)

    check.stdout("KEYS", regex=False)
    check.stdout("a set of keys", regex=False)


@check50.check(handle_items)
def conditional_move():
    """Check if holding an item affects conditional movement."""
    check = check50.run(RUN_CROWTHER)
    moves = ["DOWN", "DOWN", "DOWN", "DOWN"]

    for move in moves:
        check.stdout("> ")
        check.stdin(move, prompt=False)

    check.stdout("The grate is locked and you don't have any keys.",
                 regex=False)

    check = check50.run(RUN_CROWTHER)
    moves = ["IN", "TAKE keys", "OUT",
             "DOWN", "DOWN", "DOWN", "DOWN"
             ]

    for move in moves:
        check.stdout("> ")
        check.stdin(move, prompt=False)

    check.stdout(room_8_description, regex=False)
    for item in room_8_items:
        check.stdout(item, regex=False)


@check50.check(conditional_move)
def multiple_conditional_move():
    """Check if holding multiple items affects conditional movement."""
    try:
        check = check50.run(RUN_CROWTHER)
        moves = ["IN", "TAKE KEYS", "OUT", "DOWN", "DOWN",
                 "DOWN", "DOWN", "TAKE LAMP", "IN", "WEST",
                 "WEST", "WEST", "TAKE BIRD", "WEST", "DOWN",
                 "SOUTH", "TAKE NUGGET", "OUT", "DROP NUGGET", "UP",
                 "EAST", "EAST", "EAST", "TAKE ROD", "WEST",
                 "WEST", "LOOK"
                 ]

        for move in moves:
            check.stdout("> ")
            check.stdin(move, prompt=False)
        check.stdout(room_14_description, regex=False)

        moves = ["EAST", "DROP BIRD", "WEST", "LOOK"]

        for move in moves:
            check.stdout("> ")
            check.stdin(move, prompt=False)
        check.stdout(room_15_description, regex=False)

    except check50.Failure as error:
        raise check50.Failure("Did not find correct room description when "
                              "going WEST from room 13 holding either BIRD & "
                              "ROD or just ROD.\n"
                              f"    {error}")


@check50.check(multiple_conditional_move)
def special_move():
    """Performing special moves such as JUMP or XYZZY."""
    try:
        check = check50.run(RUN_CROWTHER)
        moves = ["IN", "XYZZY"]

        for move in moves:
            check.stdout("> ")
            check.stdin(move, prompt=False)

        check.stdout("It is now pitch dark.  If you proceed you will "
                     "likely fall into a pit.", regex=False)
    except check50.Failure as error:
        raise check50.Failure("Could not perform XYZZY. Check "
                              "CrowtherAdv.dat for all the different"
                              "connections.")


@check50.check(special_move)
def won():
    """Testing Crowther Adventure win condition."""
    moves = ["IN", "TAKE KEYS", "OUT", "DOWN", "DOWN",
             "DOWN", "DOWN", "TAKE LAMP", "IN", "WEST",
             "WEST", "WEST", "TAKE BIRD", "WEST", "DOWN",
             "SOUTH", "TAKE NUGGET", "OUT", "DROP NUGGET", "UP",
             "EAST", "EAST", "EAST", "TAKE ROD", "WEST",
             "WEST", "WEST", "DOWN", "TAKE NUGGET", "WEST",
             "WAVE", "TAKE DIAMOND", "WEST", "SOUTH", "SOUTH",
             "EAST", "NORTH", "NORTH", "TAKE CHEST", "OUT",
             "WEST", "DOWN", "WEST", "DOWN", "NORTH",
             "EAST", "TAKE COINS", "OUT", "NORTH", "DOWN",
             "EAST", "DROP LAMP", "DROP BIRD", "DROP NUGGET", "DROP COINS",
             "NORTH", "TAKE EMERALD", "OUT", "TAKE LAMP", "TAKE BIRD",
             "TAKE NUGGET", "TAKE COINS", "WEST", "WEST", "WEST",
             "DOWN", "WATER", "TAKE EGGS", "NORTH", "DOWN",
             "OUT", "EAST", "EAST", "EAST", "UP",
             "SOUTH", "SOUTH", "WEST", "WAVE", "WEST",
             "SOUTH", "NORTH", "NORTH", "EAST", "DOWN",
             "EAST", "EAST", "XYZZY", "NORTH"
             ]
    check = check50.run(RUN_CROWTHER)

    for move in moves:
        check.stdout("> ")
        check.stdin(move, prompt=False)

    check.stdout("You have collected all the treasures and are admitted to "
                 "the Adventurer's Hall of Fame.  Congratulations!",
                 regex=False)
