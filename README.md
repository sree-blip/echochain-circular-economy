# echochain-circular-economy
EchoChain is a scalable data analytics project that integrates web scraping, data engineering, PySpark processing, and Power BI visualization to build a complete ETL pipeline and generate meaningful business insights

Web Scraping Engineer 
Role :- 
       Responsible for collecting marketplace product data through web scraping, validating records, and preparing datasets for downstream processing in the EchoChain project.
       
Week 1 Work :- 
  • Installed Python, Scrapy, and VS Code.
  •Learned website structure and created the         first spider.
  •Scraped sample product data.
  •Exported data in JSON and CSV formats.
  •Tested scraper and fixed errors.

Week 1 Tools Used :- 
 * Python
 * Scrapy
 * VS Code
 * Git & GitHub
 * 
Week 1 Outcome :- 

 • Working scraper developed.
 • Sample datasets prepared.
 • CSV and JSON files generated.

Week 2 Work :- 

• Improved scraping logic.
• Implemented pagination handling.
• Removed duplicate products.
• Validated scraped data.
• Performed automated scraping tests.

Week 2 Tools Used :- 

* Python
* Scrapy
* Pandas
* VS Code
* Git & GitHub
  
Week 2 Outcome :- 

• Clean scraped dataset generated.
• Improved scraping accuracy.
• Duplicate-free and validated data prepared for the next stage of processing.

## Week 3 - Member 1 (Web Scraping Engineer)

### Day 11 — Scraper Performance & Field Extraction Fix
Fixed a bug where product fields (Brand, Category, Condition, Seller, Rating, Location) were coming empty because the CSS selector wasn't capturing text inside nested `<strong>` tags — switched to XPath text extraction. Optimized scraper settings for faster crawling.

### Day 12 — Marketplace Testing
Performed consistency testing (multiple runs), load testing (increased concurrency), and added retry mechanism with timeout handling to ensure scraper reliability.

### Day 13 — Verify Scraped Records
Built a verification script (`verify_records.py`) that cross-checks scraped data against the live source. Result: 0 mismatches found across all 20 records.

### Day 14 — Error Handling
Added try/except handling in the parsing logic and an errback handler for request-level failures, ensuring the scraper degrades gracefully instead of crashing on unexpected errors.

### Day 15: Documentation (Week 3)
- Documented scraper functionality, setup, and usage from Weeks 1-3.
- (Pagination handling was completed earlier in Week 2.)

## Week 4 - Member 1 (Web Scraping Engineer)

### Day 16: Scheduling Scrapy Jobs
- Created `run_scraper.bat` to automate scraper execution.
- Set up Windows Task Scheduler to run the scraper daily at 9:00 AM.
  - Task name: `echochain scraper`
  - Trigger: Daily at 09:00
  - Action: Runs `run_scraper.bat`

### Day 17: Final Scraper Testing
- Full run test: 20 products scraped successfully.
- Edge case test: Invalid URL/port tested — scraper handles connection errors gracefully without crashing (retries 3 times, then logs error and closes cleanly).
- Data quality check: All columns populated correctly, no missing/duplicate entries.

### Day 18: Documentation
- Documented setup steps, run instructions, automation details, and testing summary (this section).

### Day 19: Bug Fixes
- Reviewed and resolved scraper issues found during testing.
- (Add specific bugs fixed here once identified.)

### Day 20: Final Demo Preparation
- Prepared scraper output and workflow for final team demo.

---

### How to Run
**Manual run:**
scrapy crawl products

**Using the batch script:**
Double-click `run_scraper.bat`, or run it from terminal:
run_scraper.bat

### Output
- File: `scraper_data.csv`
- Contains 14 defined columns (Bronze layer format)
- Final deliverable sheet: `Scraped_Marketplace_Data_Member1.xlsx`

### Known Notes
- Requires Python's `scrapy` module installed in the same Python environment referenced by `run_scraper.bat`
- If "No module named scrapy" error occurs, run: `pip install scrapy`
- Target site must be running on `http://127.0.0.1:5000/`