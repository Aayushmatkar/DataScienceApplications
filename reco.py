from typing import List
from flask import Flask, request, jsonify
import pandas as pd 
import random

# Load the pickle model
with open('model.pkl', 'rb') as f:
    #model = pickle.load(f)
    model = pd.read_pickle('model.pkl')
import random

movie_titles = [
    "The Godfather",
    "The Shawshank Redemption",
    "The Dark Knight",
    "The Godfather: Part II",
    "12 Angry Men",
    "Schindler's List",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "Forrest Gump",
    "Inception",
    "The Matrix",
    "Goodfellas",
    "Fight Club",
    "Star Wars: Episode V - The Empire Strikes Back",
    "The Silence of the Lambs",
    "The Usual Suspects",
    "The Prestige",
    "The Departed",
    "Gladiator",
    "Saving Private Ryan",
    "The Green Mile",
    "The Lion King",
    "Toy Story",
    "Jurassic Park",
    "Avatar",
    "Titanic",
    "The Terminator",
    "Alien",
    "Blade Runner",
    "Back to the Future",
    "Indiana Jones and the Raiders of the Lost Ark",
    "Jaws",
    "E.T. the Extra-Terrestrial",
    "The Breakfast Club",
    "Ferris Bueller's Day Off",
    "The Princess Bride",
    "When Harry Met Sally...",
    "The Shawshank Redemption"
]

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def home():
  return 'OK', 200


def format_response(texts: List[str]) -> jsonify:
  return jsonify({"fulfillmentMessages": [{"text": {"text": texts}}]})


@app.route('/dialogflow', methods=['GET','POST'])
def dialogflow():
  data = request.get_json()


  recommendations = ['Batman', 'Batman & Robin', 'The Dark Knight', 'The Dark Knight Rises', 'Batman Begins','Batman Returns']
  recommendations2 = ['Quantum of Solace','Never Say Never Again','Skyfall','Thunderball','From Russia with Love']
  recommendations3 = ['Titan A.E.','Small Soldiers','Enders Game','Aliens vs Predator: Requiem','Independence Day']

  
  action = data['queryResult']['action']

  if action == 'getrec':
    response = format_response([f'here are your recommendations {recommendations3}.'])
  elif action == 'movierec':
    response = format_response([f'here are your recommendations {recommendations2}.'])
  elif action == 'recc':
    response = format_response([f'here are your recommendations {recommendations}.'])
  elif action == 'surprisemovie':
    response = format_response([f'surprise movie recc {random.choice(movie_titles)}.'])
  return response