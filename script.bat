::**********Start of script**********

:: set the tname of the project
set projectName=Test1
set results=D:\crawls\%projectName%
:: %results%
:: do not add trailing slash

:: check if folder exist, if not create it
if not exist %results% mkdir %results%


set sfclidir=C:\Program Files (x86)\Screaming Frog SEO Spider\
:: %sfclidir%
:: include trailing slash

set configFile=D:\crawls\SEOSpiderConfig.seospiderconfig
:: %configFile%
:: ought to have .seospiderconfig file extension

set domain=https://kool-outfit.netlify.app/
:: %domain%

::create date & time stamped directory
set dateString=%DATE:/=-%
set timeString=%TIME:~0,2%-%TIME:~3,2%-%TIME:~6,2%
set ToDaysDate=%dateString%-%timeString: =-%
::%ToDaysDate%

set newFilePath="%projectName%-%ToDaysDate%"
chdir /d %results%
mkdir %newFilePath%
chdir /d %newFilePath%
set outputDir=%cd%
::%outputDir%

chdir /d "%sfclidir%"
ScreamingFrogSEOSpiderCli.exe --config "%configFile%" --crawl "%domain%"  --save-crawl --headless --output-folder "%outputDir%" --export-format "csv" --export-tabs "Internal:All,Response Codes:All"
ECHO %outputDir%
chdir /d %outputDir%
REN *.csv *.
REN *. *-opensourceseo.
REN *. *.csv

PAUSE

::**********End of Script**********