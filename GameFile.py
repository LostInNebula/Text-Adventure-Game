import sys
import time

def tryagain():
    time.sleep(0.5)
    print("""
        ------------------------------------------------------------------------
        You wake up in a strange room, however you had a weird dream involving
        a desk and a door. In the room you coincidentally notice a desk and a
        door. You have 3 choices, you can investigate the desk, investigate the
        door, or go back to sleep.

        Type your choice: Desk, Door, or Sleep
        ------------------------------------------------------------------------
    """)
    c1 = input()
    time.sleep(0.5)
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "SLEEP":
            print("""
        ------------------------
        You went back to sleep
        ------------------------""")
            ans = "incorrect"
            time.sleep(0.5)
            print("""
                ----------------------------------------------------------------
                You wake up in a strange room, however you had a weird dream
                involving a desk and a door. In the room you coincidentally
                notice a desk and a door. You have 3 choices, you can
                investigate the desk, investigate the door, or go back to sleep.

                Type your choice: Desk, Door, or Sleep
                ----------------------------------------------------------------
            """)
            c1 = input()
        elif c1.upper() == "DOOR":
            print("""
        --------------------------------------------
        You walk over to the door to investigate it
        --------------------------------------------""")
            ans = 'correct'
            scene2b()
        elif c1.upper() == "DESK":
            print("""
        --------------------------------------------
        You walk over to the desk to investigate it
        --------------------------------------------""")
            ans = 'correct'
            scene2a()
        if c1.upper() != "DOOR" and c1.upper() != "SLEEP" and c1.upper() != "DESK":
            ans = "incorrect"
            print("""
        --------------------------------------------------
        Please type a valid choice: Desk, Door, or Sleep
        --------------------------------------------------""")
            c1 = input()

def goback():
    time.sleep(0.5)
    print("""
        -----------------------------------------------------------------------
        You returned to where you started, in the room you have noticed a desk
        and a door. You have 3 choices, investigate the desk, investigate
        the door, or go back to sleep.

        Type your choice: Desk, Door, or Sleep
        -----------------------------------------------------------------------
    """)

    c1 = input()
    time.sleep(0.5)
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "SLEEP":
            print("""
        ------------------------
        You went back to sleep.
        ------------------------""")
            ans = "correct"
            tryagain()
        elif c1.upper() == "DOOR":
            print("""
        --------------------------------------------
        You walk over to the door to investigate it
        --------------------------------------------""")
            ans = 'correct'
            scene2b()
        elif c1.upper() == "DESK":
            print("""
        -------------------------------------------------
        You walk over to the desk to investigate it
        -------------------------------------------------""")
            ans = 'correct'
            scene2a()
        if c1.upper() != "DOOR" and c1.upper() != "SLEEP" and c1.upper() != "DESK":
            ans = "incorrect"
            print("""
        --------------------------------------------------
        Please type a valid choice: Desk, Door, or Sleep
        --------------------------------------------------""")
            c1 = input()

def scene1():
    time.sleep(0.5)
    print("""
        ------------------------------------------------------------------------
        WELCOME TO THE GRESH'S GAMES 2.0!
        Let us begin!

        You wake up in a strange room, in the room you notice a desk and a door.
        You have 3 choices, you can investigate the desk, investigate the door,
        or go back to sleep.

        Type your choice: Desk, Door, or Sleep
        ------------------------------------------------------------------------
    """)

    c1 = input()
    time.sleep(0.5)
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "SLEEP":
            print("""
        ------------------------
        You went back to sleep.
        ------------------------""")
            ans = "correct"
            tryagain()
        elif c1.upper() == "DOOR":
            print("""
        --------------------------------------------
        You walk over to the door to investigate it
        --------------------------------------------""")
            ans = 'correct'
            #scence2b
        elif c1.upper() == "DESK":
            print("""
        --------------------------------------------
        You walk over to the desk to investigate it
        --------------------------------------------""")
            ans = 'correct'
            scene2a()
        if c1.upper() != "DOOR" and c1.upper() != "SLEEP" and c1.upper() != "DESK":
            ans = "incorrect"
            print("""
        --------------------------------------------------
        Please type a valid choice: Desk, Door, or Sleep
        --------------------------------------------------""")
            c1 = input()

def scene2a():
    time.sleep(0.5)
    print("""
        ----------------------------------
        You notice the desk has a drawer.
        Type your choice: Open or Go Back
        ----------------------------------
    """)
    c1 = input()
    time.sleep(0.5)
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "OPEN":
            print("""
        -----------------------
        You opened the drawer
        -----------------------""")
            ans = 'correct'
            scene2aa()
        elif c1.upper() == "GO BACK":
            print("""
        -----------------------------------
        You walk back to where you started
        -----------------------------------""")
            ans = 'correct'
            goback()
        elif c1.upper() != "OPEN" and c1.upper() != "GO BACK":
            ans = "incorrect"
            print("""
        --------------------------------------------
        Please type a valid choice: Open or Go back
        --------------------------------------------""")
            c1 = input()

