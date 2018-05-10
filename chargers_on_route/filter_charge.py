import random_points
import matplotlib.pyplot as plt
from matplotlib import interactive
import maps_integration


def filter_charger(input_route, charger_list):
	"""
	input_route is a list of points, every one of them contains two numbers, longitude and latitude.
	charger_list is a list of random points on the map, also contain longitude and latitude.
	
	The aim is to get a list of chargers along the path within 0.03 miles.
	"""

	long_list = []
	lat_list = []
	
	# Loop through the route, group all longitude and latitude into two lists. 
	for route_point in input_route:
		long_list.append(route_point.longitude)
		lat_list.append(route_point.latitude)
	
	long_min = min(long_list) - 0.03
	long_max = max(long_list) + 0.03
	lat_min = min(lat_list) - 0.03
	lat_max = max(lat_list) + 0.03

	# Filter the charger.
	# The route forms a block within the longitude and latitude range, filter out the charger outside of it.
	charger_in_range = []
	for charger in charger_list:
		if charger.longitude <= long_max and charger.longitude >= long_min:
			if charger.latitude <= lat_max and charger.latitude >= lat_min:
				charger_in_range.append(charger)

	# Do calculations to filter more.
	# Keep chargers within 2 miles distance from the route, which is 0.03 degree either longitude or latitude. 
	final_charger = []
	for charger in charger_in_range:
		for route_point in input_route:
			if abs(route_point.longitude - charger.longitude) < 0.03 and abs(route_point.latitude - charger.latitude) < 0.03:
				final_charger.append(charger)
				break

	return final_charger


def test():
	start_point = random_points.Point(32, 32)
	end_point = random_points.Point(35, 35)
	charger = random_points.generate_random_points(30, 40, 30, 40, 10000)
	route = maps_integration.getRoute([51.652169, -0.084417], [55.950398, -3.180827])
	charger_list_final = filter_charger(route, charger)

	route_long = []
	route_lat = []
	for i in route:
		route_long.append(i.longitude)
		route_lat.append(i.latitude)

	charger_long = []
	charger_lat = []
	for i in charger:
		charger_long.append(i.longitude)
		charger_lat.append(i.latitude)

	# Build the figure with route and original charger.
	plt.figure(1)
	plt.xlabel("Longitude")
	plt.ylabel("Latitude")
	plt.title("The Map")
	plt.scatter(charger_long, charger_lat, label="Charger", color="red", marker="*", s=5)
	plt.plot(route_long, route_lat, label="Car Route", color="blue")
	plt.legend()
	interactive(True)
	plt.show()

	charger_final_long = []
	charger_final_lat = []
	for i in charger_list_final:
		charger_final_long.append(i.longitude)
		charger_final_lat.append(i.latitude)

	# Build the figure with route and filtered charger.
	plt.figure(2)
	plt.xlabel("Longitude")
	plt.ylabel("Latitude")
	plt.title("Filtered Map")
	plt.scatter(charger_final_long, charger_final_lat, label="Charger", color="red", marker="*", s=5)
	plt.plot(route_long, route_lat, label="Car Route", color="blue")
	plt.legend()
	interactive(False)
	plt.show()


test()