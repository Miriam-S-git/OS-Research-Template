from cohortextractor import (codelist, codelist_from_csv, combine_codelists)

# Diabetes
diabetes_t1_codes = codelist_from_csv(
    "codelists/opensafely-type-1-diabetes.csv", system="ctv3", column="CTV3ID"
)

diabetes_t2_codes = codelist_from_csv(
    "codelists/opensafely-type-2-diabetes.csv", system="ctv3", column="CTV3ID"
)

diabetes_unknown_codes = codelist_from_csv(
    "codelists/opensafely-diabetes-unknown-type.csv", system="ctv3", column="CTV3ID"
)

# Ethnicity
ethnicity_codes = codelist_from_csv(
        "codelists/opensafely-ethnicity.csv",
        system="ctv3",
        column="Code",
        category_column="Grouping_6",
)

# HbA1c
hba1c_new_codes = codelist_from_csv(
    "codelists/opensafely-glycated-haemoglobin-hba1c-tests-numerical-value.csv",
    system="snomed",
    column="term"
)

# Insulin medication
insulin_med_codes = codelist_from_csv(
    "codelists/opensafely-insulin-medication.csv", 
    system="snomed", 
    column="id"
)

# Antidiabetic drugs
oad_med_codes = codelist_from_csv(
    "codelists/opensafely-antidiabetic-drugs.csv",
    system="snomed",
    column="id"
)

# Learning disabilities
learning_disability_codes = codelist_from_csv(
    "codelists/opensafely-learning-disabilities.csv",
    system="ctv3",
    column="CTV3Code",
)

# Mental illness codes
psychosis_schizophrenia_bipolar_affective_disease_codes = codelist_from_csv(
    "codelists/opensafely-psychosis-schizophrenia-bipolar-affective-disease.csv",
    system="ctv3",
    column="CTV3Code",
)

depression_codes = codelist_from_csv(
    "codelists/opensafely-depression.csv",
    system="ctv3",
    column="CTV3Code",
)

dementia_codes = codelist_from_csv(
    "codelists/opensafely-dementia-complete.csv", 
    system="ctv3", 
    column="code"
)

# Atrial fibrillation

AF_codes = codelist_from_csv(
    "codelists/opensafely-atrial-fibrillation-clinical-finding.csv",
    system="ctv3",
    column="CTV3Code"
)

# Heart Disease excluding VSD and AF

chronic_cardiac_codes = codelist_from_csv(
    "codelists/opensafely-chronic-cardiac-disease.csv",
    system= "ctv3",
    column= "CTV3ID"
)

hypertension_codes = codelist_from_csv(
    "codelists/opensafely-hypertension.csv", 
    system="ctv3", 
    column= "CTV3ID"

)

# peripheral arterial disease (PAD)
periph_art_disease_codes = codelist_from_csv(
    "codelists/opensafely-peripheral-arterial-disease.csv",
    system="ctv3",
    column="code"
)

# Combine stroke and TIA codes
stroke_codes= codelist_from_csv(
    "codelists/opensafely-stroke-updated.csv",
    system="ctv3", 
    column="CTV3ID"
)

TIA_codes= codelist_from_csv(
    "codelists/opensafely-transient-ischaemic-attack.csv",
    system="ctv3",
    column="code"
)


stroke_and_TIA_codes = combine_codelists(
    stroke_codes, 
    TIA_codes
)