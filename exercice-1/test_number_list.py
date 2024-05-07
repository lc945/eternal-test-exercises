def  test_convert_to_integer():
    from number_list import convert_to_integer
    # Test avec une liste vide
    assert convert_to_integer([]) == []

    # Test avec une liste contenant des entiers
    assert convert_to_integer(['1', '2', '3']) == [1, 2, 3]

    # Test avec une liste contenant des entiers et des chaînes de caractères
    assert convert_to_integer(['1', '2', '3', 'a', 'b', 'c']) == [1, 2, 3]

    # Test avec une liste contenant des chaînes de caractères non convertibles en entiers
    assert convert_to_integer(['1', '2', '3', 'a', 'b', 'c']) == [1, 2, 3]

    # Test avec une liste contenant des nombres flottants
    assert convert_to_integer(['1', '2.5', '3.7', '4']) == [1, 4]

    # Test avec une liste contenant des nombres flottants et des chaînes de caractères
    assert convert_to_integer(['1', '2.5', '3.7', 'a', 'b']) == [1]

    # Test avec une liste contenant des nombres négatifs
    assert convert_to_integer(['-1', '-2', '-3']) == [-1, -2, -3]

    # Test avec une liste contenant des nombres entiers et des nombres négatifs
    assert convert_to_integer(['-1', '2', '-3', '4']) == [-1, 2, -3, 4]
