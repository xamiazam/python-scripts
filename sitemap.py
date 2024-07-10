import requests
import csv
import xml.etree.ElementTree as ET
import os


def scrape_sitemap_links(sitemap_url):
    # Fetch the sitemap XML content
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(sitemap_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch sitemap: {response.status_code}")
        return []

    # Parse XML
    root = ET.fromstring(response.content)

    # Find all <loc> tags within the sitemap
    loc_tags = root.findall(
        './/{http://www.sitemaps.org/schemas/sitemap/0.9}loc')

    # Extract URLs from loc tags
    links = [loc.text.strip() for loc in loc_tags]

    return links


def save_links_to_csv(links):
    # Get the current script directory
    script_dir = os.path.dirname(__file__) if __file__ else '.'

    # Define the CSV file path
    csv_file = os.path.join(script_dir, 'sitemap_links.csv')

    # Write links to CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['URL'])  # Write header
        writer.writerows([[link] for link in links])

    print(f"Saved {len(links)} links to {csv_file}")


# Example usage:
sitemap_url = 'https://website-address.com/sitemap.xml'
sitemap_links = scrape_sitemap_links(sitemap_url)
save_links_to_csv(sitemap_links)
