# Politicrowd Autofact
## A Chrome extension for semi-automatically factchecking news articles

### About 

This is a not-for-profit project to build a tool that can help users determine whether content in text articles is correct.
We are just entering the developmet phase of this tool and a stable version has not been built yet.

======
### Installing the extension

1. Clone this repo.
2. Using the chrome browser, navigate to chrome://extensions
3. Check the developer mode box.
4. Click "Load Unpacked Extension" and set the path to ../politicrowd_autofact/politicrowd_extension.
5. Use the extension by clicking the politicrowd logo in the upper right corner of your chrome window.

======
### Backend python scripts

The scripts we use to scrape politifact data are included in backend_python_scripts. 
In the current verions, the user enters a sentence or key words into the text field of our extension and it returns a list of statements from Politifact.

======
### Goals of the project

1. Enable the extension to scan sentences on the page without them having to be entered in manually
2. Develop a more intelligent search algorithm to match sentences to relevant facts.


Built by www.politicrowd.com

Please contact us if you would like to get involved.
