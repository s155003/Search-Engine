import requests

#5d89a1427990ef5632ef74f2740a5b6478b56b7cc6ddc6da7a3a3f731c4ffbf5
def search_web(query, api_key):
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": api_key,
        "engine": "google"
    }
    response = requests.get(url, params=params)
    data = response.json()
    results = data.get("organic_results", [])
    return results

def main():
    api_key = input("Enter your SerpAPI key: ").strip()
    while True:
        query = input("\nEnter your search query (or 'exit' to quit): ")
        if query.lower() == "exit":
            break
        results = search_web(query, api_key)
        if not results:
            print("No results found.")
        else:
            for i, result in enumerate(results, 1):
                print(f"\nResult {i}:")
                print("Title:", result.get("title"))
                print("Link:", result.get("link"))
                print("Snippet:", result.get("snippet"))

if __name__ == "__main__":
    main()
