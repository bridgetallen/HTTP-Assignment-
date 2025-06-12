from app import power_of_two

def test_power_of_two():
    test_cases = [
        (0, 1),
        (1, 2),
        (2, 4),
        (3, 8),
        (4, 16),
        (5, 32),
        (6, 64),
        (7, 128),
        (8, 256),
        (9, 512),
        (10, 1024)
    ]
    for exp, expected in test_cases:
        result = power_of_two(exp)
        print(f"2^{exp} = {result}")
        assert result == expected