def scene2aa():
    time.sleep(0.5)
    print("""
        -------------------------------------
        Inside the drawer you find a key
        Type your choice: Grab Key or Go Back
        -------------------------------------
    """)
    c1 = input()
    time.sleep(0.5)
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "GRAB KEY":
            print("""
        ------------------------------------------------------------
        You go to grab the key from the drawer and close the drawer
        ------------------------------------------------------------""")
            ans = 'correct'
            scene2ab()
        elif c1.upper() == "GO BACK":
            print("""
        ----------------------------------------------------
        You close the drawer walk back to where you started
        ----------------------------------------------------""")
            ans = 'correct'
            goback()
        elif c1.upper() != "GRAB KEY" and c1.upper() != "GO BACK":
            ans = "incorrect"
            print("""
        ------------------------------------------------
        Please type a valid choice: Grab Key or Go Back
        ------------------------------------------------""")
            c1 = input()

def scene2ab():
    time.sleep(0.5)
    print("""
        ----------------------------------
        You now have the key from the drawer
        Type your choice: Stay or Go Back
        ----------------------------------
    """)
    c1 = input()
    time.sleep(0.5)
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "STAY":
            print("""
        ---------------------
        You stay at the desk
        ---------------------""")
            ans = "incorrect"
            time.sleep(0.5)
            print("""
                ----------------------------------
                You now have the key from the drawer
                Type your choice: Stay or Go Back
                ----------------------------------
            """)
            c1 = input()
        elif c1.upper() == "GO BACK":
            print("""
        -----------------------------------
        You walk back to where you started
        -----------------------------------""")
            ans = 'correct'
            scene2ac()
        elif c1.upper() != "STAY" and c1.upper() != "GO BACK":
            ans = "incorrect"
            print("""
        ---------------------------------------------
        Please type a valid choice: Stay or Go Back
        ---------------------------------------------""")
            c1 = input()

def scene2ac():
    time.sleep(0.5)
    print("""
        ---------------------------------------------------------------------
        You returned to where you started with the key from the desk's drawer
        You have 3 choices, investigate the door, go back to the desk, or go
        back to sleep.
        Type your choice: Door, Desk, or Sleep
        ---------------------------------------------------------------------
    """)

    c1 = input()
    time.sleep(0.5)
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "SLEEP":
            print("""
        ------------------------
        You went back to sleep.
        ------------------------""")
            ans = "correct"
            tryagain()
        elif c1.upper() == "DOOR":
            print("""
        --------------------------------------------
        You walk over to the door to investigate it
        --------------------------------------------""")
            ans = 'correct'
            scene2ad()
        elif c1.upper() == "DESK":
            print("""
        -------------------------------
        You walk back over to the desk
        -------------------------------""")
            ans = 'correct'
            scene2ax()
        if c1.upper() != "DOOR" and c1.upper() != "SLEEP" and c1.upper() != "DESK":
            ans = "incorrect"
            print("""
        --------------------------------------------------
        Please type a valid choice: Desk, Door, or Sleep
        --------------------------------------------------""")
            c1 = input()

def scene2ax():
    time.sleep(0.5)
    print("""
        -----------------------------------------
        You returned to the desk
        Type your choice: Open, Stay, or Go Back
        -----------------------------------------
    """)
    c1 = input()
    time.sleep(0.5)
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "STAY":
            print("""
        ---------------------
        You stay at the desk
        ---------------------""")
            ans = "incorrect"
            time.sleep(0.5)
            print("""
                ----------------------------------
                You already have the key from the drawer
                Type your choice: Open, Stay, or Go Back
                ----------------------------------
            """)
            c1 = input()
        elif c1.upper() == "GO BACK":
            print("""
        -----------------------------------
        You walk back to where you started
        -----------------------------------""")
            ans = 'correct'
            scene2ac()
        elif c1.upper() == "OPEN":
            print("""
        -------------------------------------------
        You open the desk's drawer to find nothing.
        You close the desk's drawer
        -------------------------------------------""")
            ans = 'incorrect'
            time.sleep(0.5)
            print("""
                ----------------------------------
                You already have the key from the drawer
                Type your choice: Open, Stay, or Go Back
                ----------------------------------
            """)
            c1 = input()
        if c1.upper() != "STAY" and c1.upper() != "GO BACK" and c1.upper() != "OPEN":
            ans = "incorrect"
            print("""
        ---------------------------------------------------
        Please type a valid choice: Open, Stay, or Go Back
        ---------------------------------------------------""")
            c1 = input()

