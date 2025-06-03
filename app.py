#Christian Cyr
#6/2/2025
import constants
from statistics import mean

players = constants.PLAYERS
teams = constants.TEAMS

#Returns a cleaned list of dictionaries
def cleaned_data():
        cleaned = []
        
        for player in players:
            fixed = {}
            fixed['name'] = player['name']
            fixed['guardians'] = player['guardians']
            if player['experience'] == 'YES':
                fixed['experience'] = True
            else:
                fixed['experience'] = False
            fixed['height'] = int(player['height'].split(" ")[0])
            cleaned.append(fixed)
        return cleaned
#pre: list of dictionaries cleaned version
#post: Create as many lists as their are teams
#       and evenly distribute players to each list
#       List 0 should be team 0 etc... 
def balance_teams(players):
    playersPerTeam = len(players)/len(teams)
    print(len(players))
    print(len(teams))
    
    playerNo =0
    listPointer=0
    n = len(teams)
    listNeeded = [[] for x in range(n)]
    
    print(listNeeded)
    for player in players:
            if len(listNeeded[listPointer]) < playersPerTeam:
                listNeeded[listPointer].append(player)
                playerNo+=1
            else:
                listPointer+=1
                listNeeded[listPointer].append(player)
    return listNeeded
def display_menu(listNeeded):
    listOfPlayersToPrint = []
    print("\n---MENU---\n")
    print('''Below is a number next to each team. 
To find out information on a specific team,
press the number that is shown to the left of it.
    ''')
    for team in teams:
        print("{}: {}".format(teams.index(team),team))
    print("{}: Quit".format(len(teams)))
    try:
        teamSelection = int(input("Select number choice here: \t"))
    except:
        print("Invalid Input.")
    else:
        if(teamSelection == len(teams)):
            print("Quitting")
            quit()
        elif teamSelection > len(teams) or teamSelection < 0:
            print("Invalid input.")
        else:
            team_players = listNeeded[teamSelection]
            team_name = teams[teamSelection]
            show_team_details(team_name, team_players)
def show_team_details(team_name, players):
    print(f'Team: {team_name} Stats\n-------------------------------')
    print(f'Total Players: {len(players)}')
    num_experienced = 0
    num_inexperienced = 0
    guardian_list = []
    players_on_team = []
    for player in players:
        players_on_team.append(player["name"])
        guardians = player["guardians"].split(" and ")
        guardian_list.extend(guardians)
        if player["experience"] == True:
            num_experienced += 1
        else:
            num_inexperienced += 1
    avg_height = round(mean(player["height"] for player in players))
   
    print(f'Total experienced: {num_experienced}')
    print(f'Total inexperienced: {num_inexperienced}')
    print(f'Average Height: {avg_height}')
    print(f"Players:\n\t{', '.join(players_on_team)}")
    print(f"Guardians:\n\t{', '.join(guardian_list)}")




        
if __name__ == '__main__':
    cleaned_players = cleaned_data()
    
    listNeeded = balance_teams(cleaned_players) 
    display_menu(listNeeded)
