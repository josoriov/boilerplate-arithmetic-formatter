# constants
EXTRA_PADDING: int = 2
SPACE_PADDING: int = 3


def problem_arranger(problem: str, calculate: bool = True) -> tuple[str, str, str]:
    num, op, den = problem.split(" ")
    res = ""
    if calculate:
        if op == "+":
            res = str(int(num) + int(den))
        elif op == "-":
            res = str(int(num) - int(den))
    length = max(len(num), len(den), len(res)) + 2
    num, den, res = num.rjust(length), den.rjust(length), res.rjust(length)
    den = op + den[1:]
    return num, den, res


def arithmetic_arranger(problems: list[str], calculate: bool = True) -> str:
    num_line, den_line, res_line, divider = ("", "", "", "")
    for problem in problems:
        num, den, res = problem_arranger(problem, calculate)
        num_line += num + (" " * SPACE_PADDING)
        den_line += den + (" " * SPACE_PADDING)
        res_line += res + (" " * SPACE_PADDING)
        divider += ("-" * len(num)) + (" " * SPACE_PADDING)
    num_line = num_line.rstrip() + "\n"
    den_line = den_line.rstrip() + "\n"
    res_line = res_line.rstrip() + "\n"
    divider = divider.rstrip() + "\n"

    final = num_line + den_line + divider
    if calculate:
        final += res_line
    return final
