 from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class LinuxRouter(Node):
    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()

class NetworkTopo(Topo):
    def build(self, **_opts):
        # ROUTERS
        r1 = self.addHost('r1', cls=LinuxRouter, ip='192.168.0.1/24')
        r2 = self.addHost('r2', cls=LinuxRouter, ip='192.168.1.1/24')
        r3 = self.addHost('r3', cls=LinuxRouter, ip='192.168.2.1/24')
        
        # SWITCHES para el R1
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        
        # SWITCHES para el R2
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        s9 = self.addSwitch('s9')
        s10 = self.addSwitch('s10')
        
        # SWITCHES para el R3
        s11 = self.addSwitch('s11')
        s12 = self.addSwitch('s12')
        s13 = self.addSwitch('s13')
        s14 = self.addSwitch('s14')
        s15 = self.addSwitch('s15')
        s16 = self.addSwitch('s16')
        s17 = self.addSwitch('s17')
        s18 = self.addSwitch('s18')

        # ENLACES de los SWITCHES a los ROUTERS
        self.addLink(s1, r1, intfName2='r1-eth1', params2={'ip': '192.168.0.1/24'})
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s1, s4)
        self.addLink(s2, s5)
        self.addLink(s3, s6)
        
        self.addLink(s7, r2, intfName2='r2-eth1', params2={'ip': '192.168.1.1/24'})
        self.addLink(s7, s8)
        self.addLink(s7, s9)
        self.addLink(s8, s10)
        self.addLink(s9, s11)
        
        self.addLink(s12, r3, intfName2='r3-eth1', params2={'ip': '192.168.2.1/24'})
        self.addLink(s12, s13)
        self.addLink(s12, s14)
        self.addLink(s12, s15)
        self.addLink(s13, s16)
        self.addLink(s14, s17)
        self.addLink(s15, s18)

        # ENLACES de los ROUTERS entre sí
        self.addLink(r1, r2, intfName1='r1-eth2', intfName2='r2-eth2', params1={'ip': '10.0.0.1/24'}, params2={'ip': '10.0.0.2/24'})
        self.addLink(r2, r3, intfName1='r2-eth3', intfName2='r3-eth2', params1={'ip': '11.0.0.1/24'}, params2={'ip': '11.0.0.2/24'})

        # CREAR LOS HOSTS PARA CADA ROUTER O SUCURSAL
        # ROUTER 1
        h1 = self.addHost(name='h1', ip='192.168.0.10/24', defaultRoute='via 192.168.0.1')
        h2 = self.addHost(name='h2', ip='192.168.0.11/24', defaultRoute='via 192.168.0.1')
        h3 = self.addHost(name='h3', ip='192.168.0.12/24', defaultRoute='via 192.168.0.1')
        
        # ROUTER 2
        h4 = self.addHost(name='h4', ip='192.168.1.10/24', defaultRoute='via 192.168.1.1')
        h5 = self.addHost(name='h5', ip='192.168.1.11/24', defaultRoute='via 192.168.1.1')
        h6 = self.addHost(name='h6', ip='192.168.1.12/24', defaultRoute='via 192.168.1.1')
        h7 = self.addHost(name='h7', ip='192.168.1.13/24', defaultRoute='via 192.168.1.1')
        
        # ROUTER 3
        h8 = self.addHost(name='h8', ip='192.168.2.10/24', defaultRoute='via 192.168.2.1')
        h9 = self.addHost(name='h9', ip='192.168.2.11/24', defaultRoute='via 192.168.2.1')
        h10 = self.addHost(name='h10', ip='192.168.2.12/24', defaultRoute='via 192.168.2.1')
        h11 = self.addHost(name='h11', ip='192.168.2.13/24', defaultRoute='via 192.168.2.1')
        h12 = self.addHost(name='h12', ip='192.168.2.14/24', defaultRoute='via 192.168.2.1')
        h13 = self.addHost(name='h13', ip='192.168.2.15/24', defaultRoute='via 192.168.2.1')

        # ASIGNAR LOS HOSTS A LOS SWITCH
        # ROUTER A
        self.addLink(h1, s5, intfName2='s5-eth3')
        self.addLink(h2, s6, intfName2='s6-eth3')
        self.addLink(h3, s4, intfName2='s4-eth3')
        
        # ROUTER B
        self.addLink(h4, s10, intfName2='s10-eth3')
        self.addLink(h5, s10, intfName2='s10-eth4')
        self.addLink(h6, s11, intfName2='s11-eth3')
        self.addLink(h7, s11, intfName2='s11-eth4')
        
        # ROUTER C
        self.addLink(h8, s16, intfName2='s16-eth3')
        self.addLink(h9, s16, intfName2='s16-eth4')
        self.addLink(h10, s17, intfName2='s17-eth3')
        self.addLink(h11, s17, intfName2='s17-eth4')
        self.addLink(h12, s18, intfName2='s18-eth3')
        self.addLink(h13, s18, intfName2='s18-eth4')

def run():
    topo = NetworkTopo()
    net = Mininet(topo=topo)
    
    net['r1'].cmd("ip route add 192.168.1.0/24 via 10.0.0.2 dev r1-eth2")
    net['r1'].cmd("ip route add 192.168.2.0/24 via 11.0.0.2 dev r1-eth3")
    
    # Configurar el enrutamiento para el Router B (r2)
    net['r2'].cmd("ip route add 192.168.0.0/24 via 10.0.0.1 dev r2-eth2")
    net['r2'].cmd("ip route add 192.168.2.0/24 via 11.0.0.2 dev r2-eth3")
    
    # Configurar el enrutamiento para el Router C (r3)
    net['r3'].cmd("ip route add 192.168.0.0/24 via 10.0.0.1 dev r3-eth2")
    net['r3'].cmd("ip route add 192.168.1.0/24 via 11.0.0.1 dev r3-eth3")

    net.start()
    CLI(net)
    net.stop()

if _name_ == '_main_':
    setLogLevel('info')
    run()
