###  Study definition for BMI

from cohortextractor import (
    StudyDefinition,
    codelist,
    codelist_from_csv,
    combine_codelists,
    filter_codes_by_category,
    patients,
)

################################
study = StudyDefinition(
    # define default dummy data behaviour
    default_expectations={
        "date": {"earliest": "1970-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.2,
    },

    # define the study index date
    index_date="2020-03-01",

    # define the study population
    population=patients.satisfying(
        """
        registered AND
        (sex = 'M' OR sex = 'F') AND  ##  Do i need to define sex somewhere?
        (age >= 23 AND age <= 110) AND
        (region != '')
        """,
        # Indicator for registration
        registered = patients.registered_with_one_practice_between(
    "2019-03-01", "2020-02-01"
    ),

    # define the study variables
    age=patients.age_as_of("index_date"),
        
    sex=patients.sex(
        return_expectations={
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
            "incidence": 1,
        }
    ),
    # more variables ...
)








