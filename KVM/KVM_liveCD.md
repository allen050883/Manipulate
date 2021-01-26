# USE ubuntu 18.04 to install the system, VNC port  
```
qemu-img create -f qcow2 XXX.qcow2 128G
qemu-img info XXX.qcow2
```
# Install  
```
virt-install --connect qemu:///system --virt-type kvm --name XXX --ram 4096 --vcpus=2 --os-type linux --os-variant ubuntu18.04 --disk  path=$HOME/kvm/XXX/XXX.qcow2,device=disk --cdrom $HOME/ubuntu-18.04.4-live-server-amd64.iso --network network=host-bridge,model=virtio --graphics vnc,listen=0.0.0.0,password=1234 --noautoconsole
```
# Find VNC port (default 5900)  
```
virsh vncdisplay XXX
netstat -lntp | grep IP
```
