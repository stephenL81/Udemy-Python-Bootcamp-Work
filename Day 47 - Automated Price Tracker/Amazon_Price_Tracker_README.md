# Day 47 - Amazon Price Tracker

## Description

This automated price monitoring tool scrapes product pricing from Amazon-style product pages and sends email alerts when prices drop below a specified target. The application demonstrates web scraping, data extraction, price comparison logic, and automated email notifications using SMTP. Users can set a target price and receive instant email alerts when their desired product becomes affordable.

This project showcases practical automation for online shopping, combining BeautifulSoup for HTML parsing with Python's built-in SMTP library for email delivery.

---

## How to Run

### 1. Install required dependencies
```bash
pip install beautifulsoup4 requests python-dotenv
```

### 2. Set up Gmail App Password
For Gmail SMTP to work, you need an App Password (not your regular Gmail password):
- Go to your Google Account settings
- Navigate to Security → 2-Step Verification (enable if not already)
- Go to Security → App Passwords
- Generate a new app password for "Mail"
- Save this 16-character password for your `.env` file

### 3. Configure environment variables
Create a `.env` file in your project directory:
```
MY_EMAIL=your_email@gmail.com
MY_PASSWORD=your_16_char_app_password
```

### 4. Set your target price
Edit the `target` variable in the code to your desired price threshold (in dollars).

### 5. Run the application
```bash
python main.py
```

If the current price is below your target, you'll receive an email alert!

---

## How It Works

### Web Scraping
The program uses BeautifulSoup to parse the HTML from a product page and extract price information. Prices on Amazon-style sites are typically split into two parts:
- Whole dollars: `<span class="a-price-whole">`
- Cents/fraction: `<span class="a-price-fraction">`

The script locates these elements, extracts the text, strips whitespace, and combines them into a complete price string.

### Price Conversion
The combined price string (e.g., "99.99") is converted to a float for numerical comparison:
```python
price = f"{price_dollars}{price_cents}"  # "99" + "99" = "99.99"
float_price = float(price)  # Convert to 99.99
```

### Price Comparison
The program compares the current price against the user-defined target. If the price is below the target threshold, it triggers the email notification system.

### Email Notification (SMTP)
Using Python's `smtplib`, the program:
- Connects to Gmail's SMTP server (`smtp.gmail.com`)
- Establishes a secure TLS connection
- Authenticates with the user's credentials from environment variables
- Sends an email with subject "Price Alert!!" and the current price
- Confirms successful email delivery with a console message

The email body includes the current price in a clear, actionable format.

---

## Code Overview

```python
# Scrape product page and extract price components
soup = BeautifulSoup(response.text, "html.parser")
price_dollars = soup.find(name="span", class_="a-price-whole").text.strip()
price_cents = soup.find(name="span", class_="a-price-fraction").text.strip()

# Combine and convert to float for comparison
price = f"{price_dollars}{price_cents}"
float_price = float(price)

# Send email if price is below target
if float_price < float(target):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_address, password=email_password)
        connection.sendmail(
            from_addr=email_address,
            to_addrs=recipient_email,
            msg=f"Subject:Price Alert!!\n\nThe product is now ${float_price}"
        )
```

---

## Key Features

- **Automated price monitoring**: Scrapes current product prices without manual checking
- **Email alerts**: Instant notifications when price drops below target
- **Secure credential management**: Email credentials stored in environment variables
- **Configurable target**: Easy adjustment of price threshold
- **Clean data extraction**: Handles split price formatting (dollars and cents)
- **TLS encryption**: Secure email transmission using STARTTLS

---

## Technical Skills Demonstrated

- **Web Scraping**: Using BeautifulSoup to parse HTML and extract specific elements
- **HTTP Requests**: Fetching web pages with custom headers
- **String Manipulation**: Combining text, stripping whitespace, type conversion
- **SMTP Email Automation**: Sending emails programmatically with Python
- **Environment Variables**: Secure credential storage and retrieval
- **Conditional Logic**: Price comparison and decision-making
- **Error Prevention**: Using context managers (`with` statements) for connection handling

---

## Project Limitations & Notes

### Real Amazon Limitations

This project uses a **static demo URL** (`appbrewery.github.io/instant_pot/`) rather than live Amazon pages. Real Amazon product pages present significant challenges for basic web scraping:

**Challenge: Dynamic Content Loading**

Modern Amazon pages load pricing data dynamically using JavaScript after the initial HTML is delivered. Basic HTTP requests (like `requests.get()`) only retrieve the initial HTML without executing JavaScript, meaning price elements often don't exist in the scraped content.

**Why the Demo URL:**

The static demo page contains all price information in the initial HTML, making it ideal for learning BeautifulSoup fundamentals without the complexity of:
- Browser automation (Selenium/Playwright)
- JavaScript rendering
- Anti-bot detection systems
- CAPTCHA challenges
- Regional restrictions and A/B testing

**Real-World Solution:**

Production Amazon price trackers typically use:
- **Selenium/Playwright**: Browser automation to execute JavaScript and wait for dynamic content
- **Headless browsers**: Chrome/Firefox running without UI for automated scraping
- **Rotating proxies**: To avoid IP-based blocking
- **CAPTCHA solving services**: To handle anti-bot measures
- **Official APIs**: Where available (Amazon Product Advertising API)

This project demonstrates the core concepts of price monitoring and email automation, which remain the same regardless of the data source. The scraping technique learned here applies to many e-commerce sites, particularly smaller retailers that serve static HTML.

---

## Use Cases

- **Deal hunting**: Monitor products for price drops during sales events
- **Budget shopping**: Get notified when items fit within your budget
- **Gift planning**: Track prices for upcoming birthdays or holidays
- **Price history**: Run periodically to build a database of price changes
- **Multi-product monitoring**: Modify to track multiple products simultaneously

---

## Possible Enhancements

- Schedule regular checks using `schedule` library or cron jobs
- Track multiple products with a list of URLs and targets
- Store price history in a database or CSV file
- Add SMS alerts using Twilio API
- Include product name and image in email notification
- Implement exponential backoff for failed requests
- Add logging for debugging and monitoring

---

## Setup Notes

- Gmail SMTP requires an App Password, not your regular account password
- The demo URL always shows the same price (useful for testing logic)
- To test email functionality, set `target` higher than the current price initially
- The SMTP connection automatically closes with the `with` statement
- Consider rate limiting if expanding to monitor multiple products
