from patient import check_test_result

def test_abnormal_value():
    result = check_test_result(130)
    assert result == "ABNORMAL"

def test_normal_value():
    result = check_test_result(90)
    assert result == "Normal"
