import pickle
import webbrowser

#global dictionary
song_list = {}

""" This class assigns a song URL to a chosen name. """
class URLAssignment():

    global song_list

    """ This function creates a dictionary of songs and their names. """
    def song_assign(self, song_url, assigned_name):
        song_list.update({assigned_name: song_url})
        self.save_song()

    """ This function saves the dictionary to a file. """
    def save_song(self):
        with open('song_list.pkl', 'wb') as f:
            pickle.dump(song_list, f, pickle.HIGHEST_PROTOCOL)

""" This class removes songs. """
class RemoveSong():

    global song_list

    """ This function removes a song, and makes sure that
    an inputted name matches. """
    def song_delete(self, song_name):
        if song_name not in song_list.keys():
            print("Invalid selection")
            print()
            return
        del song_list[song_name]

""" This class plays the specified song. """
class PlaySong():

    global song_list

    """ This function takes in url, brings the user to a webbrowser
    and makes sure that an inputted name matches. """
    def name_identifier(self, assigned_name):
        song_list = self.load_song()
        if assigned_name not in song_list.keys():
            print("Invalid selection")
            print()
            return

        webbrowser.open(song_list[assigned_name])

    """ This function prints out list of songs before selecting one. """
    def load_song(self):
        with open('song_list.pkl', 'rb') as f:
            return pickle.load(f)

""" These variables instantiate the classes into objects. """
url_assignment = URLAssignment()
play_song = PlaySong()
remove_song = RemoveSong()

"""
This code block tests to see if a list exists, and if not,
creates an empty one.
"""
try:
    song_list = play_song.load_song()
except:
    song_list = {}
    url_assignment.save_song()

#while loop that runs through the options until users quits
while True:

    #shows user their choices to either save or play a song
    choice = input('Save song? (press 1)'
                            + '\n' +
                    'Play song? (press 2)'
                            + '\n' +
                    'Delete song? (press 3)'
                            + '\n' +
                    'QUIT (press 4)'
                            + '\n')

    #if user selects option 1, they are told to input a song and name
    if choice == '1':
        url = input('Enter URL: ')
        song_name = input('Enter song name: ')
        print()
        url_assignment.song_assign(url, song_name)

        """ Test #1: checks to make sure a url is properly added """
        assert song_list[song_name] == url
    #if user selects option 2, they are told to input a song to play
    elif choice == '2':
        song_list = play_song.load_song()
        print("\nSaved songs: ")
        for ind in song_list.keys():
            print (ind)
        print()
        song_name = input('Enter song to play: ')
        print()
        play_song.name_identifier(song_name)

    #if user selects option3, they are told to input a song to delete
    elif choice == '3':
        print("\nSaved songs: ")
        for ind in song_list.keys():
            print (ind)
        print()
        song_name = input('Enter song to delete: ')
        remove_song.song_delete(song_name)
        url_assignment.save_song()

        """ Test #2: makes sure the correct song is deleted """
        assert song_name not in song_list

    #if user selects option 4, the program shuts down
    elif choice == '4':
        break
    else:
        print("Invalid selection")
        print()
