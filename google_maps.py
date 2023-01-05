import googlemaps 

gmaps = googlemaps.Client(key='Google_api_key')  

place_1 = 'Rosemala, 691309'
place_2 = 'HSR Layout, 560102'

distance = gmaps.distance_matrix(place_1, place_2)['rows'][0]['elements'][0]

print(distance)