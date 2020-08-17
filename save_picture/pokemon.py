#!/use/bin/env python3
import requests
import wget

 # ============================
 # API: https://pokeapi.co/
 # ============================

# PART1: function that pulls API of a user-selected pokemon
def api_pull():
    choice= input("What Pokemon would you like a picture of? ")
    # code goes here!
    url = "https://pokeapi.co/api/v2/pokemon/" + choice
    return url

 # PART2: takes URL from part1 and convert from JSON to Python
def json_conv(poke_api):
    if poke_api is not None:
        return requests.get(poke_api).json() 
    return None

 # PART3: function that slices through PokiAPI dictionary and returns image URL  
def api_slice(json2python):
    poke_pic= json2python["sprites"]["front_default"]
    return poke_pic

 # PART4: function that uses wget module to dl an image from a link
def wget_pic(imagelink):
    file_path  = '/home/student/mycode/save_picture'
    poke_img = wget.download(imagelink, out=file_path)

 # FINAL: script to call all parts
def main():
    wget_pic(api_slice(json_conv(api_pull())))

main()

