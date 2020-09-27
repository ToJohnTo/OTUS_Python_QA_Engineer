*** Settings ***
Library    SeleniumLibrary
Library    DatabaseLibrary


*** Variables ***
${LOCATOR_USERNAME}                 id:input-username
${LOCATOR_PASSWORD}                 id:input-password
${LOCATOR_SUBMIT_BUTTON}            css:.btn.btn-primary
${LOCATOR_LOGOUT_BUTTON}            css:.fa.fa-sign-out

${LOCATOR_MENU_CATALOG}             css:#menu-catalog
${LOCATOR_CATALOG_ITEMS}            css:#collapse1 > li > a
${LOCATOR_INPUT_FILTER_NAME}        css:#input-name
${LOCATOR_EDIT_BUTTON}              css:.fa.fa-pencil

${LOCATOR_ADD_NEW_PRODUCT}          xpath=//a[@data-original-title='Add New']
${LOCATOR_SAVE_NEW_PRODUCT}         xpath=//button[@data-original-title='Save']
${LOCATOR_DELETE_PRODUCT}           xpath=//button[@data-original-title='Delete']
${LOCATOR_PRODUCT_NAME_INPUT}       css=#input-name1
${LOCATOR_PRODUCT_META_INPUT}       css=#input-meta-title1
${LOCATOR_DATA_PRODUCT_TAB}         Data
${LOCATOR_PRODUCT_MODEL_INPUT}      css=#input-model
${LOCATOR_FILTER_SUBMIT_BUTTON}     css=#button-filter
${PRODUCT_DB}                       oc_product
${PRODUCT_DESCRIPTION_DB}           oc_product_description


*** Keywords ***
Login
    [Arguments]   ${username}   ${password}
    Set username  ${username}
    Set password  ${password}
    Wait until keyword succeeds   3sec   1sec   Click Element    ${LOCATOR_SUBMIT_BUTTON}


Set username
    [Arguments]  ${name}
    Clear Element Text  ${LOCATOR_USERNAME}
    Input Text          ${LOCATOR_USERNAME}     ${name}


Set password
    [Arguments]  ${password}
    Input Password      ${LOCATOR_PASSWORD}     ${password}


Verify Page Title Contains
    [Arguments]    ${value}
    ${title}    Get Title
    Should Contain      ${title}    ${value}


Logout
    Wait until keyword succeeds   3sec   1sec   Click Element    ${LOCATOR_LOGOUT_BUTTON}


Open Catalog Products
    Click Element  ${LOCATOR_MENU_CATALOG}
    ${LOCATOR_CATALOG_ITEMS} =  Get Webelements  ${LOCATOR_CATALOG_ITEMS}
    Wait Until Keyword Succeeds  3 sec  1 sec  Click Element  ${LOCATOR_CATALOG_ITEMS}[1]
    Wait Until Page Contains Element  xpath=//h1[text()='Products']


Add Product To Catalog
    [Arguments]  ${product_name}  ${product_meta}  ${product_model}
    Open Catalog Products
    Click Element  ${LOCATOR_ADD_NEW_PRODUCT}
    Input Text  ${LOCATOR_PRODUCT_NAME_INPUT}   ${product_name}
    Input Text  ${LOCATOR_PRODUCT_META_INPUT}   ${product_meta}
    Click Link  ${LOCATOR_DATA_PRODUCT_TAB}
    Input Text  ${LOCATOR_PRODUCT_MODEL_INPUT}  ${product_model}
    Click Element  ${LOCATOR_SAVE_NEW_PRODUCT}


Change Product Name In Catalog
    [Arguments]  ${old_product_name}    ${new_product_name}
    Open Catalog Products
    Input Text    ${LOCATOR_INPUT_FILTER_NAME}  ${old_product_name}
    Click Button  ${LOCATOR_FILTER_SUBMIT_BUTTON}
    Select First Product In Products
    Click Element  ${LOCATOR_EDIT_BUTTON}
    Input Text  ${LOCATOR_PRODUCT_NAME_INPUT}   ${new_product_name}
    Click Element  ${LOCATOR_SAVE_NEW_PRODUCT}


Select First Product In Products
    Click Element  css=tbody td:first-child input


Check Product In Database
    [Arguments]  ${value}
    Check If Exists In Database  select model from ${PRODUCT_DB} where model = '${value}'
    Check If Exists In Database  select name from ${PRODUCT_DESCRIPTION_DB} where name = '${value}'


Check Product Name In Database
    [Arguments]  ${value}
    Check If Exists In Database  select name from ${PRODUCT_DESCRIPTION_DB} where name = '${value}'
