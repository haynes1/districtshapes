import fiona
import sys
import os
import numpy as np
import psycopg2
import json

shapefile_path = "../shapefiles/tl_2018_us_state/tl_2018_us_state.shp"
prj_path = "../shapefiles/tl_2018_us_state/tl_2018_us_state.prj"


def main(shapefile_path, prj_path):


	input = fiona.open(shapefile_path)

	i = 0
	for feat in input:
		
		#get metadata
		metadata = getMetaData(feat['properties']['STATEFP'])

		#process input coordinates
		input_coordinates = feat['geometry']['coordinates']
		geocoordinates = []
		if len(input_coordinates) > 1:
			for ic in input_coordinates:
				if len(ic) == 1:
					gc = np.array(ic[0],dtype=float)
				else:
					gc = np.array(ic, dtype=float)
				geocoordinates.append(gc)
		else:
			gc = np.array(input_coordinates[0],dtype=float)
			geocoordinates.append(gc)


		#export to datbase or wherever you want
		exportShapeFile()

main(shapefile_path, prj_path)