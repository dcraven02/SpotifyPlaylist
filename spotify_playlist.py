"""
<   This code spotify_playlist.py is to be used for learning purposes only and should not be
    used a tool for any commercial purpose.
    All rights reserved ® 2019  David Craven
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# coding=utf-8
import sys
import spotipy
import spotipy.util as util


# Get the song_count top tracks from an artist why are you passing in 1 song_count value?
def get_top_songs_for_artist(artist, song_count=1):
    # Initializing the list of track ID
    song_ids = []

    # Search for the artist
    # https://spotipy.readthedocs.io/en/latest/#spotipy.client.Spotify.search
    artist_results = sp.search(q='artist:' + artist, type='artist', limit=1)

    #  If there is at least one artist returned from the search
    if artist_results['artists']['total']:
        # Get the artist ID
        artist_id = artist_results['artists']['items'][0]['id']
        # Fetch the top tracks of the artist
        artist_top_tracks = sp.artist_top_tracks(artist_id)
        # Get the length of the list of track
        # Check if the length is below the song_count
        # We are not looping "song_count" times but "artist_top_tracks" times.
        artist_top_tracks_length = len(artist_top_tracks['tracks'])
        # Appends the tracks ID to the list of tracks.
        # The limit is the number of tracks specified by song_count or the length of top tracks if less than song_count
        for x in range(0, artist_top_tracks_length if song_count > artist_top_tracks_length else song_count):
            # Appends the track ID to the list of tracks.
            # The tracks are in the list artist_top_tracks['tracks'].
            # Each track as an attribute 'id'
            song_ids.append(artist_top_tracks['tracks'][x]['id'])

        print(str(len(song_ids)) + ' songs found - ' + artist)
    else:
        print('Artist not found - ' + artist)

    return song_ids


# Get the tracks
def get_coachella_tracks():
    # Artist list
    artists = [
        '6LACK',
        'A Perfect Circle',
        'AC Slater',
        'Ahwlee',
        'Alan Walker',
        'alf alpha',
        'Alina Baraz',
        'Alison Wonderland',
        'alt-J',
        'Alvvays',
        'Amine',
        'Anabel Englund',
        'Anakim',
        'Angel Olsen',
        'Ardalan',
        'AURORA',
        'Avalon Emerson',
        'B Boys',
        'B. Traits',
        "Bane's World",
        'Barclay Crenshaw',
        'Bedouin',
        'Behrouz',
        'Belly',
        'Benjamin Booker',
        'Benjamin Clementine',
        'Beyoncé',
        'Big Thief',
        'Birdtastique',
        'Black Coffee',
        'blackbear',
        'Bleachers',
        'Bonobo',
        'Boogarins',
        'Brasstracks',
        'Britta Unders',
        'BROCKHAMPTON',
        'Buscabulla',
        'Busy P',
        'BØRNS',
        'Cardi B',
        'Carl Craig',
        'Carpenter Brut',
        'Cash Cash',
        'CharlesTheFirst',
        'Cherry Glazerr',
        'Chloe x Halle',
        'Chris Lake',
        'Chris Liebing',
        'Christian Martin',
        'Chromeo',
        'Chulita Vinyl Club',
        'Cuco',
        'CVSS',
        'Daniel Caesar',
        'David Byrne',
        'Declan McKenna',
        'deevo',
        'DeJ Loaf',
        'Deorro',
        'Dimond Saints',
        'Django Django',
        'DMM',
        'Dreams',
        'DROELOE',
        'Ekali',
        'Elohim',
        'Eminem',
        'EMME',
        'Eprom',
        'Father Bear',
        'Fazerdaze',
        'Feel Good Green',
        'FIDLAR',
        'First Aid Kit',
        'FISHER',
        'Flatbush Zombies',
        'Fleet Foxes',
        'Frameworks',
        'Francesca Harding',
        'French Montana',
        'Gabe Real',
        'Gabe Real + Juicewon',
        'Gingee',
        'Giraffage',
        'GoldFish',
        'Greta Van Fleet',
        'HAIM',
        'Hannah Wants',
        'Hayley Kiyoko',
        'Helado Negro',
        'Henry Pope',
        'Highly Suspect',
        'HITO',
        'Hundred Waters',
        'Ibeyi',
        'Illenium',
        'Jackmaster',
        'Jacob Banks',
        'Jamie Jones',
        'Jamiroquai',
        'Japanese Breakfast',
        'Jason Bentley',
        'Jean-Michel Jarre',
        'Jesse Calosso',
        'Jessie Ware',
        'Jidenna',
        'Jim Smith',
        'Jimbo Jenkins',
        'John Maus',
        'John Monkman',
        'Jorja Smith',
        'Joseph Capriati',
        'Juice won',
        'Jungle',
        'Just Pudge',
        'Justin Martin',
        'Kali Uchis',
        'Kamaiyah',
        'Kamasi Washington',
        'Kasbo',
        'Kelela',
        'King Krule',
        'KITTENS',
        'Knox Fortune',
        'Kygo',
        'Kyle Hall',
        'Kölsch',
        'LANY',
        'Late Night Laggers',
        'Lauren Lane',
        'Lee Wells',
        'LION BABE',
        'Loboman',
        'Los Ángeles Azules',
        'Louis The Child',
        'LP',
        'Luca Lush',
        'Luttrell',
        'LÉON',
        'Maceo Plex (Live)',
        'MAGIC GIANT',
        'Mansion',
        'Marian Hill',
        'Marvel Years',
        'MELVV',
        'MHD',
        'Michael Mayer',
        'Migos',
        'Miguel',
        'Mild High Club',
        'Monolink',
        'Moodymann',
        'Moon Boots',
        'Moscoman',
        'Moses Sumney',
        'Motor City Drum Ensemble',
        'mr. rotu',
        'Musty Boyz',
        'MØ',
        'N.A.A.F.I.',
        'Nile Rodgers & CHIC',
        'Noname',
        'nostradahm',
        'Nothing But Thieves',
        'ODESZA',
        'Oh Sees',
        'Oliver Koletski',
        'Omar-S',
        'Oshi',
        'Otoboke Beaver',
        'Pachanga Boys',
        'Party Favor',
        'Patricio',
        'Pax',
        'Peggy Gou',
        'Perfume Genius',
        'Petit Biscuit',
        'Phantom Thrett',
        'Pigeon Hole',
        'pluko',
        'Portugal. The Man',
        'Post Malone',
        'Priests',
        'Princess Nokia',
        'PVRIS',
        'Rex Orange County',
        'REZZ',
        'Rick G.',
        'Rolling Blackouts Coastal Fever',
        'Ron Gallo',
        'Russ',
        'Sacha Robotti',
        'Sage Armstrong',
        'Sahar Z',
        'Salami Rose Joe Lewis',
        'San Holo',
        'Señor Kino',
        'Sigrid',
        'Sir Sly',
        'Skip Marley',
        'Slow Magic',
        'Smiles Davis',
        'Snail Mail',
        'Snakehips',
        'SoDown',
        'Soulwax',
        'St. Vincent',
        'Sudan Archives',
        'SuperDuperKyle',
        'Surprise Guest',
        'SZA',
        'Talaboman',
        'Tank and the Bangas',
        'Tash Sultana',
        'The Black Madonna',
        'The Blaze',
        'The Bronx',
        'The Buttertones',
        'The Delirians',
        'The Drums',
        'The Marías',
        'The Neighbourhood',
        'The Regrettes',
        'The War On Drugs',
        'The Weeknd',
        'THEY.',
        'Thugf*cker',
        'Tom Misch',
        'Tor',
        'TroyBoi',
        'Tyler, the Creator',
        'Um..',
        'Vance Joy',
        'Vince Staples',
        'VNSSA',
        'Westside Gunn + Conway',
        'Whethan',
        'Willaris. K',
        'Worthy',
        'X Japan',
        'Xie',
        'Yaeji',
        'Yahtzel'
    ]

    all_track_ids = []

    # enumerate is a enumerator, it returns two values: the index (i) and the value (current_artist)
    for i, current_artist in enumerate(artists):
        # Set track limit
        api_track_add_limit = 100
        # Set top song per artist limit
        top_song_limit_per_artist = 2
        # Get the 2 top songs from the current artist
        top_artist_songs = get_top_songs_for_artist(current_artist, top_song_limit_per_artist)

        # If there is at list one song (if len of the list is > 0)
        if len(top_artist_songs):
            # Add the songs from this artist to the full list of songs
            all_track_ids.extend(top_artist_songs)
            # If you reach 100 songs or there is no more artists, we add the tracks to the spotify playlist
            if len(all_track_ids) + top_song_limit_per_artist > api_track_add_limit or (
                    i == len(artists) - 1 and len(all_track_ids)):
                # Adding the tracks to the playlist
                sp.user_playlist_add_tracks(user='xxxx', playlist_id='xxxx',
                                            tracks=all_track_ids)
                all_track_ids = []


if __name__ == '__main__':
    # Declare variable sp globally so it can be used in other functions
    global sp
    # sys.argv are the arguments of the scripts
    # sys.argv[0] is the name of the script
    # Then the following element of sys.argv are the arguments, so sys.argv[1] is the username
    if len(sys.argv) > 1:
        # Getting the username 'first argument'
        username = sys.argv[1]
    else:
        # Replace xxxx with your username
        print("You have not supplied your username")
        print("usage: python user_playlists.py xxxx")
        # Exit if no arguments provided
        sys.exit()
    # Use the API to get a token
    token = util.prompt_for_user_token(username,
                                       scope='playlist-modify-private,playlist-modify-public',
                                       client_id='xxxx',
                                       client_secret='xxxx',
                                       redirect_uri='https://localhost:8080/')

    if token:
        # If the token is valid, we authenticate to spotify. sp variable is then the spotify api
        sp = spotipy.Spotify(auth=token)
        # Get the tracks
        get_coachella_tracks()

    else:
        # Token is invalid
        print("Can't get token for", username)
