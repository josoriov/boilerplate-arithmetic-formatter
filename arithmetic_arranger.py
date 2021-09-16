# constants
EXTRA_PADDING: int = 2
SPACE_PADDING: int = 3


def problem_arranger(problem: str, calculate: bool = True) -> tuple[str, str, str, str]:
    num, op, den = problem.split(" ")
    result = ""
    if calculate:
        if op == "+":
            result = str(int(num) + int(den))
        elif op == "-":
            result = str(int(num) + int(den))
    return num, op, den, result


def arithmetic_arranger(problems: list[str], calculate: bool = True) -> str:
    for problem in problems:
        pass
    arranged_problems = None
    return ""

