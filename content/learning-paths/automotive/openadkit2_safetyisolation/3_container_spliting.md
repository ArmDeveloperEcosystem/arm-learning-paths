---
title: Split into multiple cloud container instances
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### System Architecture and Component Design

Now that you’ve explored the concept of a Safety Island -- a dedicated subsystem responsible for executing safety-critical control logic—and learned how DDS (Data Distribution Service) enables real-time, distributed communication, you’ll refactor the original OpenAD Kit architecture into a multi-instance deployment.

In the [previous learning path](http://learn.arm.com/learning-paths/automotive/openadkit1_container/), OpenAD Kit deployed three container components on a single Arm-based instance, handling:
- ***Simulation environment***
- ***Visualization*** 
- ***Planning-Control***

In this session, you will split the simulation and visualization stack from the planning-control logic and deploy them across two independent Arm-based instances. 

These nodes communicate using ROS 2 with DDS as the middleware layer, ensuring low-latency and fault-tolerant data exchange between components.

### Architectural Benefits
This architecture brings several practical benefits:

- ***Enhanced System Stability:*** 
Decoupling components prevents resource contention and ensures that safety-critical functions remain deterministic and responsive.

- ***Real-Time, Scalable Communication:*** 
DDS enables built-in peer discovery and configurable QoS, removing the need for a central broker or manual network setup.

- ***Improved Scalability and Performance Tuning:*** 
Each instance can be tuned based on its workload—e.g., simulation tasks can use GPU-heavy hardware, while planning logic may benefit from CPU-optimized setups.

- ***Support for Modular CI/CD Workflows:*** 
With containerized separation, you can build, test, and deploy each module independently—enabling agile development and faster iteration cycles.

![img1 alt-text#center](aws_example.jpg "Figure 1: Split instance example in AWS")


### Networking Setting 

To begin, launch two Arm-based instances—either as cloud VMs (e.g., AWS EC2) or on-premise Arm servers. 
These instances will independently host your simulation and control workloads.

{{% notice Note %}}
The specifications of the two Arm instances don’t need to be identical. In my tests, 16 CPUs and 32GB of RAM have already provided good performance.
{{% /notice %}}

After provisioning the machines, determine where you want the `Planning-Control` container to run. 
The other instance will host the `Simulation Environment` and `Visualization` components.

To enable ROS 2 and DDS communication between the two nodes, configure network access accordingly. 
If you are using AWS EC2, both instances should be assigned to the same ***Security Group***.

Within the EC2 Security Group settings:
- Add an Inbound Rule that allows all traffic from the same Security Group (i.e., set the source to the group itself).
- Outbound traffic is typically allowed by default and usually does not require changes.

![img2 alt-text#center](security_group.jpg "Figure 2: AWS Security Group Setting")

This configuration allows automatic discovery and peer-to-peer communication between DDS participants across the two instances.

Once both systems are operational, record the private IP addresses of each instance. You will need them when configuring CycloneDDS peer discovery in the next step.

### New Docker YAML Configuration Setting

Before you begin, ensure that Docker is installed on both of your development instances. 
You will also need to clone the demo repository used in the previous learning path.

First, you need clone the demo repo and create xml file called `cycloneDDS.xml`

#### Step 1: Clone the repository and prepare configuration files

```bash
git clone https://github.com/odincodeshen/openadkit_demo.autoware.git

cd openadkit_demo.autoware
cp docker/docker-compose.yml docker/docker-compose-2ins.yml
touch docker/cycloneDDS.xml
```

This will create a duplicate Compose configuration (docker-compose-2ins.yml) and an empty CycloneDDS configuration file to be shared across containers.


#### Step 2: Configure CycloneDDS for Peer-to-Peer Communication

The cycloneDDS.xml file is used to customize how CycloneDDS (the middleware used by ROS 2) discovers and communicates between distributed nodes.

Please copy the following configuration into docker/cycloneDDS.xml on both machines, and replace the IP addresses with the private IPs of each EC2 instance (e.g., 192.168.xx.yy and 192.168.aa.bb):

```xml
<CycloneDDS>
	<Domain>
		<General>
			<AllowMulticast>false</AllowMulticast>
			<Interfaces>
				<NetworkInterface
					autodetermine="false"
					name="ens5"
					priority="default"
					multicast="false"
				/>
			</Interfaces>
		</General>
		<Discovery>
			<MaxAutoParticipantIndex>1000</MaxAutoParticipantIndex>
			<ParticipantIndex>auto</ParticipantIndex>
			<Peers>
				<Peer address="192.168.xx.yy"/>
				<Peer address="192.168.aa.bb"/>
			</Peers>
		</Discovery>
		<Tracing>
			<OutputFile>/root/workspace/cyclonelog.log</OutputFile>
			<Verbosity>config</Verbosity>
		</Tracing>
	</Domain>
</CycloneDDS>
```

{{% notice Note %}}
1. Make sure the network interface name (ens5) matches the one on your EC2 instances. You can verify this using ip -br a.
2. This configuration disables multicast and enables static peer discovery between the two machines using unicast.
3. You can find the more detail about CycloneDDS setting [Configuration](https://cyclonedds.io/docs/cyclonedds/latest/config/config_file_reference.html#cyclonedds-domain-internal-socketreceivebuffersize)
{{% /notice %}}


#### Step 3: Update the Docker Compose Configuration for Multi-Host Deployment

To support running containers across two separate hosts, you’ll need to modify the docker/docker-compose-2ins.yml file. 
This includes removing inter-container dependencies and updating the network and environment configuration.

##### Remove Cross-Container Dependency

Since the planning-control and simulator containers will now run on different machines, you must remove any depends_on references between them to prevent Docker from attempting to start them on the same host.

```YAML
  planning-control:
  # Remove this block
  # depends_on:
  #   - simulator
```

##### Enable Host Networking
All three containers (visualizer, simulator, planning-control) need access to the host’s network interfaces for DDS-based peer discovery. 
Replace Docker’s default bridge network with host networking:

```YAML
  visualizer:
    network_mode: host
```

##### Use CycloneDDS Configuration via Environment Variable

To ensure that each container uses your custom DDS configuration, mount the current working directory and set the CYCLONEDDS_URI environment variable:

```YAML
    volumes:
      - .:/root/workspace
    environment:
      - CYCLONEDDS_URI=/root/workspace/cycloneDDS.xml
```

Add this to every container definition to ensure consistent behavior across the deployment.

Here is the complete XML file:
```YAML
services:
  simulator:
    image: odinlmshen/autoware-simulator:v1.0
    container_name: simulator
    network_mode: host
    volumes:
      - ./etc/simulation:/autoware/scenario-sim
      - .:/root/workspace
    environment:
      - ROS_DOMAIN_ID=88
      - RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
      - CYCLONEDDS_URI=/root/workspace/cycloneDDS.xml
    command: >
      ros2 launch scenario_test_runner scenario_test_runner.launch.py
      record:=false
      scenario:=/autoware/scenario-sim/scenario/yield_maneuver_demo.yaml
      sensor_model:=sample_sensor_kit
      vehicle_model:=sample_vehicle
      initialize_duration:=90
      global_timeout:=$TIMEOUT
      global_frame_rate:=20
      launch_autoware:=false
      launch_rviz:=false

  planning-control:
    image: odinlmshen/autoware-planning-control:v1.0
    container_name: planning-control
    network_mode: host
    deploy:
    volumes:
      - ./etc/simulation:/autoware/scenario-sim
      - $CONF_FILE:/opt/autoware/share/autoware_launch/config/planning/scenario_planning/lane_driving/behavior_planning/behavior_path_planner/autoware_behavior_path_static_obstacle_avoidance_module/static_obstacle_avoidance.param.yaml
      - $COMMON_FILE:/opt/autoware/share/autoware_launch/config/planning/scenario_planning/common/common.param.yaml
      - .:/root/workspace
    environment:
      - ROS_DOMAIN_ID=88
      - RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
      - CYCLONEDDS_URI=/root/workspace/cycloneDDS.xml
    command: >
      ros2 launch autoware_launch planning_simulator.launch.xml
      map_path:=/autoware/scenario-sim/map
      vehicle_model:=sample_vehicle
      sensor_model:=sample_sensor_kit
      scenario_simulation:=true
      rviz:=false
      perception/enable_traffic_light:=false

  visualizer:
    image: odinlmshen/autoware-visualizer:v1.0
    network_mode: host
    container_name: visualizer
    volumes:
      - ./etc/simulation:/autoware/scenario-sim
      - .:/root/workspace
    ports:
      - 6080:6080
      - 5999:5999
    environment:
      - ROS_DOMAIN_ID=88
      - VNC_ENABLED=true
      - RVIZ_CONFIG=/autoware/scenario-sim/rviz/scenario_simulator.rviz
      - NGROK_AUTHTOKEN=${NGROK_AUTHTOKEN}
      - NGROK_URL=${NGROK_URL}
      - CYCLONEDDS_URI=/root/workspace/cycloneDDS.xml
    command: >-
      sleep infinity
```

Before moving to the next step, make sure that `docker-compose-2ins.yml` and `cycloneDDS.xml` are already present on both instances.

#### Step 4: Optimize Network Settings for DDS Communication

In a distributed DDS setup, `high-frequency UDP traffic` between nodes may lead to  `IP packet fragmentation` or  `buffer overflows`, especially under load. 
These issues can degrade performance or cause unexpected system behavior.


```bash
sudo sysctl net.ipv4.ipfrag_time=3
sudo sysctl net.ipv4.ipfrag_high_thresh=134217728 
sudo sysctl -w net.core.rmem_max=2147483647
```

Explanation of Parameters
- ***net.ipv4.ipfrag_time=3***: Reduces the timeout for holding incomplete IP fragments, helping free up memory more quickly.
- ***net.ipv4.ipfrag_high_thresh=134217728***: Increases the memory threshold for IP fragment buffers to 128 MB, preventing early drops under high load.
- ***net.core.rmem_max=2147483647***: Expands the maximum socket receive buffer size to support high-throughput DDS traffic.

To ensure these settings persist after reboot, create a configuration file under /etc/sysctl.d/:

```bash
sudo bash -c 'cat > /etc/sysctl.d/10-cyclone-max.conf <<EOF
net.core.rmem_max=2147483647
net.ipv4.ipfrag_time=3
net.ipv4.ipfrag_high_thresh=134217728
EOF'
```

Then apply the configuration system-wide:
```bash
sudo sysctl --system
```


Reference: 
 - [Autoware dds-setting](https://autowarefoundation.github.io/autoware-documentation/main/installation/additional-settings-for-developers/network-configuration/dds-settings/)
 - [ROS2 documentation](https://docs.ros.org/en/humble/How-To-Guides/DDS-tuning.html#cyclone-dds-tuning)


#### Step 5: Execution: Launching the Distributed Containers

To start the system, you need to configure and run separate launch commands on each machine.

On each instance, copy the appropriate launch script into the openadkit_demo.autoware/docker directory.

{{< tabpane code=true >}}
  {{< tab header="Planning-Control" language="bash">}}
    !/bin/bash
    # Configure the environment variables
    export SCRIPT_DIR=/home/ubuntu/openadkit_demo.autoware/docker
    CONF_FILE_PASS=$SCRIPT_DIR/etc/simulation/config/pass_static_obstacle_avoidance.param.yaml
    CONF_FILE_FAIL=$SCRIPT_DIR/etc/simulation/config/fail_static_obstacle_avoidance.param.yaml

    export CONF_FILE=$CONF_FILE_FAIL
    export COMMON_FILE=$SCRIPT_DIR/etc/simulation/config/common.param.yaml
    export NGROK_AUTHTOKEN=$NGROK_AUTHTOKEN
    export NGROK_URL=$NGROK_URL

    # Start planning-control
      echo "Running planning v1.."
      TIMEOUT=120 CONF_FILE=$CONF_FILE_PASS docker compose -f "$SCRIPT_DIR/docker-compose-2ins.yml" up planning-control --abort-on-container-exit  {{< /tab >}}
  
  {{< tab header="Visualizer & Simulator" language="bash">}}
    #!/bin/bash
    # Configure the environment variables
    SCRIPT_DIR=/home/ubuntu/openadkit_demo.autoware/docker
    export
    CONF_FILE_FAIL=$SCRIPT_DIR/etc/simulation/config/fail_static_obstacle_avoidance.param.yaml
    export CONF_FILE=$CONF_FILE_FAIL
    export COMMON_FILE=$SCRIPT_DIR/etc/simulation/config/common.param.yaml
    export NGROK_AUTHTOKEN=$NGROK_AUTHTOKEN
    export NGROK_URL=$NGROK_URL
    # Start visualizer and show logs
    docker compose -f "$SCRIPT_DIR/docker-compose-2ins.yml" up visualizer -d
    echo "Waiting 10 seconds for visualizer to start..."
    sleep 10
    docker compose -f "$SCRIPT_DIR/docker-compose-2ins.yml" logs visualizer
    # Start simulator
    echo "Running simulator v1.."
    TIMEOUT=300 CONF_FILE=$CONF_FILE_FAIL docker compose -f "$SCRIPT_DIR/docker-compose-2ins.yml" up simulator --abort-on-container-exit
    TIMEOUT=300 CONF_FILE=$CONF_FILE_FAIL docker compose -f "$SCRIPT_DIR/docker-compose-2ins.yml" up simulator --abort-on-container-exit
    TIMEOUT=300 CONF_FILE=$CONF_FILE_FAIL docker compose -f "$SCRIPT_DIR/docker-compose-2ins.yml" up simulator --abort-on-container-exit
  {{< /tab >}}
{{< /tabpane >}}

Once both machines are running their respective launch scripts, the Visualizer will generate a web-accessible interface using the machine’s public IP address. 
You can open this link in a browser to observe the demo behavior, which will closely resemble the output from the [previous learning path](http://learn.arm.com/learning-paths/automotive/openadkit1_container/4_run_openadkit/). 

![img3 alt-text#center](split_aws_run_15.gif "Figure 4: Simulation")

Unlike the previous setup, the containers are now distributed across two separate instances, allowing for real-time cross-node communication. 
Behind the scenes, this setup demonstrates how DDS handles low-latency, peer-to-peer data exchange in a distributed ROS 2 environment.

To facilitate demonstration and observation, the simulator is configured to run `three times` sequentially, allowing you to validate the DDS communication across multiple execution cycles.


