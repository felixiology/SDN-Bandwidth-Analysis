from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import TCLink # Allows us to set bandwidth limits

class MyTopo(Topo):
    def build(self, scenario=1):
        # Adding hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        if scenario == 1:
            # Scenario 1: Single Switch (Direct connection)
            s1 = self.addSwitch('s1')
            self.addLink(h1, s1, bw=100) # 100Mbps link
            self.addLink(h2, s1, bw=100)
        else:
            # Scenario 2: Two Switches (Data has to travel further)
            s1 = self.addSwitch('s1')
            s2 = self.addSwitch('s2')
            self.addLink(h1, s1, bw=100)
            self.addLink(s1, s2, bw=50)  # Bottleneck link (50Mbps)
            self.addLink(s2, h2, bw=100)

topos = { 'mytopo': MyTopo }