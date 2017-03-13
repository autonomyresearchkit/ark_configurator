#!/usr/bin/env python

from ark_configurator.srv import *
from geometry_msgs.msg import Polygon, Point32
import rospy

def setupHusky():
    max_fwd_velocity = 1.0  #[m/s]
    max_rev_velocity = 1.0  #[m/s]
    min_fwd_velocity = 0.3  #[m/s]
    max_accel = 0.03        #[m/s^2]
    max_decel = -0.03       #[m/s^2]
    max_ang_velocity = 1.2  #[rad/s]
    max_ang_accel = 0.2     #[rad/s^2]
    max_lateral_accel = 0.6 #[m/s^2] Max lateral accel during curves. Affects velocity.
    stiction_compensator_fwd = 0.1
    stiction_compensator_yaw = 0.01

    vehicle_length = 1.042    #[m]
    vehicle_width = 0.661    #[m]
    stopping_distance_1M = 0.30	#[m] - Stopping distance when traveling 1m/s
    lidar_spacing = 0.91 #[m] - spacing between the lidar

    vehicle_gear = 1    #0 - Mixed, 1 - Forward Only, 2 - Backward only.
    curve_type = 1  #0 - Linear, 1 - Curves.

    goal_threshold = 0.15		#[m] - How close to the goal for "success"
    orientation_corr_threshold = 0.05	#[rad] - How close to goal orientation for "success"

    mpc_horizon = 2.5   #The predicition horizon [s].
    min_lookahead = 2.0 #Minimum distance [in path parameter] ahead of the robot to do tracking and collision checks.
    max_lookahead = 3.0 #Maximum distance [in path parameter] ahead of the robot to do tracking and collision checks.

    horizon_percent_change = 0.20   #Percentage change when shortening the horizon (how quickly do we want to speed up after a curve slowdown).
    lookahead_smoother = 0.6    #Factor between 0 and 1 that determines the smoothness of the change in lookahead distance: 0 means only maximum velocity is used to determine the horizon (can be jumpy but speeds up the robot faster); 1 means only averaged planned velocity is used to determine the horizon (smoother but speeds up the robot slowly)
    lookahead_factor = 2.0      #How aggressively do we want to increase the lookahead from min_lookahead to max_lookahead.

    curvature_slowdown = 0.45   #Threshold [rad] on path curvature above which to slow down the robot.
    curvature_slowdown_multiplier = 1.2

    print "Waiting for configuration service..."
    rospy.wait_for_service("configure_ark")

    try:
        print "Reconfiguring ARK..."
        reConfigSettings = rospy.ServiceProxy('configure_ark', ArkConfigSettings)
        resp = reConfigSettings(max_fwd_velocity, max_rev_velocity, min_fwd_velocity, max_accel, max_decel, max_ang_velocity, max_ang_accel, max_lateral_accel, vehicle_length, vehicle_width, stopping_distance_1M, lidar_spacing, vehicle_gear, curve_type, goal_threshold, orientation_corr_threshold, mpc_horizon, min_lookahead, max_lookahead, horizon_percent_change, lookahead_smoother, lookahead_factor, curvature_slowdown, curvature_slowdown_multiplier)

        print resp.information
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    setupHusky()
