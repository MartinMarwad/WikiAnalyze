"""
Created by Martin Marwad.





import wikipedia
import wptools

class SearchResult:
    related = None


class SearchWikipedia(object):
    def __init__(self, query=str):
        Requires a search query in string format.
        self.searchresult = SearchResult()

        # Returns possible matches.
        queries = wikipedia.search(query)
        
        if queries != None:
            # Save results
            self.searchresult.related = queries

            # Search Wikipedia and returns the result.
            query = queries[0]
            wikipage = wikipedia.page(query)
            page = wptools.page(query)
            page.get_parse()

            # Get the info box on the page.
            infobox = page.data['infobox']

            # Determine the attributes in the infobox.
            for attribute in infobox:
                if attribute == 'birth_name':
                    self.searchresult.fullname = infobox['birth_name']
                elif attribute == 'office':
                    self.searchresult.title = infobox['office'].replace('[', '').replace(']', '')
                elif attribute == 'birth_date':
                    self.searchresult.birth_date = parser.parse(infobox['birth_date'].split('|', 1)[1].replace("}", "").replace('|', '-'))
                elif attribute == 'image':
                    self.searchresult.image = page.images()[0]['url']
                elif attribute == 'party':
                    self.searchresult.political_party = infobox['party'].replace(']', '').split('|')[1]
        else:
            pass

    def save(self):
        return self.searchresult

"""