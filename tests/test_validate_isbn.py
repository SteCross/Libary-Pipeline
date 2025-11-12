def test_validate_isbn():
    assert validation('978-0-123456-78-9') == True
    assert validation('invalid') == False
    assert validation('123') == False  # Too short
    assert validation('') == False
    #assert validate_isbn(None) == True  # ❌ BUG! Should be False

    #Has this worked?

    # Fix the test
    assert validation(None) == False  # ✅ Fixed
