#!/usr/bin/env python

from ark_configurator.srv import *
from geometry_msgs.msg import Polygon, Point32
import rospy

def setupHusky():
    max_fwd_velocity = 1.0
    max_rev_velocity = 1.0
    min_fwd_velocity = 0.3
    max_accel = 0.03
    max_decel = -0.03
    max_ang_velocity = 1.2
    max_ang_accel = 0.2
    max_lateral_accel = 0.6
    stiction_compensator_fwd = 0.1
    stiction_compensator_yaw = 0.01

    vehicle_length = 1.0
    replan_enabled = True
    vehicle_gear = 1
    curve_type = 1

    goal_threshold = 0.15
    orientation_corr_threshold = 0.05

    mpc_horizon = 2.5
    min_lookahead = 2.0
    max_lookahead = 3.0

    horizon_percent_change = 0.20
    lookahead_smoother = 0.6
    lookahead_factor = 2.0

    curvature_slowdown = 0.45
    curvature_slowdown_multiplier = 1.2

    footprint = Polygon()
    footprint.points.append(Point32(-0.5, -0.33, 0))
    footprint.points.append(Point32(-0.5, 0.33, 0))
    footprint.points.append(Point32(0.5, 0.33, 0))
    footprint.points.append(Point32(0.5, -0.33, 0))

    rospy.wait_for_service("configure_ark")
    try:
        reConfigSettings = rospy.ServiceProxy('configure_ark', ArkConfigSettings)
        resp = reConfigSettings(max_fwd_velocity, max_rev_velocity, min_fwd_velocity, max_accel, max_decel, max_ang_velocity, max_ang_accel, max_lateral_accel, vehicle_length, vehicle_gear, curve_type, goal_threshold, orientation_corr_threshold, mpc_horizon, min_lookahead, max_lookahead, horizon_percent_change, lookahead_smoother, lookahead_factor, curvature_slowdown, curvature_slowdown_multiplier, footprint)

        print resp.information
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    setupHusky()
