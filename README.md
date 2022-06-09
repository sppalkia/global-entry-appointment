# global-entry-appointment
Poll for global entry appointments.

# Making this work for you
You will probably have to edit this script to make it work for you. I suggest checking at least the following:

- [chromedriver](https://chromedriver.chromium.org/downloads) and Google Chrome are required.
- Location of your google-chrome binary. The script uses `/usr/bin/google-chrome`, but on MacOS you probably want `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`.
- Your desired interview location ID. Anchorage, SFO, and BOS (Logan) are in the script already, but you need to inspect the website source to get another airport. Just mouse over the link you want in your browser's web inspector and it the center ID should be within a few lines in the page source.
