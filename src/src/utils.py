'''
this file contains the functions that are used to compile, run and test the code
'''

import subprocess


def compile_code(file_path):
    try:
        subprocess.check_output(['gcc', file_path, '-o', 'compiled_program'])
        return True
    except subprocess.CalledProcessError as e:
        print(e.output)
        return False

def run_test(input_data):
    try:
        output = subprocess.check_output(['./compiled_program'], input=input_data.encode(), text=True, timeout=2)
        return output.strip()
    except subprocess.TimeoutExpired:
        return "Timeout"

def evaluate_test(user_output, expected_output):
    return user_output == expected_output

def calculate_score(passed_tests, total_tests):
    return (passed_tests / total_tests) * 100
