import os
import hashlib



def generator(file):
    with open(file, "r") as f:
        for line in f:
            line = f.readline()
            yield hashlib.md5(line.encode('utf-8')).hexdigest()
    f.close()


if __name__ == "__main__":

    filepath = os.path.join(os.getcwd(), "countriesWikipath.txt")
    for md5_hash in generator(filepath):
        print(md5_hash)
