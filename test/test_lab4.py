import pytest

def clean_survey_data(inputs):

    sanitized_records = []
    for item in inputs:
        sanitized_records.append(item.strip().lower())
    return sanitized_records

def test_clean_survey_data():
    raw_survey_inputs = [
        "  ALICE SMITH ", 
        " dhaka, BANGLADESH  ", 
        "  mLOpS_ENGineer  ", 
        "  LIAM,MAYA "
    ]
    
    expected_output = [
        "alice smith",
        "dhaka, bangladesh",
        "mlops_engineer",
        "liam,maya"
    ]
    
    actual_output = clean_survey_data(raw_survey_inputs)
    
    assert actual_output == expected_output
    assert len(actual_output) == 4
    assert actual_output[0] == "alice smith"
