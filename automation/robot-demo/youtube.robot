*** Settings ***
Documentation   A test to demo testing YouTube
Library         Selenium2Library
Test Setup      Open Browser  https://www.youtube.com  ${BROWSER}
Test teardown   Close Browser

*** Variables ***
${BROWSER}  Chrome
${DELAY}    0



# Our Page Object Pattern 
# When the css/structure of page changes, we update the method to find here

${FIND_LOGO}           id=yt-masthead-logo-fragment 
${FIND_TRENDING_LINK}  link=Trending
${FIND_SEARCH_FIELD}   id=masthead-search-term
${FIND_SEARCH_BUTTON}  css=.search-button 


*** Test Cases ***

Homepage Loads
  Element Should Be Visible  ${FIND_LOGO}

Visit Trending Videos
  Click Element  ${FIND_TRENDING_LINK}
  ${url}=  Get Location
  Should Be Equal  ${url}  https://www.youtube.com/feed/trending

Search Loads Results
  Input Text  ${FIND_SEARCH_FIELD}  automation
  Click Button  ${FIND_SEARCH_BUTTON}
  Wait Until Page Contains  results
