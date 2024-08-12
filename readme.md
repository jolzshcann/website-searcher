# Python Website Searcher 
This is a simple website searching script that will find 1-2 defined strings within a pages html. (Basically automated ctrl+f)

There are a few inputs required to get started:

__Filename:__ this is the name of the txt file (include the .txt suffix) which contains the list of domains each on thier own line.

__Specific word:__ this is the most detailed word or phrase that will be searched to hopefully catch out false positives

__Unspecific word *(optional):*__ this is a word/phrase that is less detailed to the specific word that will hopefull catch out some false negatives
but still may containe some false positives.

---

e.g to search for an address from a list of sites the speific word would be the street number and street name (13 pitt) and the unspecific word would be just the street name (pitt). This is to create 2 seperate lists one that is 100% sure that the address has been found and one that is a 50/50 and has to be manually checked by a human. This is because (in my experience) some sites may have the street no and street name formatted differently i.e each on a new line and the script wont find those but may find other businesses with the same street name. Generally specific word gets them but the unspecific word is just a backup to double check.  There is some cases where the unspecific word catches a site but its not found on the actual page but it was found in html somewhere because when the sites are being searched its parsing ALL the HTML for that page.

---


Once the script has run through all sites 5 new text documents will be created with the date+time created:

- __specific_links:__ links that the specific word was found in
- __unspecific_links:__ links that the unspecific word was found in (or will be empty if none was selected)

The following 3 contain links that could not be access by the script, these links are generally toxic but there is sometimes false positive so just look at the link to determine if it was just toxic or need to be manually searched:
- __timeout_links:__ links that experienced a timeout error in the request. 
- __http_errors:__ links that experienced a http error (404,403,ssl issues etc). 
- __error_links:__ links that experienced an error other than the above that couldn't be accessed. 
