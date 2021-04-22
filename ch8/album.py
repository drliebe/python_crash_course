def make_album(artist_name, album_title, number_tracks=''):
    album_info = {}
    if number_tracks:
        album_info['number_tracks'] = number_tracks
    album_info['artist_name'] = artist_name
    album_info['album_title'] = album_title
    return album_info

print(make_album('Jimi Hendrix', 'Purple Haze'))
print(make_album('Prince', 'Purple Rain'))
print(make_album('Metallica', 'Load', 14))
