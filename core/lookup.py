"""
Created by Martin Marwad.

This module will 
"""

import wikipedia
import wptools


# Try to Lookup Author
author, error = self.lookup_author(author)
def lookup_author(self, author):
    """Look up author on wikipedia, and extract info from infobox."""

    # We will grab the first person closest to the name
    candidates = wikipedia.search(author.name)

    if candidates:
        candidate = candidates[0]
        wikipage = wikipedia.page(candidate)

        # Now we check if this is the right person
        # We can see if the author's source name is in their wikipedia page
        if author.source in wikipage.content:
            # Hurray! This is the right person

            # Now, get all their details from wikipedia's infobox
            page = wptools.page(candidate)
            page.get_parse()

            infobox = page.data['infobox']

            # We know these values are always there
            author.wikipage = wikipage.url
            author.description = wikipedia.summary(candidate)

            # infobox sometimes returns []
            for attribute in infobox:
                if attribute == 'birth_name':
                    author.fullname = infobox['birth_name']
                elif attribute == 'office':
                    author.title = infobox['office'].replace(
                        '[', '').replace(']', '')
                elif attribute == 'birth_date':
                    author.birth_date = parser.parse(infobox['birth_date'].split('|', 1)[
                                                        1].replace("}", "").replace('|', '-'))
                elif attribute == 'image':
                    author.image = page.images()[0]['url']
                elif attribute == 'party':
                    author.political_party = infobox['party'].replace(']', '').split('|')[
                        1]

            # Process
            # page.data['infobox']['instrument']

            # author.fullname         = page.data['infobox']['birth_name']
            # author.name             = author.name
            # author.wikipage         = wikipage.url
            # author.title            = page.data['infobox']['office'].replace('[','').replace(']', '')
            # author.birth_date       = parser.parse( page.data['infobox']['birth_date'].split('|', 1)[1].replace("}", "").replace('|', '-') )
            # author.image            = page.images()[0]['url']
            # author.description      = wikipedia.summary(candidate)
            # author.political_party  = page.data['infobox']['party'].replace(']','').split('|')[1]

            return author, None  # Error is None
        else:
            # Wrong person. Perhaps the source name isn't exactly spelled as in the wikipedia page?
            # The Author exists, but doesn't seem to be associated with the source.
            return author, "Wrong Author?"
    else:
        return author, "Author Not On Wikipedia!"

