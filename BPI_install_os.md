# Banana pi Install Ubuntu  
### Windows  
1. Format SD card  
2. Download Ubuntu Desktop 16.04  
google drive: https://drive.google.com/file/d/1YzdkY8i-IsXzXLkbPCPNbAuhYbHmUwgv/view  
  
3. Win32 Diskimager from: http://sourceforge.net/projects/win32diskimager/files/Archive/  
  
### Ubuntu  
1. Check the SD card node.  
```bash
sudo fdisk -l
```
2. Delete all existing partitions on the SD card.  
Use the o command to delete all partitions on the SD card and then use the n command to add one new partition and use the w command to save the changes.  
```bash
sudo fdisk /dev/sdx
```
3. Format all the partitions of SD card as FAT32.  
```bash
sudo mkfs.vfat /dev/sdxx
```
(x should be replaced according to your SD card node as determined in the first step above)  
You can also skip this step because the write image command dd in Linux will format the SD card automatically.  
  
4. Unzip the download file to get the OS image (.img)  
```
unzip [path]/[downloaded filename]
```
If the filename extension is .tgz, run the following command.  
```
tar -zxvf [path]/[downloaded filename]
```
Ensure that neither the file name of the image you're using nor the path contain any spaces (or other odd characters for that matter).  
5. Write the image file to the SD card.  
Check the SD card node.  
```
sudo fdisk -l
```
(Optional step) Verify if the hash key of the zip file is the same as shown on the downloads page.  
```
sha1sum [path]/[imagename]
```
This will print out a long hex number which should match the "SHA-1" line for the SD image you have downloaded.  
6. Unmount all the partitions of the the SD card  
```
umount /dev/sdxx
```
7. Write the image file to SD card.  
```
sudo dd bs=4M if=[path]/[imagename] of=/dev/sdx
```
Wait patiently to successfully complete the writing process. Please note that the block size set to 4M will work most of the time - if not, please try 1M, although 1M will take considerably longer. You can use the command below to check progress.  
```
sudo pkill -USR1 -n -x dd
```
  
resource:  
http://wiki.banana-pi.org/Banana_Pi_BPI-M64  
http://wiki.lemaker.org/BananaPro/Pi:SD_card_installation  
