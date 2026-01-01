from patient import check_test_result


def test_abnormal_value():
    assert check_test_result(130) == "ABNORMAL"


def test_normal_value():
    assert check_test_result(90) == "Normal"


def test_lower_bound_abnormal():
    assert check_test_result(60) == "ABNORMAL"


def test_upper_bound_abnormal():
    assert check_test_result(120) == "ABNORMAL"


def test_default_value():
    assert check_test_result() == "Normal"
