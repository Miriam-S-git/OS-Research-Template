from cohortextractor import (
    StudyDefinition, 
    patients, 
    codelist, 
    codelist_from_csv,
)  # NOQA

from common_variables import (
    common_variables
)

study = StudyDefinition(
    index_date="2020-03-01",
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },
    
    ############################### Robin's code
    population=patients.satisfying(
        """
        registered AND
        (NOT died) AND
        (sex = "M" OR sex = "F") AND
        (age >= 18 AND age <= 110) AND
        (region != "")
        """,
        registered=patients.registered_as_of(
            "index_date",
            return_expectations={"incidence": 0.9},
        ),
        died=patients.died_from_any_cause(
            on_or_before=end_date,
            returning="binary_flag",
            return_expectations={"incidence": 0.1}
        )
    ),
    
    
    
    
   ##################################### 
   ##################################### MY old code - changed to just define a variable
    registered=patients.registered_with_one_practice_between(
        "2019-03-01", "2020-03-01"
    ),
    
    ##############################################
    ** common_variables
)
from codelists import *
