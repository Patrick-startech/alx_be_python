def safe_divide(numerator, denominator):
    """
    Safely divide two values, handling non-numeric input and division by zero.
    Returns a string message with the result or error.
    """
    try:
        num = float(numerator)
        denom = float(denominator)

        if denom == 0:
            return "Error: Cannot divide by zero."

        result = num / denom
        return f"The result of the division is {result}"

    except ValueError:
        return "Error: Please enter numeric values only."
 