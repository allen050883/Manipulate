Case 1:  
MSI AORUS X299X Master(不支援x系列 24 lane) + Intel i9-10920X(48 lane)  
1. M2 SATA SSD不支援(只支援中間)，換成M2 PCIE SSD才可以。但是也無法做BIOS raid，可能是需要Intel SSD  
(補充BIOS raid跟linux raid依舊是不好的，還是需要做硬raid)  
2. 板子有個VROC(可以拿來做raid，但需額外購買;不買的話，還是可以做raid 0)  
3. 板子設定螺絲起子對reset pin角做短路
4. RAM 48G請買 8G 6條，不要買 16G 3條  
5. linux要做raid，只用server版來做，不能用desktop版來做。server做完上desktop(apt-get install ubuntu-desktop)
6. 裝完enthernet和wifi介面會壞掉，(ethernet修法https://forum.linuxconfig.org/t/wired-unmanaged-ubuntu-desktop-issue/1574/2)
7. wifi是Intel出的，幾乎驅動都是給Win10版，並且型號需要自己猜，完全不推薦Intel Wifi 6  
結論:  
1. 下次可以找raid卡來試玩，不然就是要請廠商確保板子可以做raid(SSD、CPU都要相容)  
2. 可以換ASUS產品  
