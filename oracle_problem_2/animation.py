
class Animation(object):

    def __init__(self, initial_state: str, speed: int) -> None:
        """
        Function to create an instance of Animation

        :param initial_state: initial_state in string format
        :param speed: speed in number format
        """
        self.initial_state = initial_state
        self.speed = speed
        self.state_dict = dict()
        self.len_initial_state = len(initial_state)

    def prepare_animation(self) -> None:
        """
        Function to prepare self.state_dict. Break from loop when all chars of string are with '.' only.

        :return: None
        """
        final_string = ''.join(['.'] * self.len_initial_state)
        self.state_dict[0] = list(self.initial_state).copy()

        last_state = self.state_dict[0]
        i = 1
        returned_string = ''

        while returned_string != final_string:
            returned_string = self.fn_movement(last_state, i)
            last_state = self.state_dict[i]
            i += 1

    def fn_movement(self, prev_state: list, state_i: int) -> str:
        """
        Function to take in an last state, calculate current state after movement and add in state dict.
        Finally return output state in string format for comparison

        :param prev_state: list of chars created after last movement
        :param state_i: movement iteration number
        :return:
        """
        len_arr = self.len_initial_state
        speed = self.speed
        tmp = ['.' for _ in range(len_arr)]
        for x in range(len_arr):
            if (prev_state[x] == 'R' or prev_state[x] == 'O') and 0 <= (x + speed) <= len_arr-1:
                if 'Y' in tmp[x + speed]:
                    tmp[x + speed] = 'O'
                else:
                    tmp[x + speed] = 'R'
            if (prev_state[x] == 'Y' or prev_state[x] == 'O') and 0 <= (x - speed) <= len_arr-1:
                if 'R' in tmp[x - speed]:
                    tmp[x - speed] = 'O'
                else:
                    tmp[x - speed] = 'Y'
        self.state_dict[state_i] = tmp.copy()
        return ''.join(self.state_dict[state_i])

    def print_animation(self) -> None:
        """
        Function to print animation from self.state_dict

        :return: None
        """
        for k, v in self.state_dict.items():
            print(''.join(self.state_dict[k]))
