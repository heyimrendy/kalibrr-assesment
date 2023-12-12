import os
import pprint

absolute_path = os.path.dirname(__file__)
pp = pprint.PrettyPrinter(indent=2)


def process_grid(grid: list[str], target: str, n_row: int, n_col: int):
    found = 0
    x = 1
    y = 1
    for i, _ in enumerate(grid):
        # Walk right direction
        new_x, new_y, ptr = x, y, (y * n_row) - (n_row - x) - 1
        curr_word = ""
        while True:
            if new_x > n_row:
                # print("FOUND BREAK: ", new_x, new_y)
                break
            curr_word += grid[ptr]
            # print(grid[ptr], " x:", new_x, " y:", new_y)
            if not target.startswith(curr_word):
                break
            if target == curr_word:
                # print("FOUND right direction: ", curr_word)
                found += 1
                break

            new_x, new_y = new_x + 1, new_y + 0
            ptr = (new_y * n_row) - (n_row - new_x) - 1

        # Walk bottom right direction
        new_x, new_y, ptr = x, y, (y * n_row) - (n_row - x) - 1
        curr_word = ""
        while True:
            if new_x > n_row or new_y > n_col:
                # print("FOUND BREAK: ", new_x, new_y)
                break
            curr_word += grid[ptr]
            if not target.startswith(curr_word):
                break
            if target == curr_word:
                # print("FOUND bottom right direction: ", curr_word)
                found += 1
                break
            # print(grid[ptr], " x:", new_x, " y:", new_y)
            new_x, new_y = new_x + 1, new_y + 1
            ptr = (new_y * n_row) - (n_row - new_x) - 1

        # Walk down direction
        new_x, new_y, ptr = x, y, (y * n_row) - (n_row - x) - 1
        curr_word = ""
        while True:
            if new_y > n_col:
                # print("FOUND BREAK: ", new_x, new_y)
                break
            curr_word += grid[ptr]
            if not target.startswith(curr_word):
                break
            if target == curr_word:
                # print("FOUND down direction: ", curr_word)
                found += 1
                break
            # print(grid[ptr], " x:", new_x, " y:", new_y)
            new_x, new_y = new_x + 0, new_y + 1
            ptr = (new_y * n_row) - (n_row - new_x) - 1

        # Walk bottom left direction
        new_x, new_y, ptr = x, y, (y * n_row) - (n_row - x) - 1
        curr_word = ""
        while True:
            if new_x < 1 or new_y > n_col:
                # print("FOUND BREAK: ", new_x, new_y)
                break
            curr_word += grid[ptr]
            if not target.startswith(curr_word):
                break
            if target == curr_word:
                # print("FOUND bottom left direction: ", curr_word)
                found += 1
                break
            # print(grid[ptr], " x:", new_x, " y:", new_y)
            new_x, new_y = new_x - 1, new_y + 1
            ptr = (new_y * n_row) - (n_row - new_x) - 1

        # Walk left direction
        new_x, new_y, ptr = x, y, (y * n_row) - (n_row - x) - 1
        curr_word = ""
        while True:
            if new_x < 1:
                # print("FOUND BREAK: ", new_x, new_y)
                break
            curr_word += grid[ptr]
            if not target.startswith(curr_word):
                break
            if target == curr_word:
                # print("FOUND left direction: ", curr_word)
                found += 1
                break
            # print(grid[ptr], " x:", new_x, " y:", new_y)
            new_x, new_y = new_x - 1, new_y + 0
            ptr = (new_y * n_row) - (n_row - new_x) - 1

        # Walk top left direction
        new_x, new_y, ptr = x, y, (y * n_row) - (n_row - x) - 1
        curr_word = ""
        while True:
            if new_x < 1 or new_y < 1:
                # print("FOUND BREAK: ", new_x, new_y)
                break
            curr_word += grid[ptr]
            if not target.startswith(curr_word):
                break
            if target == curr_word:
                # print("FOUND top left direction: ", curr_word)
                found += 1
                break
            # print(grid[ptr], " x:", new_x, " y:", new_y)
            new_x, new_y = new_x - 1, new_y - 1
            ptr = (new_y * n_row) - (n_row - new_x) - 1

        # Walk top direction
        new_x, new_y, ptr = x, y, (y * n_row) - (n_row - x) - 1
        curr_word = ""
        while True:
            if new_y < 1:
                # print("FOUND BREAK: ", new_x, new_y)
                break
            curr_word += grid[ptr]
            if not target.startswith(curr_word):
                break
            if target == curr_word:
                # print("FOUND top direction: ", curr_word)
                found += 1
                break
            # print(grid[ptr], " x:", new_x, " y:", new_y)
            new_x, new_y = new_x + 0, new_y - 1
            ptr = (new_y * n_row) - (n_row - new_x) - 1

        # Walk top right direction
        new_x, new_y, ptr = x, y, (y * n_row) - (n_row - x) - 1
        curr_word = ""
        while True:
            if new_x > n_row or new_y < 1:
                # print("FOUND BREAK: ", new_x, new_y)
                break
            curr_word += grid[ptr]
            if not target.startswith(curr_word):
                break
            if target == curr_word:
                # print("FOUND top right direction: ", curr_word)
                found += 1
                break
            # print(grid[ptr], " x:", new_x, " y:", new_y)
            new_x, new_y = new_x + 1, new_y - 1
            ptr = (new_y * n_row) - (n_row - new_x) - 1

        # Done with every direction
        if ((i + 1) % n_row) == 0:
            y += 1

        if x % n_row == 0:
            x = 1
        else:
            x += 1

    return found


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


def run(input_fname="", input_test_res_fname="", has_test_sample_out=False) -> None:
    with open(os.path.join(absolute_path, f".\\input\\{input_fname}")) as f:
        txt_input = f.read().splitlines()

    if has_test_sample_out:
        test_result: dict[str, list] = {"passed": [], "failed": []}
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
        n_row = int(txt_input[n_curr_txt_line + 1])
        n_col = int(txt_input[n_curr_txt_line])
        target_word = txt_input[n_curr_txt_line + n_col + 2]

        # Create grid from input
        grid: list[str] = []
        i_grid_start = n_curr_txt_line + 2
        i_grid_stop = i_grid_start + n_col
        for i in range(i_grid_start, i_grid_stop):
            grid.extend(list(txt_input[i]))

        res_out = process_grid(grid, target_word, n_row, n_col)
        if has_test_sample_out:
            handle_test_result(
                txt_test_res_out, res_out, test_result, n_curr_test, n_curr_txt_line
            )

        with open(os.path.join(absolute_path, ".\\input\\result.out"), "a") as myfile:
            myfile.write(f"Case {n_curr_test}: {res_out}\n")

        n_curr_txt_line = n_curr_txt_line + 3 + n_col
        n_curr_test += 1

    if has_test_sample_out:
        print(f"Total test passed: {len(test_result['passed'])}/{len_test}")
        print(f"Total test failed: {len(test_result['failed'])}/{len_test}")
        if len(test_result["failed"]) > 0:
            pp.pprint(test_result["failed"])

    # print(txt_input)


if __name__ == "__main__":
    # Don't forget to set has_test_sample_out to False when running real input
    run(
        input_fname="sample1.in",
        input_test_res_fname="test_sample1.out",
        has_test_sample_out=True,
    )