def scene2ad():
    time.sleep(0.5)
    print("""
        -------------------------------------------------
        You notice the door's knob and its lock

        Type your choice: Turn Knob, Use Key, or Go Back
        -------------------------------------------------
    """)

    c1 = input()
    time.sleep(0.5)
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "GO BACK":
            print("""
        -----------------------------------
        You walk back to where you started
        -----------------------------------""")
            ans = 'correct'
            scene2ac()
        elif c1.upper() == "TURN KNOB":
            print("""
        ------------------------------------------
        You turn the knob, but the door is locked
        ------------------------------------------""")
            ans = 'incorrect'
            time.sleep(0.5)
            print("""
                -------------------------------------------------
                You notice the door's knob and its lock

                Type your choice: Turn Knob, Use Key, or Go Back
                -------------------------------------------------
            """)
            c1 = input()
        if c1.upper() == "USE KEY":
            print("""
        ---------------------------------------------------
        You have used the key and the door is now unlocked
        ---------------------------------------------------""")
            ans = 'correct'
            scene2ae()

        if c1.upper() != "GO BACK" and c1.upper() != "TURN KNOB" and c1.upper() != "USE KEY":
            ans = "incorrect"
            print("""
        --------------------------------------------------
        Please type a valid choice: Desk, Door, or Sleep
        --------------------------------------------------""")
            c1 = input()


def scene2ae():
    time.sleep(0.5)
    print("""
        ---------------------------------------------------
        With the door unlocked, you are now free to leave!

        Type your choice: Leave or Go Back
        ---------------------------------------------------
    """)
    c1 = input()
    time.sleep(0.5)
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "GO BACK":
            print("""
        -----------------------------------
        You walk back to where you started
        -----------------------------------""")
            ans = 'correct'
            scene2aex()
        elif c1.upper() == "LEAVE":
            print("""
        ----------------------------------------
        You open the door and leave!
        Congratulations! You have won the game!
        ----------------------------------------""")
            ans = 'correct'
            end()
        if c1.upper() != "GO BACK" and c1.upper() != "LEAVE":
            ans = "incorrect"
            print("""
        ---------------------------------------------
        Please type a valid choice: Go Back or Leave
        ---------------------------------------------""")
            c1 = input()

def scene2aex():
    time.sleep(0.5)
    print("""
        ---------------------------------------------------------------------
        You returned to where you started after unlocking the door
        You have 3 choices, go back to the door, go back to the desk, or go
        back to sleep.
        Type your choice: Door, Desk, or Sleep
        ---------------------------------------------------------------------
    """)

    c1 = input()
    time.sleep(0.5)
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "SLEEP":
            print("""
        ------------------------
        You went back to sleep.
        ------------------------""")
            ans = "correct"
            tryagain()
        elif c1.upper() == "DOOR":
            print("""
        --------------------------------------------
        You walk back over to the unlocked door
        --------------------------------------------""")
            ans = 'correct'
            scene2ae()
        elif c1.upper() == "DESK":
            print("""
        -------------------------------
        You walk back over to the desk
        -------------------------------""")
            ans = 'correct'
            scene2axx()
        if c1.upper() != "DOOR" and c1.upper() != "SLEEP" and c1.upper() != "DESK":
            ans = "incorrect"
            print("""
        --------------------------------------------------
        Please type a valid choice: Desk, Door, or Sleep
        --------------------------------------------------""")
            c1 = input()

def scene2axx():
    time.sleep(0.5)
    print("""
        -----------------------------------------
        You returned to the desk
        Type your choice: Open, Stay, or Go Back
        -----------------------------------------
    """)
    c1 = input()
    time.sleep(0.5)
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "STAY":
            print("""
        ---------------------
        You stay at the desk
        ---------------------""")
            ans = "incorrect"
            time.sleep(0.5)
            print("""
                -------------------------------------
                There is nothing to do with the desk
                Type your choice: Open, Stay, or Go Back
                -------------------------------------
            """)
            c1 = input()
        elif c1.upper() == "GO BACK":
            print("""
        -----------------------------------
        You walk back to where you started
        -----------------------------------""")
            ans = 'correct'
            scene2aex()
        elif c1.upper() == "OPEN":
            print("""
        -------------------------------------------
        You open the desk's drawer to find nothing.
        You close the desk's drawer
        -------------------------------------------""")
            ans = 'incorrect'
            time.sleep(0.5)
            print("""
                ----------------------------------
                There is nothing to do with the desk
                Type your choice: Open, Stay, or Go Back
                ----------------------------------
            """)
            c1 = input()
        if c1.upper() != "STAY" and c1.upper() != "GO BACK" and c1.upper() != "OPEN":
            ans = "incorrect"
            print("""
        ---------------------------------------------------
        Please type a valid choice: Open, Stay, or Go Back
        ---------------------------------------------------""")
            c1 = input()

def scene2b():
    time.sleep(0.5)
    print("""
        -------------------------------------------------
        You notice the door's knob and its lock

        Type your choice: Turn Knob or Go Back
        -------------------------------------------------
    """)
    c1 = input()
    time.sleep(0.5)
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "TURN KNOB":
            print("""
        ------------------------------------------
        You turn the knob, but the door is locked
        ------------------------------------------""")
            ans = 'incorrect'
            time.sleep(0.5)
            print("""
                -------------------------------------------------
                You notice the door's knob and its lock

                Type your choice: Turn Knob or Go Back
                -------------------------------------------------
            """)
            c1 = input()
        elif c1.upper() == "GO BACK":
            print("""
        -----------------------------------
        You walk back to where you started
        -----------------------------------""")
            ans = 'correct'
            goback()

def end():
    time.sleep(5)
    print("Goodbye!")
    sys.exit()

def start():
    scene1()

start()
