# scrapy_parser_pep
## Parser for pep versions based on scrapy framework

## Deploy
1. Install python venv
   ```
    python -m venv venv
   ```
2. Update pip
   ```
    python3 -m pip install --upgrade pip
   ```
3. Install libraries from 'requirements.txt'
   ```
    pip install -r 'requirements.txt'
   ```  
4. start scrapy from scrapy_parser_pep folder
   ```
    scrapy crawl pep
   ```

## Result
After initial start folder 'results' will be created, where will be located all output files.
All files are in csv format. 'pep' file will contain all parsed peps with number, name and status.
'status_summary' file will contain all statuses and their amount.

## Stack
1. Scrapy
2. response

### Author: mitsushidu
    
