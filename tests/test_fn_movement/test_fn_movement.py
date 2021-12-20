import os
import json
from oracle_problem_2.animation import Animation


def _load_data() -> (dict, dict):
    print('{0}'.format(__file__))
    input_data_path = os.path.join(os.getcwd(), 'tests/test_fn_movement/input_data/input_data.json')
    expected_op_path = os.path.join(os.getcwd(), 'tests/test_fn_movement/expected_output/output_data.json')

    # Input data
    with open(input_data_path) as f:
        inp_ds = json.load(f)
        # print(inp_ds)
    # Expected output
    with open(expected_op_path) as f2:
        exp_ds = json.load(f2)
        # print(exp_ds)

    return inp_ds, exp_ds


def test_fn_movement():
    d1, d2 = _load_data()
    list_of_keys = d1.keys()

    for k in list_of_keys:
        prev_state = list(d1[k]['initialState']).copy()
        initial_state, speed = d1[k]['initialState'], d1[k]['speed']

        # create an Animation instance with every set of initial_state, speed
        anim = Animation(initial_state, speed)
        returned_string = anim.fn_movement(prev_state, 1)
        # print(f'returned_string = {returned_string}')
        # print(f"d2[k] = {d2[k]}")
        assert d2[k] == returned_string
