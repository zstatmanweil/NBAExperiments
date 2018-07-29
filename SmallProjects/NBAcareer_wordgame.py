from sys import exit

def start():
    print "Congratulations, you have been drafted to the NBA!"
    print "What number were you drafted?"

    pick = int(raw_input("> "))

    if pick > 60:
        retire("That is impossible, which means you weren't drafted after all.")
    elif pick in range (31, 61):
        print "Second round, not bad!"
        playoff()
    else:
        print "First round! Wow..."
        tank()

def tank():
    print "You have landed on a tanking team. Blame Sam Hinke."
    print "How do you approach this unfortunate problem?"

    choice = raw_input("> ")

    if "try" in choice:
        print "I have a good feeling about you..."
        tank()
    elif ("hard" in choice) or ("work" in choice):
        print "You turned this team around!"
        playoff()
    else:
        print "Sounds like you need some time in G-league"
        g_league()

def g_league():
    print "The G-league is a great place to hone your skills and improve your work ethic."
    print "What is your work ethic right now? High, medium or low?"

    work_ethic = raw_input ("> ")

    if work_ethic.lower() == "low":
        retire("I don't think the NBA is for you.")
    elif work_ethic.lower() == "medium":
        print "Sounds like you aren't ready to leave G-league."
        g_league()
    elif work_ethic.lower() == "high":
        "Your hard work paid off. A playoff team wants you - their star is injured!"
        playoff()
    else:
        retire("If you can't follow instructions, you can't follow plays.")

def playoff():
    print "You are now on a playoff contender. Buckle up. It is a long season."
    print "Do you arrive at the gym before or after 9am?"

    arrival_time = raw_input("> ")
    arrival_time = arrival_time.lower()

    if "before" in arrival_time:
        championship("You are the reason your team made it to the finals.")
    elif "after" in arrival_time:
        print "That doesn't cut it. You need some time in the G-league."
        g_league()
    else:
        tank()

def championship(happy):
    happy += " You won the championship!"
    retire(happy)


def retire(you):
    print you, "Enjoy the beach!"
    exit(0)

start()
