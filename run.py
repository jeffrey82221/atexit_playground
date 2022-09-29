import atexit


def exit_func():
    print('This program terminated')


atexit.register(exit_func)

if __name__ == '__main__':
    print('Something in the program')
