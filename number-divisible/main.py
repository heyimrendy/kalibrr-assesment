import os
import pprint

absolute_path = os.path.dirname(__file__)
pp = pprint.PrettyPrinter(indent=2)


def check_divisible_number(start: int, stop: int, target: int):
    count = 0
    for i in range(start, stop + 1):
        if i % target == 0:
            count += 1

    return count


def handle_test_result(
    txt_expected_out: list[str],
    curr_test_out: int,
    debug_res_test: dict[str, list],
    n_curr_test: int,
    n_curr_txt_line: int,
):
    expected_answer = int(txt_expected_out[n_curr_test - 1])
    if curr_test_out == expected_answer:
        debug_res_test["passed"].append(n_curr_test)
    else:
        debug_res_test["failed"].append(
            {
                "txt_line_number": n_curr_txt_line,
                "test_number": n_curr_test,
                "expected_answer": expected_answer,
                "output_answer": curr_test_out,
            }
        )


def run(input_fname="", input_test_res_fname="", has_test_sample_out=False):
    with open(os.path.join(absolute_path, f".\\input\\{input_fname}")) as f:
        txt_input = f.read().splitlines()

    if has_test_sample_out:
        test_result = {"passed": [], "failed": []}
        with open(
            os.path.join(absolute_path, f".\\input\\{input_test_res_fname}")
        ) as f:
            txt_test_res_out = f.read().splitlines()

    len_txt_input = len(txt_input)
    len_test = txt_input[0]
    n_curr_test = 1
    n_curr_txt_line = 1

    # Erase previous output file
    open(os.path.join(absolute_path, ".\\input\\result.out"), "w").close()

    while n_curr_txt_line < len_txt_input:
        n_start = int(txt_input[n_curr_txt_line])
        n_stop = int(txt_input[n_curr_txt_line + 1])
        n_target = int(txt_input[n_curr_txt_line + 2])

        res_out = check_divisible_number(n_start, n_stop, n_target)
        if has_test_sample_out:
            handle_test_result(
                txt_test_res_out, res_out, test_result, n_curr_test, n_curr_txt_line
            )
        with open(os.path.join(absolute_path, ".\\input\\result.out"), "a") as myfile:
            myfile.write(f"Case {n_curr_test}: {res_out}\n")

        n_curr_txt_line += 3
        n_curr_test += 1

    if has_test_sample_out:
        print(f"Total test passed: {len(test_result['passed'])}/{len_test}")
        print(f"Total test failed: {len(test_result['failed'])}/{len_test}")
        if len(test_result["failed"]) > 0:
            pp.pprint(test_result["failed"])

    print(txt_input)


if __name__ == "__main__":
    # Don't forget to set has_test_sample_out to False when running real input
    run(
        input_fname="sample1.in",
        input_test_res_fname="test_sample1.out",
        has_test_sample_out=True,
    )
