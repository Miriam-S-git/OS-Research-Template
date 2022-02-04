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
    population=patients.registered_with_one_practice_between(
        "2019-03-01", "2020-03-01"
    ),
)
from codelists import *
