import stringCalculatorFile
def test_correct_params_expect_OP_NUM_NUM():
    # Arrange
    cut = stringCalculatorFile.StringCalculator()
    inputVal = "+, 3, 4"
    expResult = ["OPERATOR", "NUMBER", "NUMBER"]
    # Act
    result = cut.parse(inputVal)
    # Assert
    assert result == expResult
