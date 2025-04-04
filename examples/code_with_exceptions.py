import diskoize
from typing import Optional


@diskoize.diskoize("foo")
def compute1(x: Optional[int] = 0) -> int:
    """
    Compute a value based on the input parameter.
    
    Args:
        x (int, optional): Input value to be added to the base. Defaults to 0.
        
    Returns:
        int: 744 plus the input value
        
    Raises:
        ValueError: If x equals 6
    """
    if x == 6:
        raise ValueError("x cannot be 6")
    return 744 + x
