def song_decoder(song):
    return ' '.join(song.replace('WUB', ' ').split())

# OR

def song_decoder(song):
    raw_decoded_song = song.replace('WUB', ' ')
    raw_decoded_song_splitted = raw_decoded_song.split()
    decoded_song = ' '.join(raw_decoded_song_splitted)

    return decoded_song
