# test_line.py

def test_point_on_line():
    from line import point_on_line
    a = (1, 2)
    b = (3, 6)
    c = 2
    answer = point_on_line(a, b, c)
    assert answer == 4
