#DATE - 4/2/2025

# City Name

def city_country(city_name, country_name):
    city_info = f"\n ------------------------------------------------ \n {city_name}, {country_name} \n -----------------------------------------------"
    return city_info.title()

info = city_country(city_name= "new york", country_name="usa")
print(info)
info = city_country(city_name="Tokyo", country_name="japan")
print(info)
info = city_country(city_name="california", country_name="usa")
print(info)
info = city_country(city_name="paris", country_name="france")
print(info)


# make album

def make_album(artist_name, album):
    artist_info = {"artist":artist_name, "album_name":album}
    return artist_info

inffo = make_album(artist_name="willie", album="vanbros")
print(inffo)

inffo = make_album(artist_name="tony stark", album="iron-man")
print(inffo)

inffo = make_album(artist_name="bruce van", album="bat-man")
print(inffo)

inffo = make_album(artist_name="dr steve", album="magic music")
print(inffo)


# update make_album

def make_album(artist_name, album, song_num = None):
    artist_info = {"artist":artist_name, "album_name":album}

    artist_info["numberof_songs"] = song_num

    return artist_info


inffo = make_album(artist_name="willie", album="vanbros")
print(inffo)

inffo = make_album(artist_name="tony stark", album="iron-man", song_num = 2)
print(inffo)

inffo = make_album(artist_name="bruce van", album="bat-man")
print(inffo)

inffo = make_album(artist_name="dr steve", album="magic music", song_num= 100)
print(inffo)


# User Album

def user_album(artist_name, album):
    album_info = f"\n ------------------------------\n {artist_name} => {album} \n ------------------------------"
    return album_info.title()

while True:
    artist = input("\n Enter your fav artist:- ")
    if artist == "end":
        break
    artist_album = input("\n Enter your fav album of that artist:- ")
    if artist_album == "end":
        break

    display_user_album_info = user_album(artist_name=artist, album=artist_album)
    print(display_user_album_info)


