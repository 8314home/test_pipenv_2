from animation import Animation
from argparse import ArgumentParser


def run():
    parser = ArgumentParser(description="Parser to collect and parse input arguments of script"
                                        "--initial_state takes in initial state in string format"
                                        "--speed speed of animation in integer format", add_help=True)
    parser.add_argument('--initial_state', help='initial_state: takes in initial state in string format', required=True)
    parser.add_argument('--speed', help='speed: takes in speed in int format', required=True)
    args = parser.parse_args()

    initial_state = args.initial_state
    speed_of_animation = args.speed

    if not type(initial_state) is str:
        raise ValueError('--initial_state expected argument of string type, received {0}'.format(type(initial_state)))
    if not type(speed_of_animation) is int:
        raise ValueError('--speed expected argument of int type, received {0}'.format(type(speed_of_animation)))

    anim = Animation(initial_state, speed_of_animation)
    anim.prepare_animation()
    anim.print_animation()


if __name__ == '__main__':
    print('\nstart of Program - {0}\n'.format(__file__))
    try:
        run()
    except Exception as e:
        print('\nException block of Program - {0}\n'.format(__file__))
        print(e)
    finally:
        print('\nend of Program - {0}\n'.format(__file__))



