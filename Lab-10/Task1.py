"""
def calc_average(marks):
    total = 0
    for calc_average(marks):
    total = 0
    for m in marks:
        total +=m
    average=total/len(marks)
    return average
marks = [85,90,78,92]
print("Average score is",calc_average)    
"""        
def calc_average(marks: list[int]) -> float:
    """
    Calculate the average of a list of integer marks.

    Args:
        marks (list[int]): A list of integer marks.

    Returns:
        float: The average score.

    Example:
        >>> calc_average([85, 90, 78, 92])
        86.25
    """
    total = 0
    for m in marks:
        total += m
    average = total / len(marks)
    return average

marks = [85, 90, 78, 92]
print("Average score is", calc_average(marks))
