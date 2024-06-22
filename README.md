# scrapy_parser_pep
## Parser for pep versions based on scrapy framework

## Deploy
1. Install python venv
   ```bash
    python -m venv venv
   ```
2. Update pip
   ```bash
    python3 -m pip install --upgrade pip
   ```
3. Install libraries from 'requirements.txt'
   ```bash
    pip install -r 'requirements.txt'
   ```  
4. start scrapy from scrapy_parser_pep folder
   ```bash
    scrapy crawl pep
   ```

## Result
After initial start folder 'results' will be created, where will be located all output files.
All files are in csv format. 'pep' file will contain all parsed peps with number, name and status.
'status_summary' file will contain all statuses and their amount.

## Stack:
* Python 3.11.3
* Scrapy 2.5.1
* Twisted 22.2.0

### Author: mitsushidu
    
