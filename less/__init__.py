import check50
import sys
import os

RUN_TINY = f"{sys.executable} adventure.py Tiny"
RUN_SMALL = f"{sys.executable} adventure.py Small"

room_1_name = "Outside building"
room_1_description = ("You are standing at the end of a road before a "
                      "small brick building.  A small stream flows out of "
                      "the building and down a gully to the south.  A road "
                      "runs up a small hill to the west.")

room_2_name = "End of road"
room_2_description = ("You are at the end of a road at the top of a small "
                      "hill. You can see a small building in the valley to "
                      "the east.")

room_3_name = "Inside building"
room_3_description = ("You are inside a building, a well house for a large "
                      "spring.")
room_3_items = ["KEYS", "a set of keys"]

room_6_name = ["Outside grate"]
room_6_description = ["You are in a 25-foot depression floored with bare dirt. "
                      "Set into the dirt is a strong steel grate mounted in concrete.  "
                      "A dry streambed leads into the depression from the north."]

room_8_name = "Beneath grate"
room_8_description = ("You are in a small chamber beneath a 3x3 steel "
                      "grate to the surface.  A low crawl over cobbles "
                      "leads inward to the west.")
room_8_items = ["LAMP", "a brightly shining brass lamp"]

room_14_description = ("You are in a splendid chamber thirty feet high.  "
                       "The walls are frozen rivers of orange stone.  A narrow "
                       "canyon and a good passage exit from east and west "
                       "sides of the chamber.")
room_15_description = ("You are in a splendid chamber thirty feet high.  "
                       "The walls are frozen rivers of orange stone.  A narrow "
                       "canyon and a good passage exit from east and west "
                       "sides of the chamber. High in the cavern, you see a "
                       "little bird flying around the rocks.  It takes one "
                       "look at the black rod and quickly flies out of sight.")

help_statement = ["EAST/WEST/IN/OUT", "QUIT quits", "HELP prints",
                  "LOOK lists"]
no_item = "No such item"


@check50.check()
def exists():
    """Checking if all files exist."""
    check50.include("../data")
    check50.exists("adventure.py")
    check50.exists("room.py")


@check50.check(exists)
def move_once():
    """Starting Adventure then moving once to the WEST."""
    try:
        check50.run(RUN_TINY).stdout(room_1_description, regex=False)
    except check50.Failure as error:
        raise check50.Failure(f"Expected the description of initial "
                              f"room when Adventure starts.\n    {error}")
    check50.run(RUN_TINY).stdin("WEST").stdout(room_2_description,
                                               regex=False)


@check50.check(move_once)
def move_invalid():
    """Attempt to move EAST into an unconnected room."""
    check50.run(RUN_TINY).stdin("EAST").stdout("Invalid command")


@check50.check(move_once)
def move_repeatedly():
    """Moving WEST, EAST, WEST in succession."""
    check = check50.run(RUN_TINY)
    check.stdin("WEST").stdout(room_2_description, regex=False)
    check.stdin("EAST").stdout(room_1_name, regex=False)
    check.stdin("WEST").stdout(room_2_name, regex=False)


@check50.check(move_repeatedly)
def move_mixed_case():
    """Move with mixed case command."""
    check50.run(RUN_TINY).stdin("west").stdout(room_2_description,
                                               regex=False)
    check50.run(RUN_TINY).stdin("wESt").stdout(room_2_description,
                                               regex=False)
    check50.run(RUN_TINY).stdin("west").stdin("EAST").stdout(room_1_name,
                                                             regex=False)


@check50.check(move_mixed_case)
def helper_commands():
    """Testing helper commands; HELP, LOOK, QUIT."""
    # Test HELP
    try:
        check = check50.run(RUN_TINY).stdin("HELP")
        for help in help_statement:
            check.stdout(help)
    except check50.Failure as error:
        raise check50.Failure(f"HELP did not print the expected message.\n"
                              f"    {error}")

    # Test LOOK command
    try:
        check50.run(RUN_TINY).stdin("LOOK").stdout(room_1_description,
                                                      regex=False)
    except check50.Failure as error:
        raise check50.Failure(f"LOOK did not print the expected room"
                              f"description.\n    {error}")

    try:
        check50.run(RUN_TINY).stdin("look").stdout(room_1_description,
                                                   regex=False)
    except check50.Failure as error:
        raise check50.Failure(f"look (lowercase) did not print the expected room"
                              f"description.\n    {error}")

    # Test QUIT
    try:
        check50.run(RUN_TINY).stdin("QUIT").exit(0)
    except check50.Failure as error:
        raise check50.Failure(f"QUIT did not function as expected.\n"
                              f"    {error}")


@check50.check(helper_commands)
def commands():
    """Test if program handles nonexistent commands."""
    # Check invalid command
    try:
        check = check50.run(RUN_TINY).stdin("cs50")
        check.stdout("Invalid command", regex=False)
    except check50.Failure as error:
        raise check50.Failure(f"did not print 'Invalid command' when using 'cs50' as command.\n"
                              f"    {error}")


@check50.check(helper_commands)
def forced_move():
    """Checking if FORCED immediately moves the player."""
    check = check50.run(RUN_SMALL)
    moves = ["DOWN", "DOWN", "DOWN", "WEST"]

    for move in moves:
        check.stdout("> ")
        check.stdin(move, prompt=False)

    check.stdout("You find yourself at the edge of a impassible stream. You head back to the depression.",
                 regex=False)
    check.stdout("Outside grate", regex=False)


@check50.check(forced_move)
def synonyms():
    """Checking if command synonyms are handled correctly"""
    check = check50.run(RUN_SMALL)
    check.stdin("W").stdout(room_2_description, regex=False)
    check.stdin("E").stdout(room_1_name, regex=False)

    # check with nonsensical synonyms
    check50.log('changing Synonyms.dat to contain nonsensical synonyms...')
    os.rename(r'data/Synonyms.dat', r'data/Synonyms2.dat')
    os.rename(r'data/NonsensicalSynonyms.dat', r'data/Synonyms.dat')
    check = check50.run(RUN_SMALL)

    try:
        check.stdin("G").stdout(room_2_description, regex=False)
        check.stdin("F").stdout(room_1_name, regex=False)
    except check50.Failure as error:
        raise check50.Failure(f"{error}\n"
                              f"    Your program didn't handle a different Synonyms.dat correctly. Did you hardcode the synonyms?")

    os.rename(r'data/Synonyms.dat', r'data/NonsensicalSynonyms.dat')
    os.rename(r'data/Synonyms2.dat', r'data/Synonyms.dat')

@check50.check(synonyms)
def game_over():
    """Checking if the program correctly handles winning/losing."""

    # check won
    check = check50.run(RUN_SMALL)
    moves = ["DOWN", "DOWN", "DOWN", "DOWN", "WEST", "WEST", "WEST", "WEST"]

    for move in moves:
        check.stdout("> ")
        check.stdin(move, prompt=False)

    check.stdout('You\'ve found the hidden path to victory. Unfortunately, '
                 'the passage is blocked by a barrier marked "Under Construction."',
                 regex=False)

    # check lost
    check = check50.run(RUN_SMALL)
    moves = ["DOWN", "DOWN", "DOWN", "DOWN", "WEST", "WEST", "SOUTH"]

    for move in moves:
        check.stdout("> ")
        check.stdin(move, prompt=False)

    check.stdout('You fell into a pit and broke every bone in your body!',
                 regex=False)
