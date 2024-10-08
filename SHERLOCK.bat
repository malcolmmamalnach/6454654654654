@echo off
setlocal enabledelayedexpansion

:: Enable ANSI colors in Windows
for /f "tokens=2 delims==" %%a in ('"prompt $E"') do set "ESC=%%a"

:: Define color codes
set "COLOR_GREEN=%ESC%[32m"
set "COLOR_RED=%ESC%[31m"
set "COLOR_RESET=%ESC%[0m"

:: ASCII Art Logo and Tool Information
echo.
echo   _________   ____ ___.___________________   
echo  /   _____/  |    |   \   \______   \     \  
echo  \_____  \   |    |   /   ||     ___/  |   \ 
echo  /        \  |    |  /|   ||    |   |  |___\ 
echo /_______  /  |______/ |___||____|   |_____  /
echo         \/                               \/ 
echo.
echo OSINT Username Checker
echo Author: GORLAMI
echo Description: Checks for the presence of a username across multiple popular social media platforms.
echo ----------------------------------------------------------
echo.

:: Input username
set /p "username=Enter the username to search for: "

:: Social media URLs with placeholders
set platforms=Facebook,https://www.facebook.com/{},Twitter,https://www.twitter.com/{},Instagram,https://www.instagram.com/{},TikTok,https://www.tiktok.com/@{},LinkedIn,https://www.linkedin.com/in/{},Pinterest,https://www.pinterest.com/{},GitHub,https://www.github.com/{},Reddit,https://www.reddit.com/user/{},YouTube,https://www.youtube.com/{},Flickr,https://www.flickr.com/people/{}

:: Loop through each platform and check the username
echo.
echo Results:
for %%A in (%platforms%) do (
    set /a count+=1
    if !count! lss 2 (
        set "platform=%%A"
    ) else (
        set "url=%%A"
        set "url=!url:{=%username%!"
        set "count=0"
        
        :: Make request and check response
        curl -s -o nul -w "%%{http_code}" "!url!" > temp.txt
        set /p "status_code="<temp.txt
        del temp.txt

        if !status_code! == 200 (
            echo !COLOR_GREEN!!platform!: Username found at !url!!COLOR_RESET!
        ) else if !status_code! == 404 (
            echo !COLOR_RED!!platform!: Username not found!COLOR_RESET!
        ) else (
            echo !platform!: Error - HTTP status code !status_code!
        )
    )
)
