from langchain_community.tools import DuckDuckGoSearchRun

class SentinelResearcher:
    def __init__(self):
        self.search = DuckDuckGoSearchRun()

    def fact_check(self, query):
        """Searches the live web for market rates or legal data."""
        try:
            print(f"Sentinel is researching: {query}")
            # We limit the search to financial/legal context for accuracy
            search_query = f"{query} current market rates legal standards"
            results = self.search.run(search_query)
            return results
        except Exception as e:
            return f"Research failed: {str(e)}"
