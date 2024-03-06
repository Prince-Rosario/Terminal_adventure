class Character:
    def __init__(self, time_of_day, location, mood):
        self.time_of_day = time_of_day
        self.location = location
        self.mood = mood

player = Character("morning", "home", "neutral")
locations = {
    "work": ["work", "eat", "read"],
    "home": ["relax", "eat", "sleep"],
    "park": ["relax", "exercise"],
    "gym": ["exercise"],
    "cafe": ["eat", "read"]
}

while True:
    print(f"Time of day: {player.time_of_day}, Location: {player.location}, Mood: {player.mood}")
    action = input("Choose an action: move, activity\n")

    if action == "move":
        location = input(f"Where do you want to move: {', '.join(locations.keys())}\n")
        if location in locations:
            player.location = location
        else:
            print("Invalid location. Try again.")
    elif action == "activity":
        activity = input(f"What activity do you want to do: {', '.join(locations[player.location])}\n")
        if activity in locations[player.location]:
            if activity == "work":
                player.mood = "tired"
                player.time_of_day = "afternoon"
            elif activity == "relax":
                player.mood = "happy"
                player.time_of_day = "evening"
            elif activity == "exercise":
                player.mood = "energetic"
                player.time_of_day = "afternoon"
            if activity == "eat":
                player.mood = "satisfied"
                if player.time_of_day == "morning":
                    player.time_of_day = "afternoon"
                elif player.time_of_day == "evening":
                    player.time_of_day = "night"
            elif activity == "read":
                player.mood = "calm"
                player.time_of_day = "evening"
            elif activity == "sleep":
                if player.time_of_day != "night":
                    print("You can't sleep now. It's not night yet.")
                else:
                    print("Good night!")
                    break
        else:
            print("Invalid activity. Try again.")
    else:
        print("Invalid action. Try again.")