###  Study definition for BMI



#####################
# Import statements #
#####################

from cohortextractor import (
    StudyDefinition,
    patients,
    codelist_from_csv,
    codelist,
    filter_codes_by_category,
    combine_codelists,
    Measure,
)

from common_variables import (
    common_variables
)

from codelists import *
import pyarrow.feather as feather

######################
#  Study definition  #
######################

# Define start and end dates

study = StudyDefinition(
    
    # Set time period
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.2,
    },
    
    # Limiting to patients who had an HbA1c test 
    population=patients.satisfying(
        """
        registered_one AND
        (sex = 'M' OR sex = 'F') AND
        (age >= 23 AND age <= 110) AND
        (diabetes_type != 'UNKNOWN_DM') AND
        (region != '')
        """,
        # Indicator for registration
        registered_one=patients.registered_with_one_practice_between(
            start_date="2019-03-01",
            end_date="2020-03-01",
            return_expectations={"incidence": 0.90},
        ),            
    **common_variables
)

######################
#      Measures      #
######################



