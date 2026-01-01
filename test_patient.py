from patient import check_test_result, patient_details


def test_abnormal_value():
    result = check_test_result(130)
    assert result == "ABNORMAL"


def test_normal_value():
    result = check_test_result(90)
    assert result == "Normal"


def test_default_test_result():
    result = check_test_result()
    assert result == "Normal"


def test_patient_details_with_custom_values(capsys):
    patient_details(
        name="Sameer",
        age=21,
        disease="Fever",
        room_no="12A",
        tests=[95, 120, 85]
    )

    captured = capsys.readouterr()
    output = captured.out

    assert "Sameer" in output
    assert "Fever" in output
    assert "ABNORMAL" in output


def test_patient_details_with_default_values(capsys):
    patient_details()

    captured = capsys.readouterr()
    output = captured.out

    assert "Unknown" in output
    assert "Not Specified" in output
    assert "Normal" in output
