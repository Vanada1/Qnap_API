def is_not_empty(checking_string: str, variable_name: str) -> None:
    """
    Asserts strings for empty.
    :param checking_string: String to check.
    :param variable_name: Name of the variable being checked.
    """
    if not checking_string:
        raise ValueError(f"String {variable_name} was empty")
