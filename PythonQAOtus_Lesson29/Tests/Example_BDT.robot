*** Settings ***
Library         SeleniumLibrary
Resource        ../Resources/resource-file.robot
Documentation   Это пример теста написанного с помощью Robot Framework


*** Variables ***
# C переменными уже можно работать через опцию -v
${BROWSER}    chrome
${WEB_PATH}   https://demo.opencart.com/
${WEB_ADMIN_PATH}   https://demo.opencart.com/admin


*** Test Cases ***
Check test element by id
    [Setup]     Open Browser    ${WEB_PATH}    ${BROWSER}
    Wait until keyword succeeds   3sec   1sec   Click Element	id:logo
    Wait until keyword succeeds   3sec   1sec   Click Element	id:search
    [Teardown]  Close Browser


Check test elements by css selector
    [Setup]     Open Browser    ${WEB_PATH}    ${BROWSER}
    Wait until keyword succeeds   3sec   1sec   Click Element	css:.btn-group.btn-block
    [Teardown]  Close Browser


Check test element by class name selector
    [Setup]     Open Browser    ${WEB_PATH}    ${BROWSER}
    Wait until keyword succeeds   3sec   1sec   Click Element	class:btn-group.btn-block
    [Teardown]  Close Browser


Check test login
    [Documentation]  Check login
    [Setup]     Open Browser    ${WEB_ADMIN_PATH}    ${BROWSER}
    Login    demo    demo
    Verify Page Title Contains   Dashboard
    [Teardown]  Close Browser


Check test unlogin
    [Documentation]  Check unlogin
    [Setup]     Open Browser    ${WEB_ADMIN_PATH}    ${BROWSER}
    Login    demo    demo
    Logout
    Verify Page Title Contains   Administration
    [Teardown]  Close Browser
