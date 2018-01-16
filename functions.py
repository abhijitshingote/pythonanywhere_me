magicians=['rad','abhi','shri','ani']

def make_great(arg_list):
    leng=len(arg_list)
    i=0
    while i<leng:
        arg_list[i]='Great ' + arg_list[i]
        i=i+1

    return arg_list

def show_magicians(arg_list):
    for item in arg_list:
        print('Magician: {}'.format(item))

new_magicians=make_great(magicians[:])

show_magicians(magicians)
show_magicians(new_magicians)