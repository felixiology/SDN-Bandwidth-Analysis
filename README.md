Bandwidth Measurement and Analysis in SDN (using POX)

Problem Statement: The objective is to measure and compare network throughput (bandwidth) across different network configurations using a POX controller and Mininet. You are specifically analyzing how adding switches and setting link constraints affects performance.

Setup and Execution  
1. POX Controller Setup:
./pox.py forwarding.l2_learning
2. Mininet with custom topology:
sudo mn --custom bandwidth_test.py --topo mytopo,scenario=2 --controller remote --link tc.
3. Perform measurement: iperf h1 h2

Expected Output	

A. Connectivity (Functional Correctness)
•	Expected: All hosts should be able to reach each other via the POX controller.
•	Actual: pingall resulted in "0% dropped (2/2 received)".
•	Observation: This proves the controller is successfully handling packet_in events and installing flow rules.

B. Performance Analysis
•	Expected: Scenario 1 (Default/Single Switch) should have very high bandwidth. Scenario 2 (Two Switches with 10Mbps link) should be restricted to ~10Mbps.
•	Actual: Scenario 1 gave ~33 Gbps, while Scenario 2 gave ~9.5 Mbps.
•	Observation: This demonstrates that the TCLink parameter effectively enforced the bandwidth limits on the bottleneck link.




 
