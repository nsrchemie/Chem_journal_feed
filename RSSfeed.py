import feedparser
import webbrowser
import datetime
def ChemJ_Feed():
	"""A function that prompts the user to choose from a premade list of Phytochemical/Natural Product articles listed by acronym
	Upon entering a journal a list of articles from the current RSS feed is returned.  The user is then prompted if they would
	like to save the file.  Afterwards another prompt asks the user to type the first few words of the title of an article that 
	interests them.  A web browser is then opened to the article page.

	PARAMETERS
	==========
	Input:
	None

	Output:
	
	"""
	RSS = {'JEP':'http://rss.sciencedirect.com/publication/science/5084', 'JNP':'https://feeds.feedburner.com/acs/jnprdf'}
	journal = input("Which journal would you like to view?" + '\n' + str([key for key in RSS.keys()]))
	titles = [text.title.encode('ascii','replace').decode('utf-8','ignore') + '\n' + text.link for text in feedparser.parse(RSS[journal]).entries]
	print('\n\n'.join(titles))
	save = input('Would you like to save this?')
	if save == "yes":
		fname = str(datetime.date.today())
		file = open(journal + fname, 'w')
		file.write(str(titles))
		file.close()
	options = input('\n' + 'Would you like to view a particular title in the browser? Type the first few words of the article.')
	for text in titles:
		if text.startswith(options):
			webbrowser.open(text[text.find('http:'):])

if __name__ == "__main__":
	ChemJ_Feed()