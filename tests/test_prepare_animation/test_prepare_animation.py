import os
import json
from oracle_problem_2.animation import Animation


def _load_data() -> (dict, dict):
    """
    Loads input data and expected output data from JSON files as dict

    :return: tuple of input dataset , expected output dataset
    """
    print('{0}'.format(__file__))
    input_data_path = os.path.join(os.getcwd(), 'tests/test_prepare_animation/input_data/input_data.json')
    expected_op_path = os.path.join(os.getcwd(), 'tests/test_prepare_animation/expected_output/output_data.json')

    # Input data
    with open(input_data_path) as f:
        inp_ds = json.load(f)
        # print(inp_ds)
    # Expected output
    with open(expected_op_path) as f2:
        exp_ds = json.load(f2)
        # print(exp_ds)

    return inp_ds, exp_ds


def test_prepare_animation():
    d1, d2 = _load_data()
    initial_state, speed = d1["1"]["initialState"], d1["1"]["speed"]

    anim = Animation(initial_state, speed)
    anim.prepare_animation()
    for k, v in anim.state_dict.items():
        expected_op_step_k = d2[str(k)]
        actual_op_returned_string = ''.join(v)
        # print(f'{expected_op_step_k} , {actual_op_returned_string}')
        assert actual_op_returned_string == expected_op_step_k
