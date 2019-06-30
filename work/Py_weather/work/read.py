
# https://stackoverflow.com/questions/8009882/how-to-read-a-large-file-line-by-line-in-python/801013
# https://thispointer.com/5-different-ways-to-read-a-file-line-by-line-in-python/

# https://stackoverflow.com/questions/23459095/check-for-file-existence-in-python-3

array = []

with open("city.dat", "r") as ins:
    for line in ins:
        array.append(line)
print( array )
