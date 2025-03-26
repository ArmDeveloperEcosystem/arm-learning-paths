---
title: Split into multiple cloud container instances
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### System Architecture and Component Design

Once we understand Safety Island —- the safety-critical subsystem responsible for executing essential control logic in automotive systems—and the DDS (Data Distribution Service) communication mechanism, we can refactor the original OpenAD Kit architecture, which previously ran on a single instance, by splitting it into two independent execution environments.

In the previous [learning path](http://learn.arm.com/learning-paths/automotive/openadkit1_container/), OpenAD Kit launched three containers on the same hardware, each responsible for the `Simulation environment`, `Visualization` and `Planning-Control` components.

In this session, we decouple the simulation and visualization system from the on-vehicle autonomous driving stack, deploying them on two separate Arm-based instances. Communication between the two is facilitated through the ROS 2 software architecture, using DDS as the underlying middleware, which enables real-time data exchange and modular integration across distributed systems.

This architecture brings several practical benefits:

- Improved system stability: Decoupling reduces the risk of resource contention or runtime interference between visualization workloads and safety-critical components.

- Leverages DDS’s QoS and discovery features: Ensures robust, real-time, and scalable communication across nodes without requiring a central broker or manual configuration.

- Better scalability and performance tuning: Each instance can be provisioned with resources optimized for its specific task.

- Supports modular development and CI/CD: Teams can develop, test, and iterate on components independently, enabling better DevOps practices for autonomous systems.


!!! Consider a simple network diagram showing the two EC2s, DDS, and container roles. !!!

### Networking Setting 

First, launch two Arm instances (either cloud instances or on-premise servers).

The specifications of the two Arm instances don’t need to be identical. In my tests, 16 CPUs and 32GB of RAM have already provided good performance.

Once the two machines are up and running, you need to decide where the `Planning-Control` will execute. After making the decision, the other machine will run `Simulation environment` and `Visualization`.

In order for the two instances to communicate, you must configure them to allow network access to each other. For example, in AWS EC2, both instances should belong to the same security group.

In the AWS EC2 Security Groups inbound rules setting, ensure that there is a rule allowing traffic from other members of the same security group (i.e., the security group itself as a source). Outbound traffic is typically allowed by default and usually does not require modification.
This setup ensures that both EC2 instances can discover and communicate with each other over the network as required by ROS 2 and DDS.

Once both of your machines are set up, please note down the IP addresses of both machines, as you will need them for the upcoming configuration.

### New Docker YAML Configur Setting

Ensure that Docker is installed on your development environment, then clone the same repository from the previous learning path onto both machines.

```bash
git clone https://github.com/autowarefoundation/openadkit_demo.autoware.git

cd openadkit_demo.autoware
cp docker/docker-compose.yml docker/docker-compose-2ins.yml
touch docker/cycloneDDS.xml
```

First, you need create xml file called `cycloneDDS.xml`

This CycloneDDS XML configuration file is used to customize the behavior of the CycloneDDS middleware, which is used in ROS2 for inter-process communication (IPC) and network communication over DDS.
Please replace the previously written IP addresses of the two machines with the 192.168.xx.yy and 192.168.aa.bb in the configuration.

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
You can find the more detail about CycloneDDS setting [Configuration](https://cyclonedds.io/docs/cyclonedds/latest/config/config_file_reference.html#cyclonedds-domain-internal-socketreceivebuffersize)
{{% /notice %}}

Next, we need to configure the newly created YML file `docker-compose-2ins.yml`.

- Use the host network instead of the docker network bridge. 
This is necessary for allowing the all of three of containers to access the host network interfaces. 

```YAML
  visualizer:
    network_mode: host
```

- Add the newly created XML file as an environment variable in each container, and mount the current folder as `/root/workspace`.  Configure the environment variable CYCLONEDDS_URI in the docker-compose.yaml file for all containers to ensure they use this configuration file.

```YAML
    volumes:
      - .:/root/workspace
    environment:
      - CYCLONEDDS_URI=/root/workspace/cycloneDDS.xml
```

- Remove the dependency between the `planning-control` and `simulator containers`.
Since these containers will now be launched independently, it is necessary to eliminate the dependency configuration between them.

```YAML
  planning-control:
    depends_on:
      - simulator 
```

Here is the complete XML file:
```YAML
services:
  simulator:
    image: ghcr.io/autowarefoundation/demo-packages:simulator
    container_name: simulator
    network_mode: host
    volumes:
      - ./etc/simulation:/autoware/scenario-sim
      - .:/root/workspace
      - ./log:/root/.ros/log
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
    image: ghcr.io/autowarefoundation/demo-packages:planning-control
    container_name: planning-control
    network_mode: host
    deploy:
    volumes:
      - ./etc/simulation:/autoware/scenario-sim
      - $CONF_FILE:/opt/autoware/share/autoware_launch/config/planning/scenario_planning/lane_driving/behavior_planning/behavior_path_planner/autoware_behavior_path_static_obstacle_avoidance_module/static_obstacle_avoidance.param.yaml
      - $COMMON_FILE:/opt/autoware/share/autoware_launch/config/planning/scenario_planning/common/common.param.yaml
      - .:/root/workspace
      - ./log:/root/.ros/log
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
    image: ghcr.io/autowarefoundation/demo-packages:visualizer
    network_mode: host
    container_name: visualizer
    volumes:
      - ./etc/simulation:/autoware/scenario-sim
      - .:/root/workspace
      - ./log:/root/.ros/log
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

### Network Latency and Performance Optimization

This distributed network architecture may lead to IP packet fragmentation, which can consume system memory under certain network conditions.

To mitigate issues related to IP fragmentation and socket receive buffer limitations, you can tune the network configuration to support heavy UDP load. 

```bash
sudo su
sysctl net.ipv4.ipfrag_time=3
sysctl net.ipv4.ipfrag_high_thresh=134217728 
sysctl -w net.core.rmem_max=2147483647
exit
```

To make the configuration permanent across reboot, modify the create the file `/etc/sysctl.d/10-cyclone-max.conf`:

```bash
sudo su
cat << EOF > /etc/sysctl.d/10-cyclone-max.conf
net.core.rmem_max=2147483647
net.ipv4.ipfrag_time=3
net.ipv4.ipfrag_high_thresh=134217728 # (128 MB)
EOF
exit
```

Reference: 
 - [Autoware dds-setting](https://autowarefoundation.github.io/autoware-documentation/main/installation/additional-settings-for-developers/network-configuration/dds-settings/)
 - [ROS2 documentation](https://docs.ros.org/en/humble/How-To-Guides/DDS-tuning.html#cyclone-dds-tuning)


### Execution

Next, you need to configure the execution commands on the different machines.
Copy the corresponding commands into the `openadkit_demo.autoware/docker` directory of two instances.

{{< tabpane code=true >}}
  {{< tab header="Planning-Control" language="bash">}}
    #!/bin/bash
    # Configure the environment variables
    export SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    export SCRIPT_DIR="$(  pwd )"
    export CONF_FILE_PASS=$SCRIPT_DIR/etc/simulation/config/pass_static_obstacle_avoidance.param.yaml
    export CONF_FILE_FAIL=$SCRIPT_DIR/etc/simulation/config/fail_static_obstacle_avoidance.param.yaml
    export CONF_FILE=$CONF_FILE_FAIL
    export COMMON_FILE=$SCRIPT_DIR/etc/simulation/config/common.param.yaml
    export NGROK_AUTHTOKEN=$NGROK_AUTHTOKEN
    export NGROK_URL=$NGROK_URL
    # Start planning-control
    echo "Running planning v1.."
    CONF_FILE=$CONF_FILE_FAIL docker compose -f "$SCRIPT_DIR/docker-compose-2ins.yml" up planning-control --abort-on-container-exit
  {{< /tab >}}
  {{< tab header="Visualizer & Simulator" language="bash">}}
    #!/bin/bash
    # Configure the environment variables
    export SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    export SCRIPT_DIR="$( pwd )"
    export CONF_FILE_PASS=$SCRIPT_DIR/etc/simulation/config/pass_static_obstacle_avoidance.param.yaml
    export CONF_FILE_FAIL=$SCRIPT_DIR/etc/simulation/config/fail_static_obstacle_avoidance.param.yaml
    export CONF_FILE=$CONF_FILE_FAIL
    export COMMON_FILE=$SCRIPT_DIR/etc/simulation/config/common.param.yaml
    export NGROK_AUTHTOKEN=$NGROK_AUTHTOKEN
    export NGROK_URL=$NGROK_URL

    # Start visualizer and show logs
    docker compose -f "$SCRIPT_DIR/docker-compose.yml" up visualizer -d
    echo "Waiting 10 seconds for visualizer to start..."
    sleep 10
    docker compose -f "$SCRIPT_DIR/docker-compose-2ins.yml" logs visualizer

    # Start  simulator
    echo "Running simulator v1.."
    TIMEOUT=70 CONF_FILE=$CONF_FILE_FAIL docker compose -f "$SCRIPT_DIR/docker-compose-2ins.yml" up simulator --abort-on-container-exit  {{< /tab >}}
{{< /tabpane >}}


Once both machines execute their respective scripts, the visualizer will provide a link that can be accessed through the public IP. When you access the link, you will see that the demo execution will be very similar to the [previous learning path](http://learn.arm.com/learning-paths/automotive/openadkit1_container/4_run_openadkit/). 

The only difference is that the containers are distributed across two physical machines, and at the underlying layer of the demo, there will be frequent packet exchanges.

