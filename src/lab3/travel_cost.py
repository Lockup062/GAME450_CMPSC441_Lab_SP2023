'''
Lab 3: Travel Cost

Your player will need to move from one city to another in order to complete the game.
The player will have to spend money to travel between cities. The cost of travel depends 
on the difficulty of the terrain.
In this lab, you will write a function that calculates the cost of a route between two cities,
A terrain is generated for you 
'''
import numpy as np

def get_route_cost(route_coordinate, game_map):
  #my code ///////////////////////////////

#import numpy as np
# route = ((0,0),(5,4))
# gameMap = np.array([[2,3,4], [5,6,7], [8,9,10], [11,12,13], [14,15,16]])
# myroute = []
# myroute.insert(0,route[0][0])
# myroute.insert(1,route[0][1])
# myroute.insert(2,route[1][0])
# myroute.insert(3,route[1][1])

# def get_route_cost(route_coordinate, game_map):
#     cost = 0.0;

#     while(myroute[0]<myroute[2] and myroute[1]<myroute[3]):
#         cost += game_map[myroute[0],myroute[1]];
#         myroute[0]= (myroute[0])+1; 
#         myroute[1]= (myroute[1])+1; 
#         print(myroute[0],myroute[1] )
        

    
#     while(myroute[0]>myroute[2] and myroute[1]>myroute[3]):
#         cost += game_map[myroute[0],myroute[1]];
#         myroute[0]-1; 
#         myroute[1]-1; 

#     while(myroute[0]<myroute[2] and myroute[1]>myroute[3]):
#         cost += game_map[myroute[0],myroute[1]];
#         myroute[0]+1; 
#         myroute[1]-1; 

#     while(myroute[0]>myroute[2] and myroute[1]<myroute[3]):
#         cost += game_map[myroute[0],myroute[1]];
#         myroute[0]-1; 
#         myroute[1]+1; 

#     return cost

#NEW CODE NEW CODE NEW CODE NEW CODE NEW CODE NEW CODE NEW CODE NEW CODE NEW CODE NEW CODE NEW CODE NEW CODE NEW CODE NEW CODE NEW CODE NEW CODE NEW CODE NEW CODE 
##route = ((0,0),(5,4))
    x1, y1 = route_coordinate[0]
    x2, y2 = route_coordinate[1]
    x_diff = x2 - x1
    y_diff = y2 - y1
    steps = max(abs(x_diff), abs(y_diff))
    x_step = x_diff / steps
    y_step = y_diff / steps
    coords = []
    for i in range(steps + 1):
        x = x1 + i * x_step
        y = y1 + i * y_step
        coords.append((round(x), round(y)))
        
    return coords

numpy_array = np.zeros((6, 5))

path = shortest_path(route, numpy_array)
    """
    This function takes in a route_coordinate as a tuple of coordinates of cities to connect, 
    example:  and a game_map as a numpy array of floats,
    remember from previous lab the routes looked like this: [(A, B), (A, C)]
    route_coordinates is just inserts the coordinates of the cities into a route like (A, C).
    route_coordinate might look like this: ((0, 0), (5, 4))

    For each route this finds the cells that lie on the line between the
    two cities at the end points of a route, and then sums the cost of those cells
      -------------
    1 | A |   |   |
      |do you wanna build a snowman012-|
    2 |   |   |   |
      |-----------|
    3 |   | C |   |
      -------------
        I   J   K 

    Cost between cities A and C is the sum of the costs of the cells 
        I1, I2, J2 and J3.
    Alternatively you could use a direct path from A to C that uses diagonal movement, like
        I1, J2, J3

    :param route_coordinates: a list of tuples of coordinates of cities to connect
    :param game_map: a numpy array of floats representing the cost of each cell

    :return: a floating point number representing the cost of the route
    """
    # Build a path from start to end that looks like [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 4)]
    pass 
    return game_map[tuple(zip(*path))].sum()


def route_to_coordinates(city_locations, city_names, routes):
    """ get coordinates of each of the routes from cities and city_names"""
    route_coordinates = []
    for route in routes:
        start = city_names.index(route[0])
        end = city_names.index(route[1])
        route_coordinates.append((city_locations[start], city_locations[end]))
    return route_coordinates


def generate_terrain(map_size):
    """ generate a terrain map of size map_size """
    return np.random.rand(*map_size)


def main():
    # Ignore the following 4 lines. This is bad practice, but it's just to make the code work in the lab.
    import sys
    from pathlib import Path
    sys.path.append(str((Path(__file__)/'..'/'..').resolve().absolute()))
    from lab2.cities_n_routes import get_randomly_spread_cities, get_routes

    city_names = ['Morkomasto', 'Morathrad', 'Eregailin', 'Corathrad', 'Eregarta', 
                  'Numensari', 'Rhunkadi', 'Londathrad', 'Baernlad', 'Forthyr']
    map_size = 300, 200

    n_cities = len(city_names)
    game_map = generate_terrain(map_size)
    print(f'Map size: {game_map.shape}')

    city_locations = get_randomly_spread_cities(map_size, n_cities)
    routes = get_routes(city_names)
    np.random.shuffle(routes)
    routes = routes[:10]
    route_coordinates = route_to_coordinates(city_locations, city_names, routes)

    for route, route_coordinate in zip(routes, route_coordinates):
        print(f'Cost between {route[0]} and {route[1]}: {get_route_cost(route_coordinate, game_map)}')


if __name__ == '__main__':
    main()