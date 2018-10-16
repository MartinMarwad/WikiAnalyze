"""
Created by Martin Marwad.
"""

import wikipedia
import wptools
from core.spacy import format_summary

def compare():
    pass

class Wikipedia(object):
    """Wikipedia API to python."""
    def __init__(self, query=str):
        # Define variables
        self.query = query
        self.query_page = None # Wikipedia (python package) object 
        self.query_results = None
        self.query_infobox = None
        self.query_summary = None
        self.query_image = None
        self.query_logo = None

    def search(self, query=str):
        """Returns a list of results from query."""
        if self.query:
            query = self.query 

        self.query_results = wikipedia.search(query)

        results = []
        for query in self.query_results:
            results.append([query, f"/wikipage/{query.replace(' ', '_')}"])

        return results

    def get_search_results(self):
        self.query_results = wikipedia.search(self.query)

        results = []
        for query in self.query_results:
            results.append([self.query, f"/wikipage/{self.query.replace(' ', '_')}"])

        return results

    def get_summary(self):
        wikipedia_page = wikipedia.page(self.query)
        self.query_summary = wikipedia_page.summary
        return self.query_summary

    def get_summary_formated(self):
        summary = self.get_summary()
        formatted = format_summary(summary)
        return formatted

    def get_image(self):
        return self.query_image

    def get_logo(self):
        return self.query_logo

    def get_infobox(self):
        # Get wikipedia article page
        self.query_page = wikipedia.page(self.query)
        wikipage = wptools.page(self.query)
        wikipage.get_parse()

        # Get InfoBox
        infobox = wikipage.data['infobox']

        # Organize the data better
        self.query_infobox = []
        for key, value in infobox.items():
            if key == "image":
                # Since we can only get the name of the file
                for image in self.query_page.images:
                    value = value.replace(' ', '_')
                    if value in image:
                        self.query_image = image
            if key == "logo":
                # Since we can only get the name of the file
                for image in self.query_page.images:
                    value = value.replace(' ', '_')
                    if value in image:
                        self.query_logo = image
            if key == "logofile":
                # Since we can only get the name of the file
                for image in self.query_page.images:
                    value = value.replace(' ', '_')
                    if value in image:
                        self.query_logo = image
            else:
                pass
            self.query_infobox.append([key, value])
        
        print(f"Debug: ImageURL - {self.query_image}")
        
        return self.query_infobox

