teams = []
player_list = []
points_scored = {}

events = [
    "Event 1",
    "Event 2",
    "Event 3",
    "Event 4",
    "Event 5"
]

event_entries = {}

points_table = {
    1: 35,
    2: 30,
    3: 25,
    4: 20,
    5: 15,
    6: 10,
    7: 5
}


# Validation

def valid_name(name):
    return name.strip() != ""


def valid_number(value):
    return value.isdigit() and int(value) > 0


# Add individual

def add_individual():
    if len(player_list) >= 20:
        print("Maximum of 20 individuals reached")
        return

    name = input("Enter individual name: ")

    if not valid_name(name):
        print("Invalid name")
        return

    if name in points_scored:
        print("Player already exists")
        return

    player_list.append(name)
    points_scored[name] = 0

    print("Individual added")


# Add team

def add_team():
    if len(teams) >= 4:
        print("Maximum of 4 teams reached")
        return

    team_name = input("Enter team name: ")

    if not valid_name(team_name):
        print("Invalid team name")
        return

    if team_name in points_scored:
        print("Team already exists")
        return

    members = []

    for i in range(5):
        member = input(f"Enter member {i + 1}: ")

        if not valid_name(member):
            print("Invalid member name")
            return

        members.append(member)

    teams.append({
        "name": team_name,
        "members": members
    })

    points_scored[team_name] = 0

    print("Team has been added")


# Register event

def register_event():
    print("\nEvents:")

    for i, event in enumerate(events, 1):
        print(i, event)

    name = input("Enter team or individual name: ")

    if name not in points_scored:
        print("Team or individual name is incorrect")
        return

    event_choice = input("Select an event between 1 and 5: ")

    if not valid_number(event_choice):
        print("Invalid event number. Please enter a valid number")
        return

    event_index = int(event_choice) - 1

    if event_index < 0 or event_index >= len(events):
        print("Event does not exist")
        return

    if name in event_entries:
        print("Already entered. One event only")
        return

    event_entries[name] = events[event_index]

    print("Registration successful")


# Points

def get_points(position):
    return points_table.get(position, 1)


# Enter results

def enter_results():
    print("\nCompetitors:")

    for competitor in points_scored:
        print(competitor)

    count = input("How many results? ")

    if not valid_number(count):
        print("Invalid number. Please enter a valid number")
        return

    count = int(count)

    for i in range(count):
        name = input(f"Position {i + 1}: ")

        if name in points_scored:
            points_scored[name] += get_points(i + 1)
        else:
            print("Competitor not found")

    print("Results saved")


# Leaderboard

def leaderboard():
    print("\nLEADERBOARD")

    leaderboard_list = sorted(
        points_scored.items(),
        key=lambda item: item[1],
        reverse=True
    )

    position = 1

    for name, score in leaderboard_list:
        print(position, name, score)
        position += 1


# Main menu

def main():
    while True:
        print("\n1. Add Team")
        print("2. Add Individual")
        print("3. Register Event")
        print("4. Enter Results")
        print("5. Leaderboard")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_team()

        elif choice == "2":
            add_individual()

        elif choice == "3":
            register_event()

        elif choice == "4":
            enter_results()

        elif choice == "5":
            leaderboard()

        elif choice == "6":
            print("Program closed")
            break

        else:
            print("Invalid choice")


main()