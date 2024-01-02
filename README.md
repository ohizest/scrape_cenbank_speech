# Scrape_cenbank_speech
This Python script utilizes the Selenium library to scrape information about speaker names, speech dates, speech titles, and speech URLs from [this website](https://www.centralbank.ie/news-media/speeches). Users are prompted to input a start date and end date, and the script returns the relevant information from the returned pages within that date range in a csv file.
## Requirements
+ Python 3.x
+ Selenium
  ```bash
  pip install selenium
  ```

## Sample Scraped Information
| Speaker_Name        | Speech_Date           | Speech_Title       | Speech_URL  |
| ------------------- |:---------------------:| -------------:| -----------:|
| Derville Rowland      | 30 November 2023 | Private Assets: A changing European... | [link1](https://www.centralbank.ie/news/article/private-assets--a-changing-european-landscape---remarks-by-deputy-governor-derville-rowland-at-the-irish-funds--10th-annual-uk-symposium) |
|Gerry Cross	      | 23 November 2023      | “Implementing DORA” - Remarks by... |  [link2](https://github.com/ohizest/scrape_cenbank_speech/blob/main/Ireland_Bank_speech.csv#:~:text=https%3A//www.centralbank.ie/news/article/speech%2Dsharon,7) |


## Contributing
If you found an issue or would like to submit an improvement to this script, please, feel free to contribute by submitting issues or pull requests. Your feedback and suggestions are highly appreciated.
