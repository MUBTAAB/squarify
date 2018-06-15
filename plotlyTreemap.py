def plotly_treemap(dataframe, groups, subgroups, values, filename = None, colors = None):
	import pandas as pd 
	import squarify 
	
	#Create parent squaresizes
	dataframe = dataframe.sort_values(groups)
	grp = dataframe.groupby(groups)[values].sum()
	
	#Initialize first square
	x = 0.
	y = 0.
	width = 100.
	height = 100.

	sizes = grp.values
	
	# Parent squares 
	normed = squarify.normalize_sizes(sizes, width, height)
	rects = squarify.squarify(normed, x, y, width, height)

	subrects = []

	for group, rect in zip(set(dataframe[groups]), rects):

		dff = dataframe[dataframe[groups] == group][values]
		x = rect['x']
		y = rect['y']
		width = rect['dx']
		height = rect['dy']
		sizes = dff.values
		normed = squarify.normalize_sizes(sizes, width, height)
		rectgroup = squarify.padded_squarify(normed, x, y, width, height)
		subrects += rectgroup

	return(subrects)


