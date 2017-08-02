<div class="wiki-content">
<h4>
========================== THIS REPOSITORY IS DEPRECATED! ===========================<br>
========== PLEASE USE AN EXAMPLE CONFIGURATION FROM THE OPTIONS BELOW ===========<br>
<br>
== RIDGEBACK - https://github.com/autonomyresearchkit/ridgeback_cpr_ark_navigation ==<br>
====== HUSKY - https://github.com/autonomyresearchkit/husky_cpr_ark_navigation ======<br>
<br>
</h4>
<h3> About the ark_robot_configurations tool: </h3> <p> This tool allows you to easily set
up the Clearpath Robotics' ARK for use with your robot. This tool uses a ROS Message sent over the network to the ARK
to configure its autonomous navigation settings. The rest of the readme will be an instructional tutorial on how to
make your robot compatible.</p> <h3>Making your robot compatible with the Clearpath Robotics ARK (Autonomy Research
Kit) </h3> <ol> <li>(Optional). Fork this repository for making a pull request later with your changes</li>  <li>Determining your variables</li> <li>Configuring the ARK via a ROS message</li>
<li>(Optional) Sharing your robot configuration</li> <li>Done! Check out our knowledge base for more information on
how to utilize the ARK, the ARK API, and how to purchase an ARK.</li> </ol>

<h3>Determining your variables</h3>
<h3>Configuring the ARK via YAML</h3>
Take a template .yaml file from the templates/example.yaml file. Use the above instructions (Determining your variables) to find proper values to fill in. Some of them are straight forward, and others will require using the documentation provided in this README.md to configure your robot.

<p>Run the configuration script while connected to your ARK:</p>
<pre>./ark-v1.0-configure.py ../ark-v1.0-configurations/your_robot.yaml</pre>

<h3>Verifying it was set:</h3> <p>Status and information response from:
/ark_config_settings_response</p></div>

<h3>Sharing your robot configuration</h3>
<p>To make your robot configuration available for other users, add your YAML file to the ark-v1.0-configurations directory and make a pull request to the http://github.com/autonomyresearchkit/ark_robot_configurations repository
