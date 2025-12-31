from patient import check_test_results

def test_patient_results():
    
    tests = [80, 120, 65]  # 80 normal, 120 high, 65 low

    result = check_test_results(tests)

    
    assert result == ["Normal", "ABNORMAL", "ABNORMAL"]