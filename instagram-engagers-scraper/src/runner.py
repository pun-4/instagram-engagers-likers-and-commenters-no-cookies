thonimport json
import logging
from extractors.instagram_parser import InstagramParser
from outputs.exporters import Exporter

logging.basicConfig(level=logging.INFO)

def run_scraper(input_data):
    try:
        parser = InstagramParser(input_data)
        parsed_data = parser.parse_comments()
        
        exporter = Exporter(parsed_data)
        exporter.export_to_json('output.json')
        
        logging.info(f"Scraper completed successfully. Data exported to 'output.json'")
    except Exception as e:
        logging.error(f"Error during scraping: {e}")

if __name__ == "__main__":
    input_data = json.load(open('data/inputs.sample.txt'))
    run_scraper(input_data)