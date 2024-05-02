# 本篇說明如何製作外網連進內網  
  
## 路由器挑選  
1. 以ASUS為例，需要有 "虛擬伺服器" 功能
參考：https://www.asus.com/tw/support/FAQ/1037906/  
  
2. 別的品牌有類似功能會再新增  
  



## 情境1
描述：從家裡透過ssh連線到公司內部作業，記得要跟主管或MIS說  
型號：ASUS RT-N66U(目前已停產)  
已知：公司有兩組外部IP(應為ADSL)  
設定方法：  
1. 連接方式：外部網路(WAN, 59.XXX.XXX.XXX) --> ASUS RT-N66U(192.168.1.X) --> 內網(LAN, 192.168.1.X)  
這樣的連接方式在底下只有一層，ASUS router並沒有再另外建NAT的網路，因此可以直接在虛擬伺服器直接做port轉發  
2. 檢查：ASUS的網路拓樸會在一開始寫著，外部網路WAN是直接連接到的  
  
## 情境2
描述：從家裡透過ssh連線到咖啡廳內部作業，記得要鎖密碼輸入功能  
型號：ASUS RT-AC1500G Plus  
已知：有一組外部IP(為PPPOE撥接發方法)  
設定方法：  
1. 設備觀察：中華電信提供小烏龜，其中插電後只有看到電話線，無法替換成ASUS router的方法做連接  
2. 去內網登入小烏龜來看，是PPPOE的撥號方式，因此需要將登入中華電信的帳密記錄起來，等等在ASUS router需要一樣透過PPPOE的方式撥接  
3. 連接方式：小烏龜(WAN, 219.XXX.XXX.XXX) --> ASUS RT-N66U(192.168.1.X) --> 內網(LAN, 192.168.50.X)  
此時ASUS router不能利用AP(access point)的方法去做延伸，雖然網路就不會多一層NAT的架構(不會有192.168.50.X)，但是無法利用"虛擬伺服器"的功能  
4. 直接利用ASUS router透過PPPOE的方式做撥接，此時網路拓樸上就不會看到原本的(192.168.1.XXX)，而是會顯示(219.XXX.XXX.XXX)
5. 一樣將虛擬伺服器設定好就可轉發了
  
## 注意  
以上方法需要再登入的時候將密碼輸入的直接鎖住，可以先利用ssh-copy-id存取金鑰  
```
sudo vi /etc/ssh/sshd_config
將
PasswordAuthentication no

重新啟動網路
sudo netplan apply
sudo systemctl restart NetworkManager.service
sudo service network-manager restart
```
  
  
  
## 重要知識補充  
## 針對台灣地區目前的上網類型，主要有3大類型： 
第一種類型：PPPOE(帳號密碼)類型：又細分為2種類別  
a.非固定制：浮動真實ip位址，共有8個浮動真實ip可使用。例：中華電信「用戶帳號」：89841254@hinet.net  
b.固定制：共有1個固定真實IP，7個浮動真實IP，共8個真實ip位址可使用。例：中華電信「用戶帳號」：89841254@ ip.hinet.net  
   
第二種類型：DHCP類型：適用於下列這3種來源方式：  
a.第四台Cable Modem網路業者(例如：東森、凱擘)  
b.社區網路  
c.串接在另一台路由器(IP分享器)底下  
  
第三種類型：固定IP類型：
若您是申請固定IP ADSL的使用者（靜態IP Address），也就是說您向ISP（寬頻網路廠商）申請的寬頻是固定真實IP位址，並且寬頻網路廠商提供您所有的廣域網路端IP位址的資訊：包含IP位址（IP Address）、子網路遮罩（Subnet Mask）、通訊閘（Gateway）、以及DNS伺服器位址。  
例：中華電信可申請3組固定真實ip位址  
