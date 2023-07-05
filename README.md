# BBC Kiswahili Data Scraper
This repo contains python code that scrapes data from the [BBC Kiswahili website](https://www.bbc.com/swahili) and saves the 
data to a text file. The scraped data can then be imported into a csv file for further analysis.
The project was done as part of the requirements for the a friend's research project.

## Requirements
To run the scraper yourself, you'll need the following 

- python (3.6 or higher)

- beautifulsoup4 (4.12.2 or higher)

- requests library (2.31.0 or higher)

You can install the required libraries using pip.

```pip install beautifulsoup4```

```pip install requests```


## Usage
1. Clone the repository to your local machine

``` git clone https://github.com/brucemug/bbc-kiswahili-data-scraper.git```

2. Navigate to the project directory

```cd bbc-kiswahili-data-scraper```

3. To run the scraper, run the following command in your terminal

```python scraper.py```

** Caution: The classes (in html) to the BBC website can change at any time, and there might be a need to adjust the scraping code accordingly and also
The scraper will take a while to run. This is because it has to make a request to the BBC Kiswahili website for each category. **

On running for the first time, the scraper will create text files in the data folder. The text files will contain the scraped data. Files are titled according to the category of the article i.e. Afya.txt, Michezo.txt, etc.
On completion, the files can be imported into a csv file for further analysis.
 

## Contributing
If you would like to contribute to this project, please fork the repository and make changes as you see fit and submit a pull request. Contributions, suggestions and reports are all welcome.

## License
Feel free to modify the above template to suit your specific needs. You can also use the code as is.

