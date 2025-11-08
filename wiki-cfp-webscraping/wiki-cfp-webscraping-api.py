import requests
import uuid
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request

app = Flask(__name__)

def scrape_events(url):
    # Page counter
    page = 1

    # End of pages flag
    end_of_pages = False

    # Event data list
    events = []

    print(f"Scraping URL: {url}")

    while not end_of_pages:
        paged_url = f"{url}&page={page}"

        response = requests.get(paged_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        tables = soup.find_all("table")
        if len(tables) < 2:
            print("Could not find the CFP table.")
            break

        cfp_table = tables[5]  # The 6th table contains the CFP listings

        # Extract table rows
        rows = cfp_table.find_all("tr")[1:]  # Skip header row
        
        if not rows or 'Expired CFPs' in rows[0].text:
            end_of_pages = True
            break

        i = 0
        while i < len(rows):
            if 'Expired CFPs' in rows[i].text:
                end_of_pages = True
                break

            # Each event is represented by two consecutive rows
            if i + 1 < len(rows):
                first_row = rows[i].find_all("td")
                second_row = rows[i + 1].find_all("td")

                if len(first_row) >= 2 and len(second_row) >= 3:
                    event = {
                        "acronym": first_row[0].text.strip(),
                        "name": first_row[1].text.strip(),
                        "when": second_row[0].text.strip(),
                        "where": second_row[1].text.strip(),
                        "deadline": second_row[2].text.strip(),
                        "enabled": True
                    }

                    # Generating a ID using UUID of the concatenated string of all fields
                    unique_string = f"{event['acronym']}{event['name']}{event['when']}{event['where']}{event['deadline']}"
                    event['id'] = str(uuid.uuid5(uuid.NAMESPACE_DNS, unique_string))
                    
                    # Append event to the list
                    events.append(event)
                i += 2
            else:
                break

        page += 1

    return events


@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({"error": "Missing 'url' in request body"}), 400
    try:
        events = scrape_events(url)
        return jsonify(events)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)