This is the website searcher  that will search for 1-2 specific strings in list of websites html.
A few inputs are required to start.

filename: ths name of the txt file (include the .txt suffix) for that contains the list of domains each on thier own line. 
Best way to do this is do download a csv/xlsx and copy the list of refering domains column to a text file

Specific word: this is the most detailed word or phrase that will be searched to hopefully catch out false positives

Unspecific word (optional): this is a word/phrase that is less detailed to the specific word that will hopefull catch out some false negatives
but still may containe some false positives.

e.g to search for an address from a list of sites the speific word would be the street number and street name (13 pitt) and the unspecific word would be just the street name (pitt).
This is to create 2 seperate lists one that is 100% sure that the address has been found and one that is a 50/50 and has to be manually checked by a human
This is because (in my experience) some sites may have the street no and street name formatted differently i.e each on a new line and the script wont find those
but may find other businesses with the same street name. Generally specific word gets them but the unspecific word is just a backup to double check. 
There is some cases where the unspecific word catches a site but its not found on the actual page but it was found in html somewhere because when the sites are being searched its parsing ALL the HTML for that page.

Once the script has run through all sites 5 new text documents will be created with the date+time created

specific_links: links that the specific word was found in
unspecific_links: links that the unspecific word was found in (or will be empty if none was selected)
The following 3 contain links that could not be access by the script, these links are generally toxic but there is sometimes false positive so just look at the link to determine if it was just toxic or need to be manually searched
timeout_links: links that experienced a timeout error in the request. 
http_errors: links that experienced a http error (404,403,ssl issues etc). 
error_links: links that experienced an error other than the above that couldn't be accessed. 
