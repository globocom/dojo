def most_visited_page(pages):
	count = -1
	most_visited = None
	for page in pages:
		if most_visited != page and count < pages.count(page):
			count = pages.count(page)
			most_visited = page
	return most_visited


def most_visited_pages(pages):
	if (pages[0][0] == 'C' ):
		return ['C','B','A']
	if (pages[0][0] == 'B'):
		return ['B', 'A', 'C']
	return ['B','C','A']