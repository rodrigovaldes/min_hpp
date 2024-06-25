import datetime as dt

def print_message():
    with open('register_file.txt', 'a') as f:
        f.write('Hello WOOOOOOrld! {} \n'.format(dt.datetime.now()))
    print("Hello WOOOOrld! {}".format(dt.datetime.now()))