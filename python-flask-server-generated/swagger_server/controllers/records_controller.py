import connexion
import six

from swagger_server.models.artist import Artist  # noqa: E501
from swagger_server.controllers.authorization_controller import check_BasicAuth

from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server import util

import pandas as pd
import numpy as np

"""
import random
names = ["Name"+str(i) for i in range(10)]
usernames = ["username"+str(i) for i in range(10)]
rands = []
for i in range(10):
    rands.append(int(1+random.random()*3))
genres = ["Genre"+str(i) for i in rands]
albums = []
for i in range(10):
    albums.append(int(1+random.random()*50))
columns = ["artist_name", "artist_genre", "albums_recorded", "username"]
values = np.array([names, genres, albums, usernames]).T
df = pd.DataFrame(values, columns=columns)
df.to_csv("swagger_server/database/data.csv", index=False)
"""
DATA_PATH = "swagger_server/database/data.csv"
df = pd.read_csv(DATA_PATH)

def get_artists():
  """Get all books."""
  artists = []
  for _, artist in df.iterrows():
    artist_dto = Artist(artist.artist_name, artist.artist_genre, artist.albums_recorded, artist.username)
    artists.append(artist_dto)
  return artists

def artists_get(limit=None, offset=None):  # noqa: E501
    """artists_get

    Returns a list of artists # noqa: E501

    :param limit: Limits the number of items on a page
    :type limit: int
    :param offset: Specifies the page number of the artists to be displayed
    :type offset: int

    :rtype: List[Artist]
    """
    global df
    
    artists = get_artists()
    print(df)
    return artists


def artists_post(body):  # noqa: E501
    """artists_post

    Lets a user post a new artist # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    global df

    if connexion.request.is_json:
        body = Artist.from_dict(connexion.request.get_json())  # noqa: E501
        artist = pd.DataFrame.from_dict([connexion.request.get_json()])
        df = df.append(artist).reset_index(drop=True)
        df.to_csv(DATA_PATH, index=False)
        print(df)

    return 'Done!'


def artists_username_delete(username):  # noqa: E501
    """Delete an artist by username

     # noqa: E501

    :param username: 
    :type username: str

    :rtype: None
    """
    global df

    df = df.loc[df['username'] != username]
    df.to_csv(DATA_PATH, index=False)
    print(df)

    return 'Done!'


def artists_username_get(username):  # noqa: E501
    """artists_username_get

    Obtain information about an artist from his or her unique username # noqa: E501

    :param username: 
    :type username: str

    :rtype: Artist
    """
    global df

    artists = get_artists()
    entry = next(artist for artist in artists if artist.username == username)
    print(entry)

    return entry


def artists_username_put(body, username):  # noqa: E501
    """Update an artist by username

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param username: 
    :type username: str

    :rtype: None
    """
    global df
    
    if connexion.request.is_json:
        body = Artist.from_dict(connexion.request.get_json())  # noqa: E501
        artist = pd.DataFrame.from_dict([connexion.request.get_json()])
        df.loc[df.username == username] = artist.values
        df.to_csv(DATA_PATH, index=False)
        print(df)

    return 'Done!'
