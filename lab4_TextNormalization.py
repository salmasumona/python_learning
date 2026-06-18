raw_survey_inputs = ["  ALICE SMITH ", " dhaka, BANGLADESH  ", "  mLOpS_ENGineer  ", "  LIAM,MAYA "]
sanitized_records = []

# TODO: Write a loop to clean each string element and save it to sanitized_records

for item in raw_survey_inputs:
    sanitized_records.append(item.strip().lower())

print(f"Raw Input: {raw_survey_inputs}")
print(f"Sanitized Production Input: {sanitized_records}")