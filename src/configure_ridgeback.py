#!/usr/bin/env python

from ark_bridge.msg import ArkConfigSettingsResponse, ArkConfigSettingsCall
import time
import rospy

def response_callback(data):
  global started
  if started:
    print data.information
    rospy.signal_shutdown("Ark Configured")

def setupRidgeback():
    global started
    started = False
    print "Starting..."

    rospy.init_node("ridgeback_configurator")

    rospy.Subscriber("/ark_bridge/ark_config_settings_response", ArkConfigSettingsResponse, response_callback)
    time.sleep(0.3)
    started = True

    print "Configuring Ark for Ridgeback"

    pub = rospy.Publisher("/ark_bridge/ark_config_settings_call", ArkConfigSettingsCall, latch=True, queue_size=1)
    settingsMsg = ArkConfigSettingsCall()

    settingsMsg.max_fwd_velocity = 1.0  #[m/s]
    settingsMsg.max_rev_velocity = 1.0  #[m/s]
    settingsMsg.min_fwd_velocity = 0.05  #[m/s]
    settingsMsg.max_accel = 0.3        #[m/s^2]
    settingsMsg.max_decel = -0.3       #[m/s^2]
    settingsMsg.max_ang_velocity = 1.0  #[rad/s]
    settingsMsg.max_ang_accel = 0.3     #[rad/s^2]
    settingsMsg.max_lateral_accel = 0.3 #[m/s^2] Max lateral accel during curves. Affects velocity.
    settingsMsg.vehicle_length = 0.960    #[m]
    settingsMsg.vehicle_width = 0.800    #[m]
    settingsMsg.stopping_distance_1M = 0.40	#[m] - Stopping distance when traveling 1m/s
    settingsMsg.lidar_spacing = 0.8254 #[m] - spacing between the lidar
    settingsMsg.laser_fov = 270.0 #[deg]
    settingsMsg.vehicle_gear = 1    #0 - Mixed, 1 - Forward Only, 2 - Backward only.
    settingsMsg.curve_type = 1  #0 - Linear, 1 - Curves.
    settingsMsg.goal_threshold = 0.15		#[m] - How close to the goal for "success"
    settingsMsg.orientation_corr_threshold = 0.05	#[rad] - How close to goal orientation for "success"
    settingsMsg.mpc_horizon = 3.0   #The predicition horizon [s].
    settingsMsg.min_lookahead = 2.0 #Minimum distance [in path parameter] ahead of the robot to do tracking and collision checks.
    settingsMsg.max_lookahead = 3.0 #Maximum distance [in path parameter] ahead of the robot to do tracking and collision checks.
    settingsMsg.horizon_percent_change = 0.06   #Percentage change when shortening the horizon (how quickly do we want to speed up after a curve slowdown).
    settingsMsg.lookahead_smoother = 0.4    #Factor between 0 and 1 that determines the smoothness of the change in lookahead distance: 0 means only maximum velocity is used to determine the horizon (can be jumpy but speeds up the robot faster); 1 means only averaged planned velocity is used to determine the horizon (smoother but speeds up the robot slowly)
    settingsMsg.lookahead_factor = 1.45      #How aggressively do we want to increase the lookahead from min_lookahead to max_lookahead.
    settingsMsg.curvature_slowdown = 0.6   #Threshold [rad] on path curvature above which to slow down the robot.

    pub.publish(settingsMsg)
    rospy.spin()

    print "Done"

if __name__ == "__main__":
    setupRidgeback()
