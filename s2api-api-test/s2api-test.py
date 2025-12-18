from semantic_scholar import SemanticScholar
import asyncio

async def main():
    # Initialize client (API key optional for basic usage)
    client = SemanticScholar()

    # Search for papers
    papers = await client.search_papers("machine learning", limit=10)
    #print(f"Found {len(papers)} papers")

    # Get paper details
    paper = await client.get_paper("paper-id")
    print(paper)

if __name__ == "__main__":
    asyncio.run(main())