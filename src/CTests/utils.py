'''
This file contains the functions that are used to compile, run, and test the code.
'''

import subprocess
compiled_program = 'test'
from src.settings import C_ENTRYPOINT

# compile the code
def compile_code(file_path,exec_file=compiled_program):
    try:
        subprocess.run(['gcc','-e',C_ENTRYPOINT, file_path, '-o', exec_file], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(e.output)
        return False


def run_test(input_data='', exec_file=compiled_program):
    try:
        result = subprocess.run([f'./{exec_file}',input_data], text=True, timeout=2, capture_output=True, check=True)
        print(result.stdout.strip())
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "Timeout"

def evaluate_test(user_output, expected_output):
    print(f"user_output: '{str(user_output).strip()}' expected_output: '{str(expected_output).strip()}'")
    return str(user_output).strip() == str(expected_output).strip()


def calculate_score(passed_tests, total_tests, question_score=100):
    if passed_tests < total_tests/2: return 0
    return (passed_tests / total_tests) * question_score

# for test
tests = [
    {
        'input': 'world',
        'output': 'Hello, world!'
    },
    {
        'input': '5',
        'output': 'Hello, 5!\n'
    },
    {
        'input': '5\n',
        'output': 'Hello, 5!\n'
    },
]

question = {
    'points':30
}
# this func compiles and run tests and calculate score
def totalScore(file_path,question, tests):
    c =    compile_code(file_path)
    if not c:
        print("> Compilation failed")
        return 0   
    print("> Compiled successfully")
    passed_tests = 0
    for test in tests:
        if evaluate_test(run_test(test['input']),test['output']):
            passed_tests += 1
    
    print(f"> Passed {passed_tests} out of {len(tests)} tests")
    total = calculate_score(passed_tests, len(tests), question['points'])
    print(f"> Total score: {total}")
    return total
    



totalScore('main.c',question,tests)

