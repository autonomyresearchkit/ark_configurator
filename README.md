Setting the Configuration:
Send a message to: /ark_config_settings_call
Setting	Info
max_fwd_velocity	[m/s]
max_rev_velocity	[m/s]
min_fwd_velocity	[m/s]
max_accel	[m/s^2]
max_decel	[m/s^2]
max_ang_velocity	[rad/s]
max_ang_accel	[rad/s^2]
max_lateral_accel	[m/s^2] Max lateral accel during curves. Affects velocity.
vehicle_length	[m]
vehicle_width	[m]
stopping_distance_1M	[m] - Stopping distance when traveling 1m/s
lidar_spacing	[m] - spacing between the lidar
laser_fov	[deg]
vehicle_gear	0 – Mixed, 1 - Forward Only, 2 - Backward only.
curve_type	0 – Linear, 1 – Curves.
goal_threshold	[m] - How close to the goal for "success"
orientation_corr_threshold	[rad] - How close to goal orientation for "success"
mpc_horizon	The predicition horizon [s].
min_lookahead	Minimum distance [in path parameter] ahead of the robot to do tracking and collision checks.
max_lookahead	Maximum distance [in path parameter] ahead of the robot to do tracking and collision checks.
horizon_percent_change	Percentage change when shortening the horizon (how quickly do we want to speed up after a curve slowdown).
lookahead_smoother	
Factor between 0 and 1 that determines the smoothness of the change in lookahead distance: 0 means only maximum velocity is used to determine the horizon (can be jumpy but but speeds up the robot faster); 1 means only averaged planned velocity is used to determine the horizon (smoother but speeds up the robot slowly)
lookahead_factor	How aggressively do we want to increase the lookahead from min_lookahead to max_lookahead.
curvature_slowdown	Threshold [rad] on path curvature above which to slow down the robot.
Verifying it was set:
Status and information response from: /ark_config_settings_response
