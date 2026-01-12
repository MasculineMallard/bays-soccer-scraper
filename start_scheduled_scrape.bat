@echo off
echo Starting scheduled BAYS scraper...
echo.
echo This window will show progress. You can minimize it but do not close it.
echo.
python src\scheduled_scrape.py --wait 75 --year 2024 --season Fall
echo.
echo Scraping complete! Press any key to close this window.
pause
