---
# User change
title: "Create a Linux Super User"

weight: 4

# Do not modify these elements
layout: "learningpathall"
---

On the NXP board, create a non-root super user (if you do not already have one):

1. While [logged in as root]( {{< relref "2-boot-nxp.md" >}} ):

   * Enable super user privileges:
     ```bash
     sudo visudo
     ```
   * In the vi editor that opens up, uncomment the below line:  
     ```bash { output_lines = "1" }
     %wheel ALL=(ALL:ALL) ALL # uncomment this line
     ```

2. Add a super user:
   ```bash
   sudo adduser testuser
   sudo usermod -aG wheel testuser
   ```

3. While still logged in as root, confirm successful super user creation:
   ```bash
   su - testuser 
   sudo whoami # should return "root"
   ```

4. Log out of the NXP board and log back in to Linux as the super user