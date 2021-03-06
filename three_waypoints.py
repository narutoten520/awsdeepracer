def reward_function(params):

    import math

    #Read all input variables
    all_wheels_on_track = params['all_wheels_on_track']
    x = params['x']
    y = params['y']
    distance_from_center = params['distance_from_center']
    is_left_of_center  = params['is_left_of_center']
    heading = params['heading']
    progress = params['progress']
    steps = params['steps']
    speed = params['speed']
    steering_angle = params['steering_angle']
    track_width = params['track_width']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']

    #Start with initial reward
    reward = 1.0

    #Reward Car Direction Aligned with Upcoming Track Direction (Three Waypoints Ahead)
    three_waypoints_ahead = waypoints[(closest_waypoints[1]+2) % len(waypoints)]

    y3 = three_waypoints_ahead[1]
    x3 = three_waypoints_ahead[0]

    three_waypoints_ahead_direction = math.degrees(math.atan2(y3 - y, x3 - x))

    #Heading is based on Positive from X Axis CCW and Negative below X Axis (-180 to 180 deg)
    heading_difference = abs(three_waypoints_ahead_direction - heading)
    if heading_difference > 180:
        heading_difference = 360 - heading_difference
    
    #Reward Better Aligned direction towards 2 waypoints ahead
    if heading_difference > 15:
        reward *= 0.7
    
    # Reward higher speed
    if speed < 2:
        reward *= 0.7

    return float(reward)