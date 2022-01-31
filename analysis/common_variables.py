from cohortextractor import patients
from codelists import *

common_variables = dict(
    # Index date for comparison
    index_date = "2019-03-01",
    
    # Sex
    sex = patients.sex(return_expectations={
        "rate": "universal",
        "category": {"ratios": {"M": 0.49, "F": 0.51}},
    }),
    
    # Age
    age_group = patients.categorised_as(
        {
            "0-15": "age >= 0 AND age < 16",
            "16-24": "age >= 16 AND age < 25",
            "25-34": "age >= 25 AND age < 35",
            "35-44": "age >= 35 AND age < 45",
            "45-54": "age >= 45 AND age < 55",
            "55-64": "age >= 55 AND age < 65",
            "65-74": "age >= 65 AND age < 75",
            "75+": "age >= 75",
            "missing": "DEFAULT",
        },
        return_expectations = {
            "rate": "universal",
            "category": {
                "ratios": {
                    "0-15": 0.2,
                    "16-24": 0.1,
                    "25-34": 0.1,
                    "35-44": 0.15,
                    "45-54": 0.1,
                    "55-64": 0.1,
                    "65-74": 0.1,
                    "75+": 0.13,
                    "missing": 0.02,
                }
            },
        },
        age = patients.age_as_of(
            "index_date",
        ),
    ),
                       
    # Region
    region = patients.registered_practice_as_of(
        "index_date",
        returning = "nuts1_region_name",
        return_expectations = {
            "category": {
                "ratios": {
                    "North East": 0.1,
                    "North West": 0.1,
                    "Yorkshire and the Humber": 0.1,
                    "East Midlands": 0.1,
                    "West Midlands": 0.1,
                    "East of England": 0.1,
                    "London": 0.2,
                    "South East": 0.2, 
                }
            },       
            "incidence": 0.8}
    ),
    
    # Index of multiple deprivation
    imd = patients.categorised_as(
        {
            "0": "DEFAULT",
            "1": """index_of_multiple_deprivation >=1 AND index_of_multiple_deprivation < 32844*1/5""",
            "2": """index_of_multiple_deprivation >= 32844*1/5 AND index_of_multiple_deprivation < 32844*2/5""",
            "3": """index_of_multiple_deprivation >= 32844*2/5 AND index_of_multiple_deprivation < 32844*3/5""",
            "4": """index_of_multiple_deprivation >= 32844*3/5 AND index_of_multiple_deprivation < 32844*4/5""",
            "5": """index_of_multiple_deprivation >= 32844*4/5 """,
        },
        index_of_multiple_deprivation = patients.address_as_of(
            "index_date",
            returning = "index_of_multiple_deprivation",
            round_to_nearest = 100,
        ),
        return_expectations = {
            "rate": "universal",
            "category": {
                "ratios": {
                    "0": 0.01,
                    "1": 0.20,
                    "2": 0.20,
                    "3": 0.20,
                    "4": 0.20,
                    "5": 0.19,
                }
            },
        },
    ),   
    # Dementia
    dementia=patients.with_these_clinical_events(
        dementia_codes,
        on_or_before="index_date",
        returning="binary_flag",
        return_expectations={"incidence": 0.02, },
    ),       
)
    


# ignore diabetes type for now
# For HbA1c level use codelist *opensafely/glycated-haemoglobin-hba1c-tests-numerical-value/5134e926  - this has included just IFCC measures. 


## Diabetes diagnosis:  https://github.com/opensafely/ethnicity-covid-research/issues/11  to identify Type 1 or Type 2 based on codes
# Type 1 diabetes:  opensafely/type-1-diabetes/2020-06-29
# Type 2 diabetes: opensafely/type-2-diabetes/2020-06-29
# Oral Antidiabetic drugs:  opensafely/antidiabetic-drugs/2020-07-16
# Insulin: opensafely/insulin-medication/2020-04-26
