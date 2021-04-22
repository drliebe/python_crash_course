def make_album(artist_name, album_title, number_tracks=''):
    album_info = {}
    if number_tracks:
        album_info['number_tracks'] = number_tracks
    album_info['artist_name'] = artist_name
    album_info['album_title'] = album_title
    return album_info

while True:
    print("Enter 'q' to quit at any time.")
    
    artist_entered = input('Enter artist name: ')
    if artist_entered == 'q':
        break
    
    album_entered = input('Enter album name: ')
    if album_entered == 'q':
        break

    album = make_album(artist_entered,Mil album_entered)
    print(album)
