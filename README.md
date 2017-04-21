<p>tl;dr To configure the ark, run:</p>
<pre>./ark-v1.0-configure.py ../ark-v1.0-configurations/ridgeback.yaml</pre>

<div class="wiki-content"> <h3> about the ark_robot_configurations tool: </h3> <p> This tool allows you to easily set 
up the Clearpath Robotics' ARK for use with your robot. This tool uses a ROS Message sent over the network to the ARK 
to configure its autonomous navigation settings. The rest of the readme will be an instructional tutorial on how to 
make your robot compatible.</p> <h3>Making your robot compatible with the Clearpath Robotics ARK (Autonomy Research 
Kit) </h3> <ol> <li>(Optional). Fork this repository for making a pull request later with your changes</li>  <li>Determining your variables</li> <li>Configuring the ARK via a ROS message</li> 
<li>(Optional) Sharing your robot configuration</li> <li>Done! Check out our knowledge base for more information on 
how to utilize the ARK, the ARK API, and how to purchase an ARK.</li> </ol>

<h3>Determining your variables</h3> 
<h3>Configuring the ARK via YAML</h3> 
<h3>Sharing your robot 
configuration</h3> <p>To make your robot configuration available for other users, add your YAML file to the ark-v1.0-configurations directory and make a pull request to the http://github.com/autonomyresearchkit/ark_robot_configurations repository 

<h3> ROS Message Definition: </h3> 
<table>
  <tr>
    <th>ArkConfigSettingsCall.msg</th>
  </tr>
  <tr>
  <td>double max_fwd_velocity</td>
  </tr>
  <tr>
    <td>double max_rev_velocity</td>
  </tr>
  <tr>
    <td>double min_fwd_velocity</td>
  </tr>
  <tr>
    <td>double max_accel</td>
  </tr>
  <tr>
    <td>double max_decel</td>
  </tr>
  <tr>
    <td>double max_ang_velocity</td>
  </tr>
  <tr>
    <td>double max_ang_accel</td>
  </tr>
  <tr>
    <td>double max_lateral_accel</td>
  </tr>
  <tr>
    <td>double vehicle_length</td>
    </tr>
  <tr>
    <td>double vehicle_width</td>
  </tr>
  <tr>
    <td>double stopping_distance_1M</td>
  </tr>
  <tr>
  <td>double lidar_spacing</td>
  </tr>
  <tr>
    <td>double laser_fov</td>
  </tr>
  <tr>
    <td>int8_t vehicle_gear</td>
  </tr>
  <tr>
    <td>int8_t curve_type</td>
  </tr>
  <tr>
    <td>double goal_threshold</td>
  </tr>
  <tr>
    <td>double orientation_corr_threshold</td>
   
  </tr>
  <tr>
    <td>double mpc_horizon</td>
    
  </tr>
  <tr>
    <td>double min_lookahead</td>
  
  </tr>
  <tr>
    <td>double max_lookahead</td>
   
  </tr>
  <tr>
    <td>double horizon_percent_change</td>
   
  </tr>
  <tr>
    <td>double lookahead_smoother</td>
   
  </tr>
  <tr>
    <td>double lookahead_factor</td>
   
  </tr>
  <tr>
    <td>double curvature_slowdown</td>
  
  </tr> </table> <h3> Variable Meanings and Effects </h3> <table> <tbody> <tr> <th>Setting</th> <th>Info</th></tr> 
<tr> <td>max_fwd_velocity</td> <td>[m/s]</td></tr> <tr> <td>max_rev_velocity</td> <td>[m/s]</td></tr> <tr> 
<td>min_fwd_velocity</td> <td>[m/s]</td></tr> <tr> <td>max_accel</td> <td>[m/s^2]</td></tr> <tr> <td>max_decel</td> 
<td>[m/s^2]</td></tr> <tr> <td>max_ang_velocity</td> <td>[rad/s]</td></tr> <tr> <td>max_ang_accel</td> 
<td>[rad/s^2]</td></tr> <tr> <td>max_lateral_accel</td> <td>[m/s^2] Max lateral accel during curves. Affects 
velocity.</td></tr> <tr> <td>vehicle_length</td> <td>[m]</td></tr> <tr> <td>vehicle_width</td> <td>[m]</td></tr> <tr> 
<td>stopping_distance_1M</td> <td>[m] - Stopping distance when traveling 1m/s</td></tr> <tr> <td>lidar_spacing</td> 
<td>[m] - spacing between the lidar</td></tr> <tr> <td>laser_fov</td> <td>[deg]</td></tr> <tr> <td>vehicle_gear</td> 
<td>0 &ndash; Mixed, 1 - Forward Only, 2 - Backward only.</td></tr> <tr> <td>curve_type</td> <td>0 &ndash; Linear, 1 
&ndash; Curves.</td></tr> <tr> <td>goal_threshold</td> <td>[m] - How close to the goal for 
&quot;success&quot;</td></tr> <tr> <td>orientation_corr_threshold</td> <td>[rad] - How close to goal orientation for 
&quot;success&quot;</td></tr> <tr> <td>mpc_horizon</td> <td>The predicition horizon [s].</td></tr> <tr> 
<td>min_lookahead</td> <td>Minimum distance [in path parameter] ahead of the robot to do tracking and collision 
checks.</td></tr> <tr> <td>max_lookahead</td> <td>Maximum distance [in path parameter] ahead of the robot to do 
tracking and collision checks.</td></tr> <tr> <td>horizon_percent_change</td> <td>Percentage change when shortening 
the horizon (how quickly do we want to speed up after a curve slowdown).</td></tr> <tr> <td>lookahead_smoother</td> 
<td> <p>Factor between 0 and 1 that determines the smoothness of the change in lookahead distance: 0 means only 
maximum velocity is used to determine the horizon (can be jumpy but but speeds up the robot faster); 1 means only 
averaged planned velocity is used to determine the horizon (smoother but speeds up the robot slowly)</p></td></tr> 
<tr> <td>lookahead_factor</td> <td>How aggressively do we want to increase the lookahead from min_lookahead to 
max_lookahead.</td></tr> <tr> <td>curvature_slowdown</td> <td>Threshold [rad] on path curvature above which to slow 
down the robot.</td></tr></tbody></table> <h3>Verifying it was set:</h3> <p>Status and information response from: 
/ark_config_settings_response</p></div>
