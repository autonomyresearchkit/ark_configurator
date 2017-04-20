#!/usr/bin/env python

from ark_bridge.msg import ArkConfigSettingsResponse, ArkConfigSettingsCall
import time
import rospy
import yaml
import sys

def response_callback(data):
  global started
  if started:
    print data.information
    rospy.signal_shutdown("Ark Configured")

def configure_ark(yaml_file):

    # Read the yammygang file
    yaml_lib = ""
    with open(yaml_file, 'r') as stream:
        try:
            yaml_lib = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    global started
    started = False
    print "Starting..."

    rospy.init_node("robot_ark_configurator")

    rospy.Subscriber("/ark_bridge/ark_config_settings_response", ArkConfigSettingsResponse, response_callback)
    time.sleep(0.3)
    started = True

    print "Configuring ARK"

    pub = rospy.Publisher("/ark_bridge/ark_config_settings_call", ArkConfigSettingsCall, latch=True, queue_size=1)
    settingsMsg = ArkConfigSettingsCall()

    settingsMsg.max_fwd_velocity = yaml_lib["ark_config"]["max_fwd_velocity"] #[m/s]
    settingsMsg.max_rev_velocity = yaml_lib["ark_config"]["max_rev_velocity"] #[m/s]
    settingsMsg.min_fwd_velocity = yaml_lib["ark_config"]["max_rev_velocity"] #[m/s]
    settingsMsg.max_accel = yaml_lib["ark_config"]["max_accel"]                     #[m/s^2]
    settingsMsg.max_decel = yaml_lib["ark_config"]["max_decel"]       #[m/s^2]
    settingsMsg.max_ang_velocity = yaml_lib["ark_config"]["max_ang_velocity"] #[rad/s]
    settingsMsg.max_ang_accel = yaml_lib["ark_config"]["max_ang_accel"]    #[rad/s^2]
    settingsMsg.max_lateral_accel = yaml_lib["ark_config"]["max_lateral_accel"] #[m/s^2] Max lateral accel during curves. Affects velocity.
    settingsMsg.vehicle_length = yaml_lib["ark_config"]["vehicle_length"]    #[m]
    settingsMsg.vehicle_width = yaml_lib["ark_config"]["vehicle_width"]   #[m]
    settingsMsg.stopping_distance_1M = yaml_lib["ark_config"]["stopping_distance_1M"]	#[m] - Stopping distance when traveling 1m/s
    settingsMsg.lidar_spacing = yaml_lib["ark_config"]["lidar_spacing"] #[m] - spacing between the lidar
    settingsMsg.laser_fov = yaml_lib["ark_config"]["laser_fov"] #[deg]
    settingsMsg.vehicle_gear = yaml_lib["ark_config"]["vehicle_gear"]    #0 - Mixed, 1 - Forward Only, 2 - Backward only.
    settingsMsg.curve_type = yaml_lib["ark_config"]["curve_type"]  #0 - Linear, 1 - Curves.
    settingsMsg.goal_threshold = yaml_lib["ark_config"]["goal_threshold"]		#[m] - How close to the goal for "success"
    settingsMsg.orientation_corr_threshold = yaml_lib["ark_config"]["orientation_corr_threshold"]	#[rad] - How close to goal orientation for "success"
    settingsMsg.mpc_horizon = yaml_lib["ark_config"]["mpc_horizon"]   #The predicition horizon [s].
    settingsMsg.min_lookahead = yaml_lib["ark_config"]["min_lookahead"]#Minimum distance [in path parameter] ahead of the robot to do tracking and collision checks.
    settingsMsg.max_lookahead = yaml_lib["ark_config"]["max_lookahead"] #Maximum distance [in path parameter] ahead of the robot to do tracking and collision checks.
    settingsMsg.horizon_percent_change = yaml_lib["ark_config"]["horizon_percent_change"]   #Percentage change when shortening the horizon (how quickly do we want to speed up after a curve slowdown).
    settingsMsg.lookahead_smoother = yaml_lib["ark_config"]["lookahead_smoother"]    #Factor between 0 and 1 that determines the smoothness of the change in lookahead distance: 0 means only maximum velocity is used to determine the horizon (can be jumpy but speeds up the robot faster); 1 means only averaged planned velocity is used to determine the horizon (smoother but speeds up the robot slowly)
    settingsMsg.lookahead_factor = yaml_lib["ark_config"]["lookahead_factor"]      #How aggressively do we want to increase the lookahead from min_lookahead to max_lookahead.
    settingsMsg.curvature_slowdown = yaml_lib["ark_config"]["curvature_slowdown"]   #Threshold [rad] on path curvature above which to slow down the robot.

    pub.publish(settingsMsg)

    print "Done"

if __name__ == "__main__":
    yaml_file_path = None
    configure_ark(sys.argv[1])
