# Empire Top 100 Movies Web Scraper

## Description

This web scraper extracts the Empire Magazine "Top 100 Greatest Movies" list from a archived web page and saves it to a text file with proper formatting. The script handles data cleaning challenges including reversing the list order and correcting non-standard title formatting (e.g., "Godfather, The" becomes "The Godfather"). This project demonstrates fundamental web scraping techniques, data transformation, and file handling in Python.

The scraper uses the Internet Archive's Wayback Machine to access a snapshot of the original Empire Online article, ensuring the data source remains stable and accessible even if the original page changes or is removed.

---

## How to Run

### 1. Install required dependencies
```bash
pip install requests beautifulsoup4
```

### 2. Run the script
```bash
python main.py
```

The script will:
- Scrape the movie list from the archived web page
- Clean and format the data
- Save the top 100 movies to `movies.txt` in numbered order

---

## How It Works

### Web Scraping
The script uses the `requests` library to fetch the HTML content from the Internet Archive's snapshot of the Empire Online article. BeautifulSoup parses the HTML to locate and extract movie titles from within the page structure.

### Data Extraction
Movie titles are found within `<a>` tags nested inside a `<div>` with class `entity-info-items__list`. The script extracts all anchor tag text values into an initial list.

### Data Transformation
**List Reversal:** The original scraped data is in reverse order (100 to 1), so the list is reversed to display movies from rank 1 to 100.

**Title Formatting:** Many movie titles use non-standard formatting where articles like "The" appear at the end with a comma (e.g., "Godfather, The"). The script identifies these cases and reformats them to standard English (e.g., "The Godfather").

**Edge Case Handling:** The formatting logic correctly handles titles containing multiple commas (e.g., "The Good, The Bad & The Ugly, The" becomes "The Good, The Bad & The Ugly") by only moving the article from the end of the title.

### File Output
The cleaned and formatted list is written to `movies.txt` with sequential numbering (1-100) and proper line breaks for readability.

---

## Code Overview

```python
# Fetch the archived web page
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Extract movie titles from the HTML structure
movies_html = soup.find(name="div", class_="entity-info-items__list")
names = movies_html.find_all("a")

# Reverse the list to get correct ranking order
movies_initial_list.reverse()

# Fix title formatting
for movie in movies_initial_list:
    if movie.endswith(", The"):
        formatted_movie = f"The {movie[:-5]}"
    else:
        formatted_movie = movie

# Write to file with numbering
with open("movies.txt", mode="w") as file:
    for number, movie in enumerate(the_list, start=1):
        file.write(f"{number}) {movie}\n")
```

---

## Key Features

- **Automated data extraction**: Scrapes 100 movie titles without manual copying
- **Data cleaning**: Handles non-standard title formatting automatically
- **Edge case handling**: Correctly processes titles with multiple commas
- **File generation**: Creates a clean, numbered text file ready for use
- **Archived source**: Uses Internet Archive for stable, reliable data access
- **Minimal dependencies**: Only requires requests and BeautifulSoup

---

## Technical Skills Demonstrated

- **Web Scraping**: Using BeautifulSoup to parse HTML and extract specific elements
- **HTTP Requests**: Fetching web page content with the requests library
- **Data Transformation**: Cleaning and reformatting scraped data programmatically
- **String Manipulation**: Handling edge cases in text processing (slicing, concatenation, conditionals)
- **File I/O**: Writing formatted data to text files
- **List Operations**: Reversing lists and iterating with enumeration
- **Problem-Solving**: Identifying and handling data quality issues (formatting inconsistencies)

---

## Use Cases

- **Movie recommendation reference**: Quick access to critically acclaimed films
- **Watchlist creation**: Export for tracking which films you've seen
- **Data analysis foundation**: Clean dataset for further processing (e.g., cross-referencing with IMDb ratings, release years, etc.)
- **Learning resource**: Demonstrates practical web scraping workflow from data extraction to cleaned output

---

## Notes

- The script uses a specific snapshot from the Internet Archive (May 18, 2020) to ensure consistency
- The original Empire Online page structure may have changed since then, making the archived version more reliable
- Output file `movies.txt` is overwritten each time the script runs
- Some titles may retain original formatting if they don't match the ", The" pattern (e.g., titles ending with ", A" would need additional logic)
- The scraper respects the archived page's structure; changes to the page HTML would require updating the BeautifulSoup selectors
