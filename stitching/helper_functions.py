from typing import Union, List

def create_list_if_none(value: Union[List, None]) -> List:
    """Create a list if the value is None."""
    return value if value is not None else []