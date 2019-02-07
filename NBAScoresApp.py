import json
from httplib import HTTPSConnection, HTTPResponse, HTTPMessage
from Tkinter import *
import tkFont
from ttk import *

balldontlie_url = "www.balldontlie.io"
spurs_games_url = "/api/v1/games?team_ids[]=27&seasons[]=2018&per_page=100";

def get_last_game():
	games_request = HTTPSConnection(balldontlie_url)
	games_request.request('GET', spurs_games_url)
	games_response = games_request.getresponse();
	games_data = json.loads(games_response.read())
	games = games_data['data']
	game_count = len(games)
	return games[game_count - 1]	

def display_game(root):
	team_font = tkFont.Font(size=44, weight='bold')
	score_font = tkFont.Font(size=50, weight='normal')
	separator_font = tkFont.Font(size=44, weight='bold')

	main_frame = Frame(root)

	visitor_team = Label(main_frame, text=last_game['visitor_team']['abbreviation'])
	visitor_team.config(font=team_font)
	visitor_team.grid(row=0, column=0)

	visitor_team_score = Label(main_frame, text=last_game['visitor_team_score'])
	visitor_team_score.config(font=score_font)
	visitor_team_score.grid(row=0, column=1)

	team_separator = Label(main_frame, text="-")
	team_separator.config(font=separator_font)
	team_separator.grid(row=0, column=2)

	home_team_score = Label(main_frame, text=last_game['home_team_score'])
	home_team_score.config(font=score_font)
	home_team_score.grid(row=0, column=3)

	home_team = Label(main_frame, text=last_game['home_team']['abbreviation'])
	home_team.config(font=team_font)
	home_team.grid(row=0, column=4)

	main_frame.pack()	

if __name__ == "__main__":
	last_game = get_last_game()

	root = Tk()
	root.title("NBA Scores App !")
	root.geometry("600x100")

	display_game(root)

	root.mainloop()
