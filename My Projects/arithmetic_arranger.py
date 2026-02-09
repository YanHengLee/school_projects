def arithmetic_arranger(problems, show_answer=False):
    """
    Arrange arithmetic problems vertically and side-by-side.

    Supports addition and subtraction with optional display of answers.

    Parameters:
        problems (list): A list of arithmetic problem strings.
        show_answer (bool): Whether to include the calculated answers.

    Returns:
        str: Formatted arithmetic problems or an error message.
    """

    # ------------------------------------------------
    # Error handling
    # ------------------------------------------------
    # Limit the number of problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Supported operators and their corresponding operations
    ops = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y
    }

    # ------------------------------------------------
    # Containers for each output line
    # ------------------------------------------------
    line1 = []    # First operands
    line2 = []    # Operators and second operands
    dashes = []   # Separator lines
    answers = []  # Computed results

    # Split each problem into components: operand1, operator, operand2
    problem = []
    for p in problems:
        problem.append(p.split())

    # ------------------------------------------------
    # Process each arithmetic problem
    # ------------------------------------------------
    for p in problem:

        # Validate operator
        if p[1] not in ops:
            return "Error: Operator must be '+' or '-'."

        # Validate numeric operands
        if not p[0].isnumeric() or not p[2].isnumeric():
            return "Error: Numbers must only contain digits."

        # Validate operand length
        if len(p[0]) > 4 or len(p[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # ------------------------------------------------
        # Determine spacing and alignment
        # ------------------------------------------------
        # Width is based on the longer operand plus operator and space
        width = max(len(p[0]), len(p[2])) + 2

        # First line (right-aligned first operand)
        line1.append(p[0].rjust(width))

        # Second line (operator + right-aligned second operand)
        line2.append(p[1] + p[2].rjust(width - 1))

        # Dash line
        dashes.append("-" * width)

        # Calculate answer
        result = ops[p[1]](int(p[0]), int(p[2]))
        answers.append(str(result).rjust(width))

    # ------------------------------------------------
    # Combine all problems into formatted strings
    # ------------------------------------------------
    line1_string = "    ".join(line1)
    line2_string = "    ".join(line2)
    dashes_string = "    ".join(dashes)
    answer_string = "    ".join(answers)

    final_output = [line1_string, line2_string, dashes_string]

    # Include answers only if requested
    if show_answer:
        final_output.append(answer_string)

    # Join lines with newline characters for vertical display
    return "\n".join(final_output)
