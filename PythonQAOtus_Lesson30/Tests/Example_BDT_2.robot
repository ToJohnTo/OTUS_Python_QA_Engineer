*** Settings ***
Library         SeleniumLibrary
Library         DatabaseLibrary
Resource        ../Resources/resource-file.robot
Documentation   Это пример теста написанного с помощью Robot Framework #2


*** Variables ***
${BROWSER}              chrome
${WEB_PATH}             https://localhost:/
${WEB_ADMIN_PATH}       https://localhost/admin
${LOGIN}                user
${PASSWORD}             bitnami1
${TEST_PRODUCT_NAME}    TestProduct
${NEW_PRODUCT_NAME}     TestProductNEW
${DBName}               bitnami_opencart
${DBUser}               root
${DBPass}
${DBHost}               127.0.0.1
${DBPort}               3306
${BASE_URL}             localhost


*** Test Cases ***
Edit New Product In Catalog With Db Validation
    [Documentation]  Edit product in catalog with ui and validate precence in database
    [Tags]  DB  AddProduct
    [Setup]     Setup configure test for edit product
    Login    ${LOGIN}     ${PASSWORD}
    Verify Page Title Contains   Dashboard
    Add Product To Catalog  ${TEST_PRODUCT_NAME}  TestMeta  ${TEST_PRODUCT_NAME}
    Wait Until Keyword Succeeds  3 sec  1 sec  Check Product In Database  ${TEST_PRODUCT_NAME}
    Change Product Name In Catalog  old_product_name=${TEST_PRODUCT_NAME}  new_product_name=${NEW_PRODUCT_NAME}
    Wait Until Keyword Succeeds  3 sec  1 sec  Check Product Name In Database  ${NEW_PRODUCT_NAME}
    [Teardown]  Release configure test for edit product


Check test login
    [Documentation]  Check login
    [Setup]     Open Browser    ${WEB_ADMIN_PATH}    ${BROWSER}   options=add_argument("--ignore-certificate-errors")
    Login    ${LOGIN}     ${PASSWORD}
    Verify Page Title Contains   Dashboard
    [Teardown]  Close Browser


Check test unlogin
    [Documentation]  Check unlogin
    [Setup]     Open Browser    ${WEB_ADMIN_PATH}    ${BROWSER}   options=add_argument("--ignore-certificate-errors")
    Login    ${LOGIN}     ${PASSWORD}
    Logout
    Verify Page Title Contains   Administration
    [Teardown]  Close Browser


*** Keywords ***
Setup configure test for edit product
    Connect To Database  pymysql  ${DBName}  ${DBUser}  ${DBPass}  ${DBHost}  ${DBPort}
    Open Browser  ${WEB_ADMIN_PATH}  browser=${BROWSER}  options=add_argument("--ignore-certificate-errors")


Release configure test for edit product
    Execute Sql String  delete from ${PRODUCT_DB} where model = '${TEST_PRODUCT_NAME}'
    Execute Sql String  delete from ${PRODUCT_DESCRIPTION_DB} where name = '${TEST_PRODUCT_NAME}'
    Close Browser
    Disconnect From Database
