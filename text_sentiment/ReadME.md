# News Title Sentiment Analyzer

## Introduction

This repository contains code for a News Title Sentiment Analyzer. The purpose of this code is to analyze the sentiment of news article titles by inputting the article's URL into the `url` variable. The sentiment result ranges from -1 (extremely negative) to +1 (extremely positive).

## Usage

1. Clone this repository to your local machine using the following command:

   ```
   git clone https://github.com/your-username/news-title-sentiment-analyzer.git
   ```

2. Navigate to the project directory:

   ```
   cd news-title-sentiment-analyzer
   ```

3. Open the `main.py` file in your preferred code editor.

4. Locate the `url` variable at the beginning of the `main.py` file. Replace the default URL with the URL of the news article whose title you want to analyze.

   ```python
   # Example URL
   url = "https://www.example.com/news-article"
   ```

5. Run the script using the following command:

   ```
   python main.py
   ```

6. The script will analyze the sentiment of the news article's title and display the result, which will be a floating-point number between -1 and +1, with -1 indicating an extremely negative sentiment and +1 indicating an extremely positive sentiment.

## Dependencies

This project relies on the following Python libraries:

- [newspaper3k](https://newspaper.readthedocs.io/en/latest/): For web scraping the news article title from the provided URL and extracting other relevant information from the article.
- [TextBlob](https://textblob.readthedocs.io/en/dev/): For sentiment analysis of the news article title.

You can install these dependencies using the following command:

```
pip install newspaper3k textblob
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This code was created as a demonstration of sentiment analysis for news article titles.
- Feel free to modify and extend it for your own projects and needs.

If you encounter any issues or have suggestions for improvement, please open an issue on this GitHub repository.
