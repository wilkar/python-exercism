def convert(number):
    raindrops = {3: "Pling", 5: "Plang", 7: "Plong"}
    sound: str = ""
    for key, value in raindrops.items():
        if number % key == 0:
            sound = f"{sound}{value}"
    if sound == "":
        sound = str(number)
    return sound
