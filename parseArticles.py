# "Articles" are also properly known as "determiners"
# References:
# https://learnenglish.britishcouncil.org/en/english-grammar/determiners-and-quantifiers
# http://dictionary.cambridge.org/us/grammar/british-grammar/determiners/a-an-and-the


# This removes articles from the input sentence
# Should less common ones (any, some, my, this, that, his, her) be removed also?
# Source / reference: http://dictionary.cambridge.org/us/grammar/british-grammar/determiners/a-an-and-the
def removeArticles(lineInput):
	newString = lineInput.replace(' the ', ' ')
	newString = newString.replace(' a ', ' ')
	newString = newString.replace(' an ', ' ')

	# ignored some that aren't likely to be encountered
	newString = newString.replace(' any ', ' ')
	newString = newString.replace(' some ', ' ')
	newString = newString.replace(' my ', ' ')
	newString = newString.replace(' this ', ' ')
	newString = newString.replace(' that ', ' ')
	return newString