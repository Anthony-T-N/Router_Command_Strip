![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Anthony-T-N/Router_Command_Strip)
![Python](https://img.shields.io/badge/python-%3E%3D3-brightgreen.svg)
![version](https://img.shields.io/badge/version-1.0.0-yellow.svg)
![support](https://img.shields.io/badge/OS-Windows-orange.svg)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/Anthony-T-N/Router_Command_Strip)

# Router_Command_Strip
A python script that takes a text file containing a list of commands used to configure routers. The script then strips away unnecessary
parts that prevent the router from accepting the command.

Usage
-
Two text files are generated named as "router.txt" and new_router.txt as the script is executed.

**router.txt file content**
```text
R2(config)# ipv6 unicast-routing
R2(config)# ipv6 router eigrp 1
R2(config-rtr)# eigrp router-id 2.2.2.2
R2(config-rtr)# no shutdown
R2(config-rtr)# exit
R2(config)#
R2(config)# interface lo 0
R2(config-if)# ipv6 eigrp 1                   
R2(config-if)# exit
R2(config)#
R2(config)# interface s0/1/0
R2(config-if)# ipv6 eigrp 1    
R2(config-if)# exit
```
**new_router.txt file content**
```text
ipv6 unicast-routing
ipv6 router eigrp 1
eigrp router-id 2.2.2.2
no shutdown
exit

interface lo 0
ipv6 eigrp 1                   
exit

interface s0/1/0
ipv6 eigrp 1    
exit
```
