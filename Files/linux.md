# LINUX by Ifeanyi Omeata

[Back to Personal Page](../README.md)

## UDEMY COURSES

- [ ] [LINUX](https://www.udemy.com/courses/search/?src=ukw&q=linux)

## YOUTUBE

<<<<<<< Updated upstream
- [ ] [Linux Command Line - Entire Tutorial Series](https://www.youtube.com/watch?v=avg65oY7sj4)
- [ ] [**-- LAB --** | Linux Command Line - Entire Tutorial Series](https://github.com/omeatai/Personal/blob/main/Files/linux/01.md)
- [ ] [Linux Security & Administration From Boot Process to Firewalls](https://www.youtube.com/watch?v=_WB3evmgxYA)
- [ ] [**-- LAB --** | Linux Security & Administration From Boot Process to Firewalls](https://github.com/omeatai/Personal/blob/main/Files/linux/02.md)
=======
- [ ] [**-- LAB --** | Linux Command Line - Entire Tutorial Series](#lab-linux-command-line)
- [ ] [**-- LAB --** | Linux Security & Administration From Boot Process to Firewalls](#lab-linux-security)
>>>>>>> Stashed changes

## LINUX COURSES

- [ ] [linuxjourney.com](https://linuxjourney.com/)
- [ ] [Linux for Beginners](https://www.udemy.com/course/linuxforbeginners/)
- [ ] [Complete Linux Training Course to Get Your Dream IT Job 2026](https://www.udemy.com/course/complete-linux-training-course-to-get-your-dream-it-job/)
- [ ] [The Linux Command Line Bootcamp: Beginner To Power User](https://www.udemy.com/course/the-linux-command-line-bootcamp/)
- [ ] [Linux Mastery: Master the Linux Command Line in 11.5 Hours](https://www.udemy.com/course/linux-mastery/)
- [ ] [Linux Administration: The Complete Linux Bootcamp](https://www.udemy.com/course/master-linux-administration/)
- [ ] [CompTIA Linux+ (XK0-006) Complete Course & Exam](https://www.udemy.com/course/comptia-linux/)
- [ ] [Mastering Linux: The Comprehensive Guide](https://www.udemy.com/course/mastering-linux/)

## -- LAB -- | Linux Command Line - Entire Tutorial Series

<a id="lab-linux-command-line"></a>

<details>
  <summary>Linux Command Line - Entire Tutorial Series</summary>

## Introduction

This is the full Frugal Computer Guy command-line series in one video, recorded on Linux Mint MATE (Ubuntu-based). A command is three parts: the command, optional options that usually start with a dash, and an argument such as a file or directory. The same commands work on Red Hat, Ubuntu, and Arch, with small differences in package install and in whether a new user gets a home directory. The terminal is how you talk to the operating system when a server has no desktop. Mint puts Terminal on the panel, the main menu, and System Tools. Ctrl+Shift++ enlarges the window for the current session. A custom profile can keep the font and colors.

## Detailed Explanation

- [x] **Listing files and reading help**
  - `ls` lists the current directory. `ls -l` is the long list. `ls -lah` adds all files, including hidden ones, and human sizes. The first character is `d` for a directory and `-` for a file.
  - Options start with a dash. The argument defaults to the directory you are in.
  - `man` opens the manual. The lesson uses it for `chattr`, `chfn`, `tmux`, and history time formats.
- [x] **Moving around and making files**
  - `cd` changes directory. `.` is the current directory and `..` is the parent. Every directory has those two hidden entries.
  - `touch filename` creates an empty file. Quote a name that contains a space, or the shell treats the second word as another argument. A leading dash in a name can look like an option.
  - `mkdir` creates a directory.
- [x] **Editors and readers**
  - `nano filename` is the easier editor. `vi` is the other one already installed on most systems.
  - `cat file` prints a file. `cat -n` adds line numbers. Tab completes a name. Up arrow repeats the last command. Ctrl+A jumps to the start of the line.
  - `more`, `less`, `head`, and `tail` are the other viewers. `less` pages. The grocery-list file used in later lessons is one the instructor also offered as a download from the series site.
- [x] **Redirect, move, copy, delete**
  - `cat` and `ls` write to standard output. `>` sends that output into a file. The lesson redirects `ls -lh` into a file named `output`.
  - `mv` moves or renames. `cp` copies. A second name such as `error-copy` is a new file, not a flag.
  - `rm` deletes a file. `rm -r` (upper or lower R) deletes a directory tree. An incomplete command that is not finished does nothing if you press Enter too early.
- [x] **Links and inodes**
  - The filesystem can run out of inodes even when bytes remain.
  - A hard link is a second name for the same inode. The lesson links `grocerylist.txt` to `grocerylist-link.txt`, then shows both names share an inode with `ls -lh -i`. `cat` reads either name. `rm` or `unlink` removes one name.
- [x] **Root and sudo**
  - Privileged users and ordinary users are different. On this Mint system you prefix one command with `sudo` and type your password. The password is remembered for about 5 to 10 minutes.
  - `ls -lah /root` fails until you add `sudo`. `sudo touch` can create a file in root’s directory.
- [x] **Adding users**
  - `sudo adduser username` is the friendly Ubuntu command. It asks questions and creates a home directory. `ls -lh /home` shows it.
  - `sudo useradd testuseradd` does not ask for a password and does not create a home directory. No output means it worked.
  - Accounts live in `/etc/passwd`. Hashes live in `/etc/shadow`, which you read with `sudo cat /etc/shadow`. The first `$` marks the hash algorithm, then the salt, then the hash. Dates are days since 1 January 1970. The lesson counts 18,321 days for the sample account. The last field is reserved and unused.
- [x] **Changing and locking accounts**
  - `sudo chage -m 14 user` sets the minimum days between password changes. `sudo chage -E` sets an expire date. `sudo chage -l` lists the settings. `chage` does not edit `/etc/passwd`.
  - `getent passwd user` prints the passwd line. `sudo mkdir /users` then `sudo usermod -d /users/user -m user` points the home directory at the new path and moves it.
  - `sudo usermod -c` sets the comment. `sudo apt install finger` installs `finger`. `chfn -h` lists the change-finger options.
  - `sudo usermod -L user` or `passwd -l user` locks the account. A `!` appears in front of the hash in `/etc/shadow`. `passwd -S user` shows status. An uppercase L means locked. `passwd -u user` unlocks. `su - user` switches user.
- [x] **sudoers**
  - A normal user who runs `ls -lh /root` gets permission denied.
  - `sudo visudo` edits the sudoers file. On this Ubuntu-based system the command name contains `vi` but the editor that opens is nano.
- [x] **Permissions, owners, and groups**
  - `chmod` changes mode. Symbolic form does not need a dash: `r` for read and `x` for execute. `chmod 770 chemistry` lets the owner and the group read, write, and execute, and gives others nothing.
  - `groups` lists your groups. `getent group sudo` shows the sudo group. `sudo groupadd team` creates a group. `sudo groupadd deleteme` fails if it exists. `sudo groupdel deleteme` removes it.
  - A group administrator adds a member with `gpasswd -a ryan chemistry` and removes one with `gpasswd -d dan chemistry`. `sudo chgrp chemistry chemistry` sets the directory’s group. `sudo su - brenda` starts a login shell as Brenda. `chown :chemistry file` changes only the group. A period works anywhere a colon works in `chown`.
  - `chown michael:plugdev grocerylist` needs `sudo` when you are not allowed to give the file away.
- [x] **setuid, setgid, and the sticky bit**
  - `which passwd` shows the program. It is setuid root so a normal user can update `/etc/shadow`.
  - Special octal digits: setuid is 4, setgid is 2, sticky is 1, and none is 0.
  - `sudo chmod g+s /srv/chemistry` sets setgid. New files in that directory inherit the chemistry group. `ls -lh` shows a lowercase `s` in the group execute position. `chmod g-s` turns it off.
  - `/tmp` is the usual sticky-bit example. Temporary files there are removed after 10 days or at reboot. `sudo chmod +t /srv/chemistry` sets the sticky bit so users can remove only their own files. `sudo chmod -t` clears it. An uppercase `T` means sticky is on and other does not have execute. `sudo chmod 3770 /srv/chemistry` is sticky (1) plus setgid (2), which is 3, plus mode 770.
- [x] **ACLs and attributes**
  - `getfacl` shows the access list. `sudo setfacl -m g:auditors:rx directory` gives the auditors group read and execute. `sudo setfacl -m u:michael:rwx directory` does the same for one user. The mask can hide write and execute even when the ACL grants them. `setfacl -k` removes default ACL entries.
  - `man chattr` explains attributes. The immutable attribute stops `echo` from changing the file and stops `rm` from deleting it. `sudo chattr -i file` removes that attribute. Attributes are not available on every filesystem.
- [x] **Time and stat**
  - `date` prints local time. `date -u` is UTC. `date -d yesterday`, `date -d tomorrow`, `date -d "two weeks ago"`, and `date -d 12/25/2025` parse other dates.
  - `sudo timedatectl set-time` sets the clock. `sudo timedatectl set-ntp true` turns NTP on. `sudo systemctl status systemd-timesyncd` shows the sync service.
  - `stat file` prints the inode fields that `ls -lh` summarizes, including the octal mode.
- [x] **wc, sort, and uniq**
  - The lesson uses a directory named `LCL`. `wc -l grocerylist` counts lines and does not change the file. `sort` also does not rewrite the file unless you redirect. `sort -u` drops duplicate lines. `sort -f` folds case before comparing. `sort -r` reverses the order.
- [x] **find and grep**
  - `sudo apt install tree` then `tree -a LCL` draws the tree.
  - `find /home/michael/LCL -name image.jpg` searches by name. `find . -mtime -7` is files modified in the last 7 days. `+7` is older than 7 days. Adding `-not` inverts the test.
  - `grep` means global regular expression print. `grep pattern grocerylist` prints matching lines. `grep -E` turns on extended expressions. `.` is one character, `*` repeats, `^` is the start of the line, and a backslash makes a dot literal so `.txt` is not “any character plus txt”. `ls -lh | grep` searches the listing.
- [x] **tr, sed, cut, awk, and xargs**
  - `tr` translates characters and does not take a filename at the end. Feed it with `cat file | tr`. The lesson maps `a` to `@` and `u` to `-`, and uses a range to change case. Extra characters on the left with a shorter right side all become the last character on the right.
  - `sed` is a stream editor. `sed 's/a/@/' grocerylist` substitutes. Without a filename, sed reads the keyboard and edits each line when you press Enter. `\1` and `\2` are the captured groups. `sed -E` drops the backslashes in front of parentheses. `sed -n` turns off the default print so a substituted line is not printed twice.
  - `cut -c 2-10` cuts characters. Cut can also cut bytes or fields. The lesson pipes `ls -lh` through `sed -n '2,$p'` to drop the total line before cutting.
  - `awk` is a small language, often one line. `-F` sets the field separator. `$0` is the whole line. `NF` is the number of fields. A pattern between slashes works like grep. `awk -f script.awk file` runs a script saved in nano. A tab separator is `-F` with a tab.
  - `xargs` turns stdin into arguments. Echo is the default command. `xargs -n 2` puts two words on each command. `xargs -t` prints the command before it runs. The lesson uses it so `wc` receives a filename that was printed by an earlier command.
- [x] **Archives**
  - `gzip file` replaces the file with `file.gz`. `zgrep` searches inside a gzip file. `bzip2` works the same way. `bzgrep` searches `.bz2`. `xz` can be smaller and slower. `xzgrep` searches those files.
  - `tar --create --file=bkup.tar` builds a tarball. `tar -xf bkup-lcl.tar` extracts. `tar -xkf` keeps files that already exist and only restores missing ones.
  - `zip bkup.zip mary.txt findavg.awk` stores named files. `zip -r` includes a directory. `unzip -d zipx_2` extracts into another directory. `less` can show the inside of a zip.
  - `rsync source destination` copies, with more control than `cp`. `rsync -v` is verbose. `rsync -av --dry-run` shows the plan. `--delete` removes destination files that are not in the source. The same command pushes or pulls over SSH. The remote path starts with the same user and host you used to SSH.
- [x] **Scheduling**
  - `systemctl status cron` checks the cron daemon. `crontab -l` lists your table. `crontab -e` edits it. The lesson’s backup is a Monday 3:04 a.m. job. Put the date in the backup and log names so each run keeps its own files. You can paste the command into the shell to test it before it is scheduled.
  - Anacron is for machines that are not on 24 hours. Jobs are hourly, daily, weekly, or monthly, and missed jobs run at startup. The files are under `/etc/cron*`. `ls -lh /etc/cron*` lists them.
  - `sudo apt install at` installs `at`. Ubuntu starts and enables `atd` on install. `systemctl stop atd`, `systemctl status atd`, and `sudo systemctl enable atd` manage it. `at now + 5 minutes` counts from the moment you press Enter, not from when you finish typing the script.
  - A systemd timer needs a script, a `.service`, and a `.timer`. `sudo systemctl daemon-reload` makes systemd notice a new unit. `sudo systemctl start name.service` runs it once. `OnCalendar=Mon *-*-* 13:15` is the lesson’s Monday 1:15 p.m. example. `Persistent=true` runs a missed timer at boot, which is the anacron behavior.
- [x] **Processes, screen, and tmux**
  - `ps` shows your processes. `ps -a` uses the POSIX dash. `ps a` with no dash uses BSD options and the output changes. The last column is the command.
  - `top` is the live view. `m` switches the memory display. `c` toggles the full command line. The lesson warns that pressing `A` or `W` in this version can crash the display when you return.
  - `dd if=/dev/zero of=/dev/null` burns one CPU. Nice values run from `-20` (most CPU) upward. A higher nice value yields the CPU.
  - `kill PID` stops the process from another terminal. Ctrl+C stops it in its own terminal. The lesson’s sample PID for `dd` is 2405.
  - Jobs can be stopped and moved between foreground and background. `+` is the current job and `-` is the next one. `nohup` lets a background command keep running after the terminal closes.
  - `screen -ls` lists sessions. `screen -r` reattaches when there is only one. Ctrl+A is the prefix. `resize -5` shrinks the window by five columns.
  - `tmux` is the other multiplexer. `tmux ls` has no dash before `ls`. `tmux -v` prints the version. `set -g mouse on` and `set -g status-position top` go in the config. `tmux -S /tmp/mysocket` uses a shared socket. `sudo chown michael:lisa /tmp/mysocket` lets Lisa attach.
- [x] **The shell**
  - `alias rm="rm -i"` makes `rm` ask before it deletes. Put the alias in `~/.bashrc` or it disappears. `source` the file, or open a new terminal, to load it.
  - `echo $0` prints `-bash` in an interactive login shell and `bash` without the dash otherwise. `export` passes a variable into a bash subshell.
  - `history -c` clears the in-memory history. `~/.bash_history` is the file on disk. Commands still in memory are not in that file until the shell writes them. `HISTSIZE` and the history time format are in the manual.
  - The prompt itself is configurable. The series changes it in the shell startup file.
- [x] **Disks, filesystems, and encryption**
  - `df` shows free space. The line mounted on `/` is the one that matters. `df -m` is megabytes. `df -h` is the easier human view. `du -a` adds every file. `du` of `*.ext` totals one extension.
  - `/media` is where Mint mounts extra disks and USB drives, often under your username. `/mnt` is for temporary mounts. `find /lib -name '*.so'` shows shared libraries. A symlink shows an arrow in `ls -lh`.
  - Mint auto-mounts a USB stick under `/media`. `sudo umount` removes it. `lsblk` shows the device. Mount at boot by UUID in the filesystem table, filtered with `grep` so you do not pick the wrong disk.
  - The disks GUI unmounts, deletes, and formats partitions. On the command line, `sudo parted` edits the table (it defaults to the first disk if you do not name one). `sudo mkfs.fat -F32` makes FAT32. `sudo e2label /dev/sdb2 part2_ext4` labels ext4. `sudo fdisk -l` lists disks. Unmount every partition on the stick before you repartition it.
  - `dd` copies disks. The default block size in the lesson is the 512-byte sector size from `fdisk -l`. Unmount both the source and the destination before `dd if=` the source `of=` the destination.
  - LVM is physical volumes, volume groups, and logical volumes. Install `lvm2`. `sudo vgcreate Blue /dev/sdb` creates the group and the physical volume. `sudo lvcreate -L` sets a size. `sudo pvs`, `sudo vgs`, `sudo lvs`, and `sudo lvdisplay` inspect them. `sudo lvextend -L +500M /dev/blue/orange` grows a volume. `sudo lvremove` deletes one. RAID 5 in the lesson is `sudo lvcreate --type raid5` with `-n` for the name, `-L` for the size, and `-i` for the number of data disks. LVM keeps about 4 MB per disk for its own metadata. Snapshots are another logical volume you can restore. Ubuntu’s installer has a “Use LVM” choice. The same commands then show the installed layout.
  - ZFS on Ubuntu 22.04 and newer is checked with `zfs version`. `sudo zpool create` builds a pool from a device or from an id under `/dev/disk/by-id` so a renamed `sdb` does not point at the wrong disk. `zpool list` and `zfs list` show them. `sudo zfs create pool/dataset` makes a dataset the ZFS tools understand. A plain `mkdir` inside the pool does not. `zfs snapshot` and `zfs list -t snapshot` manage snapshots. A clone recovers an older snapshot without deleting newer ones. A scrub compares data to checksums. RAIDZ is the ZFS form of RAID 5 (lose one disk). RAIDZ2 can lose two.
  - `sudo apt update` and `sudo apt install smartmontools` install SMART. `sudo smartctl -i /dev/sda` reports whether SMART is available and enabled. `smartd` is the scheduled daemon.
  - LUKS sits on the `dm-crypt` kernel module. `sudo cryptsetup luksFormat` the device, then `mkfs` the mapper device. `sudo cryptsetup luksDump` shows key slots. `sudo cryptsetup luksAddKey` adds another passphrase. The disks GUI lock icon closes the device. The last lesson also installs Mint with LVM so the disk is encrypted against someone who boots another system.

<details>
  <summary>Lab</summary>

## Lab

Use a Linux Mint or Ubuntu virtual machine. The names below are the ones in the series: user `michael`, directory `LCL`, group `chemistry`, volume group `Blue`.

### **Overview**

- [ ] Open a terminal from the Mint panel or from System Tools.
- [ ] You will:
  - [ ] List, create, move, and remove files.
  - [ ] Add a user, lock it, and give it sudo.
  - [ ] Set setgid and the sticky bit on a shared directory.
  - [ ] Search with `find` and `grep`, then schedule one command with cron.
  - [ ] Read disk free space and identify a USB device with `lsblk` before you change it.
- [ ] Success: you can explain command, option, and argument, create a user who can `sudo`, and show a sticky directory where one user cannot delete another user’s file.

### **Task 1: Look around**

- [ ] Enlarge the terminal with Ctrl+Shift++.
- [ ] List the current directory, then the long human listing including hidden names:

```bash
ls
ls -lah
```

- [ ] Open the manual for `ls`, then quit it:

```bash
man ls
```

- [ ] `cd` into `Documents` or your home directory. `cd ..` goes back up. `ls -lah` shows `.` and `..`.

### **Task 2: Create, edit, and remove a file**

- [ ] Make a practice directory and a file whose name contains a space:

```bash
mkdir LCL
cd LCL
touch "new file2.txt"
ls -l
nano "new file2.txt"
```

- [ ] In nano, type one line, save, and exit.
- [ ] Number the lines, then save the listing into a file:

```bash
cat -n "new file2.txt"
ls -lh > output.txt
cat output.txt
```

- [ ] Copy, rename, and delete. `-r` is required for a directory:

```bash
cp output.txt output-copy.txt
mv output-copy.txt ../
rm output.txt
mkdir practice
rm -r practice
```

### **Task 3: Add a user and lock the account**

- [ ] Create the friendly account, then the bare one:

```bash
sudo adduser testadduser
sudo useradd testuseradd
ls -lh /home
getent passwd testuseradd
sudo cat /etc/shadow
```

- [ ] Set a minimum password age, list it, lock the account, and confirm the lock:

```bash
sudo chage -m 14 testadduser
sudo chage -l testadduser
sudo usermod -L testadduser
sudo passwd -S testadduser
sudo passwd -u testadduser
```

- [ ] A locked hash in `/etc/shadow` starts with `!`. `passwd -S` prints `L` while it is locked.
- [ ] Give the new user sudo by running `sudo visudo` and adding that user the same way the original admin is listed. On Mint the editor is nano.

### **Task 4: Share a directory with setgid and a sticky bit**

- [ ] Create the group and the directory, then let the group work there:

```bash
sudo groupadd chemistry
sudo mkdir /srv/chemistry
sudo chgrp chemistry /srv/chemistry
sudo chmod 770 /srv/chemistry
sudo chmod g+s /srv/chemistry
ls -lh /srv
```

- [ ] Add yourself with `gpasswd -a`, switch user with `sudo su -`, and `touch` a file. The file’s group should be chemistry.
- [ ] Turn on the sticky bit so members cannot delete each other’s files, then remove it:

```bash
sudo chmod +t /srv/chemistry
sudo chmod 3770 /srv/chemistry
sudo chmod -t /srv/chemistry
```

- [ ] `3770` is sticky (1) plus setgid (2) in the special digit, then mode 770.

### **Task 5: Find text and schedule it**

- [ ] Install `tree` if the shell offers `sudo apt install tree`, then search:

```bash
tree -a LCL
find . -mtime -7
grep -E 'c' grocerylist.txt
```

- [ ] Use your own file if you do not have `grocerylist.txt`.
- [ ] Confirm cron and edit your table:

```bash
systemctl status cron
crontab -l
crontab -e
```

- [ ] Add one line you have already run by hand, such as a backup of `LCL`. Test the command in the shell before you save the crontab.

### **Task 6: Look at disks without formatting them**

- [ ] Read free space and the device list:

```bash
df -h
lsblk
```

- [ ] Plug in a USB stick you can erase later. `lsblk` shows the new device under `/media`. Unmount it only when you intend to repartition:

```bash
sudo umount /dev/sdb1
```

- [ ] Use the device `lsblk` showed. Do not assume `sdb`. `sudo fdisk -l` lists sizes before any `dd` or `parted` command. Unmount every partition on that stick first.

You can build a file from `touch` and `nano`, add a user, lock and unlock it, share `/srv/chemistry` so members keep their own files, and read `df -h` and `lsblk` before you touch a disk.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

Everyday file commands. Options start with a dash. Quote names that contain spaces.

```bash
ls
ls -l
ls -lah
ls -lh -i
man ls
cd
mkdir LCL
touch "new file2.txt"
nano "new file2.txt"
cat -n "new file2.txt"
ls -lh > output.txt
mv output.txt LCL/
cp output.txt output-copy.txt
rm output-copy.txt
rm -r practice
unlink grocerylist-link.txt
```

Users and privilege. `adduser` asks questions and makes a home directory. `useradd` does not.

```bash
sudo ls -lah /root
sudo adduser testadduser
sudo useradd testuseradd
getent passwd testuseradd
sudo cat /etc/shadow
sudo chage -m 14 testadduser
sudo chage -l testadduser
sudo usermod -d /users/testadduser -m testadduser
sudo usermod -L testadduser
sudo passwd -S testadduser
sudo passwd -u testadduser
sudo visudo
sudo su - brenda
```

Permissions and ACLs.

```bash
groups
getent group sudo
sudo groupadd chemistry
sudo groupdel deleteme
gpasswd -a ryan chemistry
gpasswd -d dan chemistry
sudo chgrp chemistry /srv/chemistry
sudo chmod 770 /srv/chemistry
sudo chmod g+s /srv/chemistry
sudo chmod +t /srv/chemistry
sudo chmod 3770 /srv/chemistry
sudo chmod -t /srv/chemistry
sudo chown michael:plugdev grocerylist.txt
getfacl /srv/chemistry
sudo setfacl -m g:auditors:rx /srv/chemistry
sudo setfacl -k /srv/chemistry
sudo chattr -i file
which passwd
```

Search, text, and archives.

```bash
sudo apt install tree
tree -a LCL
find . -name image.jpg
find . -mtime -7
grep -E '^c' grocerylist.txt
sort -u grocerylist.txt
wc -l grocerylist.txt
date -u
date -d yesterday
stat grocerylist.txt
gzip mary.txt
zgrep lamb mary.txt.gz
tar --create --file=bkup.tar mary.txt
tar -xf bkup-lcl.tar
tar -xkf bkup-lcl.tar
zip -r bkup.zip LCL
unzip -d zipx_2 bkup.zip
rsync -av --dry-run SRC/ DST/
```

Scheduling, processes, and the shell.

```bash
systemctl status cron
crontab -l
crontab -e
sudo apt install at
systemctl status atd
sudo systemctl enable atd
ps
ps a
top
kill 2405
screen -ls
screen -r
tmux ls
tmux -v
alias rm="rm -i"
history -c
echo $0
```

Disks. Replace `sdb` with the device `lsblk` shows. Unmount before `fdisk`, `parted`, or `dd`.

```bash
df -h
du -a LCL
lsblk
sudo umount /dev/sdb1
sudo fdisk -l
sudo apt update
sudo apt install smartmontools
sudo smartctl -i /dev/sda
sudo cryptsetup luksDump /dev/sdb
```

</details>

<details>
  <summary>Code</summary>

## Code

A crontab line is five time fields and then the command. The lesson’s sample backup runs Monday at 3:04 a.m. Test the command in the shell before you put it here.

```text
4 3 * * 1 command-you-already-tested
```

systemd timer calendar from the lesson: every Monday at 13:15, any year, month, and day. `Persistent=true` runs the job at boot if the machine was off.

```text
OnCalendar=Mon *-*-* 13:15
Persistent=true
```

Alias to add to `~/.bashrc`. Open a new terminal or `source` the file before `rm` starts asking.

```bash
alias rm="rm -i"
```

LVM create and grow, using the names from the lesson. The RAID 5 line needs one more disk than `-i` because of parity, and LVM reserves about 4 MB on each disk.

```bash
sudo vgcreate Blue /dev/sdb
sudo lvextend -L +500M /dev/blue/orange
sudo lvcreate --type raid5 -n lv_raid5 -L 2040 -i 2 Blue
```

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What are the three parts of a command?

<details>
<summary>Answer</summary>

- [x] The command name, such as `ls`.
- [x] Options, which usually start with a dash, such as `-lah`.
- [x] An argument, such as a directory. If you omit it, `ls` uses the current directory.

</details>

### Question 2: What do `d` and `-` mean in the first column of `ls -l`?

<details>
<summary>Answer</summary>

- [x] `d` is a directory.
- [x] `-` is a regular file.
- [x] Hidden names start with a dot. `ls -a` shows them. `.` and `..` are in every directory.

</details>

### Question 3: Why quote `touch "new file2.txt"`?

<details>
<summary>Answer</summary>

- [x] The space would split the name into two arguments.
- [x] A name that starts with a dash can be read as an option.
- [x] Extensions such as `.txt` are for you. Linux does not require them.

</details>

### Question 4: How do `adduser` and `useradd` differ on Ubuntu?

<details>
<summary>Answer</summary>

- [x] `sudo adduser` asks questions and creates a home directory.
- [x] `sudo useradd` returns immediately, does not ask for a password, and does not create a home directory.
- [x] Silence from `useradd` means the account was created.

</details>

### Question 5: What does a `!` in `/etc/shadow` mean?

<details>
<summary>Answer</summary>

- [x] The account is locked.
- [x] `sudo usermod -L` or `passwd -l` puts it there.
- [x] `passwd -S` prints `L` for a locked account.
- [x] `passwd -u` unlocks it.

</details>

### Question 6: Why can a normal user run `passwd` if `/etc/shadow` is root’s file?

<details>
<summary>Answer</summary>

- [x] `which passwd` shows the program.
- [x] That program is setuid root.
- [x] The user runs `passwd` with root’s rights long enough to update their own hash.

</details>

### Question 7: What does `chmod 3770` mean on `/srv/chemistry`?

<details>
<summary>Answer</summary>

- [x] The special digit 3 is sticky (1) plus setgid (2).
- [x] `770` lets the owner and the group read, write, and execute. Others have no access.
- [x] Setgid makes new files inherit the directory’s group.
- [x] The sticky bit lets a user delete only their own files.

</details>

### Question 8: What is the difference between `find` and `grep`?

<details>
<summary>Answer</summary>

- [x] `find` searches for files. `-name` matches a name. `-mtime -7` matches files changed in the last 7 days.
- [x] `grep` searches inside files for a regular expression and prints the matching lines.
- [x] `grep -E` uses extended regular expressions.

</details>

### Question 9: Does `sort` change the file?

<details>
<summary>Answer</summary>

- [x] No. `sort` writes the sorted lines to the screen.
- [x] The file stays the same unless you redirect the output yourself.
- [x] `sort -u` hides duplicate lines. `sort -f` ignores case while it compares.

</details>

### Question 10: Why pipe `cat` into `tr` instead of giving `tr` a filename?

<details>
<summary>Answer</summary>

- [x] `tr` does not take the input filename at the end the way `grep` does.
- [x] `cat file | tr` is how the lesson feeds it.
- [x] The lesson maps `a` to `@` and `u` to `-`.

</details>

### Question 11: What does `sed -n` change?

<details>
<summary>Answer</summary>

- [x] Sed prints every line by default, and it prints a substituted line as well.
- [x] `sed -n` turns off that default print.
- [x] You then print only the lines you ask for, so a changed line appears once.

</details>

### Question 12: How is anacron different from cron?

<details>
<summary>Answer</summary>

- [x] Cron runs at a clock time, such as Monday at 3:04 a.m. A machine that is off misses that run.
- [x] Anacron uses hourly, daily, weekly, or monthly, and runs missed jobs at startup.
- [x] `crontab -e` edits your cron table. Anacron’s files are under `/etc`.

</details>

### Question 13: When does `at now + 5 minutes` start counting?

<details>
<summary>Answer</summary>

- [x] From the moment you press Enter on the `at` command.
- [x] Not from the moment you finish typing the script.
- [x] If the script takes longer than five minutes to type, the start time has already passed.

</details>

### Question 14: What is the difference between `ps -a` and `ps a`?

<details>
<summary>Answer</summary>

- [x] `ps -a` uses a POSIX option.
- [x] `ps a` with no dash uses BSD options.
- [x] The two listings are not the same. The last column is still the command that started the process.

</details>

### Question 15: What should you do before `dd` or `fdisk` on a USB stick?

<details>
<summary>Answer</summary>

- [x] Run `lsblk` and use the device that appeared when you plugged the stick in.
- [x] `sudo umount` every partition on that device.
- [x] `sudo fdisk -l` shows the sector size. The lesson’s `dd` default block size is 512 bytes.
- [x] Unmount both the source and the destination before a disk copy.

</details>

### Question 16: What three objects does LVM use?

<details>
<summary>Answer</summary>

- [x] A physical volume, the disk or partition.
- [x] A volume group, such as `Blue`, built with `vgcreate`.
- [x] A logical volume, built with `lvcreate` and grown with `lvextend`.
- [x] `pvs`, `vgs`, and `lvs` list those three layers.

</details>

</details>

## Summary

A command is a name, optional dashed options, and an argument. `ls`, `cd`, `touch`, `mkdir`, `nano`, `cat`, `mv`, `cp`, and `rm -r` cover everyday files. `sudo` runs one command as root and remembers the password for a few minutes. `adduser` is the Ubuntu helper. `useradd` is the bare command. Hashes live in `/etc/shadow`. `chage`, `usermod -L`, and `passwd -S` manage aging and locks. `chmod 3770` is sticky plus setgid plus mode 770. `find` locates files. `grep` locates text. `sort` and `tr` do not rewrite the file unless you redirect. `tar`, `gzip`, `zip`, and `rsync` archive and copy. `crontab -e` schedules a clock time. Anacron and a systemd timer with `Persistent=true` catch machines that were off. `lsblk`, `umount`, and `fdisk -l` come before any partition or `dd` work. LVM is physical volume, volume group, and logical volume. ZFS and LUKS are the later storage and encryption lessons.

## References

- [Linux Command Line - Entire Tutorial Series (YouTube)](https://www.youtube.com/watch?v=avg65oY7sj4)
- [Linux Command Line playlist](https://www.youtube.com/watch?v=JMT5CGFxa_4&list=PLy7Kah3WzqrHPrgkBgwzXyfDDCvthdUfl)
- [Frugal Computer Guy Linux series](https://thefrugalcomputerguy.com/linux/seriespg.php?ser=10020)
- [Local transcript](../course_videos/Linux%20Command%20Line%20-%20Entire%20Tutorial%20Series/Linux%20Command%20Line%20-%20Entire%20Tutorial%20Series.txt)

</details>

## -- LAB -- | Linux Security & Administration From Boot Process to Firewalls

<a id="lab-linux-security"></a>

<details>
  <summary>Linux Security & Administration From Boot Process to Firewalls</summary>

## Introduction

This course is a hands-on walk through hardening a Linux system from the boot path to the firewall. Linux here means the kernel. A distribution is that kernel plus a desktop, GNU tools, and other packages. The lessons use CentOS as a binary match for Red Hat Enterprise Linux, Ubuntu, and Kali for security testing. Hardened servers often have no graphical desktop, so the work is done in the terminal. The same jobs use different commands on Debian-family systems (`apt`) and Red Hat-family systems (`yum`).

## Detailed Explanation

- [x] **What you are securing**
  - Hardening means reducing how an attacker can compromise the operating system and the services on it.
  - The course path is distributions, the boot process, services, logging, intrusion detection, users and permissions, admin utilities, the kernel, then firewalls.
- [x] **Kernel, distribution, and Unix heritage**
  - The kernel schedules the CPU, memory, and disks. Adding a desktop such as KDE, GNOME, or Xfce produces a distribution, not a different kernel.
  - GNU is one contributor among many. The working style comes from Unix, created at AT&T Bell Labs in the late 1960s.
- [x] **Distributions and package families**
  - DistroWatch tracks releases. At the time of the lesson the top entries were Linux Mint, Ubuntu, and Debian. Mint is based on Ubuntu, and Ubuntu is based on Debian. Mint’s Cinnamon and MATE desktops are GNOME-based, but package management stays the Debian `apt` family.
  - Fedora is community-developed and feeds Red Hat Enterprise Linux. Fedora and RHEL use RPM. The lessons treat CentOS as binary-identical to RHEL.
- [x] **Binary packages versus building from source**
  - Binary distributions (Red Hat, Debian, Ubuntu) ship compiled packages and choose the dependencies for you.
  - Source-oriented systems such as Gentoo, and Arch with `pacman`, let you choose dependencies. They take longer to install and teach more about how the system is built.
- [x] **Ubuntu package management with apt**
  - `apt-get install` downloads a package and its dependencies. The demo installs Vim.
  - `apt-get update` refreshes the package index. `apt-get upgrade` then installs newer versions of what is already installed.
  - `apt-cache search` finds a package name when you only remember part of it. The demo searches for Logwatch, installs `fwlogwatch`, then removes it.
  - The same tools apply to Debian, Ubuntu, Linux Mint, and other Debian derivatives.
- [x] **Red Hat package management with yum**
  - YUM is Yellowdog Updater Modified. Unlike installing a bare RPM, `yum` resolves dependencies.
  - `yum search` does not need root. Installing, updating, or removing does. The demo uses `sudo yum install vim-enhanced` (the `.x86_64` suffix is optional).
  - `sudo yum check-update` looks for updates. `yum update` lists them and defaults to **No** when the prompt shows a capital N. `yum update` with a package name limits the update to that package. `yum remove` and `yum erase` do the same removal.
- [x] **From power-on to the boot loader**
  - Power-on self-test checks hardware, then firmware reads the Master Boot Record or the GUID partition table.
  - The MBR is the first 512-byte sector and holds a partition table plus about 440 bytes of boot code. GPT uses a larger boot area.
  - The boot code loads the kernel. It is not the operating system itself. Ubuntu in the demo hides the GRUB menu, then the kernel starts services and a graphical login.
- [x] **Physical access**
  - Anyone who can boot a live CD or USB can bypass account passwords. BIOS or firmware passwords (supervisor, user, and password-on-boot) run before the boot loader.
  - Disk encryption protects a drive that is removed. Locks, racks, and cables slow physical removal. Encryption is covered again later in the course.
- [x] **GRUB configuration**
  - GRUB stage 1 lives in the MBR or the GPT boot area and loads later stages, then the kernel.
  - Older GRUB used `/boot/grub/menu.lst`. Current Ubuntu builds the config from scripts in `/etc/grub.d`.
  - As root, `grub-mkconfig` writes `/boot/grub/grub.cfg`. That file says not to edit it by hand. A menu entry names the kernel under `/boot`, passes a root UUID, often mounts root read-only, and may pass `quiet`. Recovery mode is the same kernel in single-user mode without `quiet`.
  - Edits made in the GRUB menu at boot apply once. They are not written back to the config.
- [x] **GRUB passwords**
  - In `/etc/grub.d` (the header script), the lesson sets a superuser named `me`, a password for that user, and exports the superuser variable. Superusers may edit the menu and boot any entry. Extra users can be limited to specific entries.
  - `update-grub` rebuilds `grub.cfg` from those scripts.
  - A clear-text password in that file is unsafe. `grub-mkpasswd-pbkdf2` prompts for a password and prints a SHA-512 hash to paste back in. Keep a second superuser until the hashed password has been tested, then hash the rest. Run `update-grub` again.
- [x] **LILO**
  - `liloconfig` writes `lilo.conf`. Running `lilo` installs LILO into the MBR. Unlike GRUB, a config change is not picked up until you run `lilo` again.
  - The file sets the boot device, LBA and large-memory options, a boot map, a text or graphical menu, then an `image=` line for a compressed `vmlinuz` kernel, a label, a root UUID, and an initrd. The lesson prefers GRUB and does not replace it.
- [x] **xinetd, the internet super-server**
  - `xinetd` (the newer `inetd`) listens for many small services and starts the real daemon on connection. Per-service files live in `/etc/xinetd.d`. Port numbers come from `/etc/services`.
  - The FTP example is a `stream` (TCP) socket on port 21, user `root`, server `in.ftpd`, with `-l` passed as a server argument. Echo is port 7 TCP and UDP. The main config sets defaults and includes the directory.
- [x] **SysV runlevels**
  - `/etc/rcN.d` links to scripts in `/etc/init.d`. `S` starts a service and `K` stops it. The number in the name sets ASCII order (`K01` before `K09` before `K10`).
  - Runlevel 0 halts, 1 is single user, 6 reboots. Runlevel 2 in the lesson is multi-user. Runlevel 5 is multi-user plus networking plus a graphical login.
  - `/etc/inittab` sets the default runlevel and also handles Ctrl+Alt+Delete and virtual terminals.
- [x] **systemd targets**
  - RHEL 7 and CentOS replace init runlevels with targets under `/etc/systemd`. `graphical.target` matches runlevel 5. `multi-user.target` matches runlevel 3.
  - `systemctl get-default` prints the default. `systemctl isolate graphical.target` or `multi-user.target` switches now without changing the default. `systemctl set-default multi-user.target` changes the boot default.
- [x] **Managing services with systemctl**
  - `systemctl` lists services, devices, and mounts. Units are named like `sshd.service`.
  - `restart`, `status`, `stop`, `start`, `enable`, `disable`, and `is-enabled` replace the old init scripts. `enable` creates the symlink that starts the unit at boot. `status` shows loaded/active, the main PID, and a few log lines.
- [x] **TCP wrappers**
  - TCP wrappers sit in front of services that cannot restrict clients themselves, such as Telnet, FTP, or the old r-commands. They are used with `inetd` or `xinetd`.
  - `/etc/hosts.allow` is the allow list. `/etc/hosts.deny` is the deny list. If a client is in neither file, access is allowed, so a useful policy allows a few clients and denies everyone else.
- [x] **Listening ports**
  - A service is an IP address plus a TCP or UDP port. `/etc/services` maps well-known names. Telnet is TCP 23. Chargen is port 19.
  - `netstat` shows listeners. Piping to `less` pages the list. `-p` adds the program and PID (`sshd` on 22, PostgreSQL, SMTP 25, `rpcbind`). `-a` includes more than listeners. `-n` skips name lookups so you see `22` and `25` instead of `ssh` and `smtp`. A state of `LISTEN` is waiting. `ESTABLISHED` means a connection exists.
- [x] **Mail, web, DNS, and application servers**
  - Postfix is the mail server in the lesson. Set the system name carefully and do not advertise extra version detail to strangers. Greylisting tells an unknown sender to retry. A legitimate server retries. Many spam senders do not. SPF is covered in the same stretch of lessons.
  - Apache config on this Ubuntu system is `/etc/apache2/apache2.conf`, with modular files in `conf-enabled` and sites in `sites-enabled`. `security.conf` includes `ServerTokens`, which controls how much version text Apache sends. A virtual host can bind an address such as `172.30.42.19` and a name such as `www.foo.com`. The browser sends that name in the Host header.
  - DNSSEC in BIND: in `named.conf.options` set `dnssec-enable yes`, `dnssec-validation yes`, and `dnssec-lookaside auto`, then create zone keys.
  - MySQL: set a strong root password, log in so the client prompts for it, and the demo renames the `root` account in `mysql.user` (`user` becomes `newroot` where `user` was `root`) so the default name is gone.
  - PostgreSQL already starts out fairly locked down. `psql` can `CREATE ROLE` a user `WITH LOGIN PASSWORD` and `VALID UNTIL` a date. The demo uses `2016-12-31`.
  - Tomcat 7 is a Java servlet container. Its XML config includes a listener port. JBoss is the other Java application server in the module.
  - `mod_security` is a web application firewall for Apache, installed with a core rule set so attacks that pass the network firewall still get inspected.
  - TLS is preferred over SSL for browser traffic. A real deployment uses a certificate from a company CA or a public vendor rather than a long-lived self-signed cert.
- [x] **Logging**
  - This system uses rsyslog. Local files are under `/var/log`, and logrotate gzips older copies.
  - A syslog line is timestamp (local time), hostname, process name and PID, then the message. Remote logs are separated by hostname. `auth.log` records logins and `sudo`.
  - To ship logs off the box, add rsyslog lines that send facilities to another host and port. The reason is that an attacker who owns the machine can edit local logs. A receive-only syslog host is the copy you trust.
  - To listen, the lesson enables a TCP server and a UDP server on port 514 (`UDP` is the historical syslog transport; TCP is more reliable), restarts rsyslog, and confirms port 514 with `netstat -n`.
  - `logwatch` summarizes logs. `utmp` and `wtmp` record current and historical logins. `last` reads the login log. `last -f` reads an older rotated file.
- [x] **Host integrity and rootkits**
  - Tripwire hashes important files so a later check can show unexpected changes. `twadmin` generates a site key and a local key (each with a passphrase), then builds the binary config and policy from the text files. `tripwire --init` builds the database. `tripwire --check` compares the disk to that database.
  - Samhain and AIDE (`/etc/aide/aide.conf`) are other file-integrity checkers. Prelude is the console that collects IDS alerts.
  - `rkhunter --update` refreshes the signatures, then `rkhunter --check` looks for rootkit strings, suspicious directories, and enabled xinetd services.
- [x] **Snort**
  - `apt-get install snort` pulls the daemon, common files, docs, and the default rules. Set `HOME_NET` and the external network. On Debian and Ubuntu, `/etc/snort/snort.debian.conf` can override variables.
  - Newer Snort writes a binary `snort.log` (Unified2). The lesson also turns syslog and pcap output back on, then restarts Snort. Rules live in the rules directory. PulledPork is named as the updater. A sample web-attacks rule alerts on TCP from the external net to an HTTP server when the URI contains something like `/bin/ps`.
  - Barnyard2 reads `/var/log/snort/snort.log` and can forward alerts. The pcap output opens in Wireshark.
- [x] **Users, passwords, and permissions**
  - `groupadd` creates the primary group. `useradd -g` sets that group, `-d` sets the home directory, `-s /bin/bash` sets the shell, and `-m` creates the home directory.
  - `passwd` with no user, when run via `sudo`, changes root’s password. `passwd newuser` sets that user’s password.
  - `/etc/login.defs` supplies `PASS_MAX_DAYS`, `PASS_MIN_DAYS`, and `PASS_WARN_AGE` for new shadow entries.
  - `/etc/pam.d/common-password` on this Ubuntu host uses `pam_unix` with SHA-512. A `requisite` `pam_cracklib` line, with three retries, requires two digits, two lowercase letters, and two symbols. There is no `system-auth` file on this host, so the line goes in `common-password`.
  - `unshadow` merges passwd and shadow data into a file the lesson calls `password.txt`. `john password.txt` runs John the Ripper on it, and a second run uses the wordlist file named `wordlist`. Incremental mode is the other method he names. The point is to find weak passwords, not to collect them.
  - Unix permissions are three triads: user, group, other. Read is 4, write is 2, execute is 1. `chmod 600 server.key` leaves read and write for the owner only. `chmod g-w` removes group write.
- [x] **AppArmor and SELinux**
  - Discretionary control means the owner can `chmod` their own files. Mandatory control is a system policy the owner cannot override.
  - AppArmor profiles (the demo opens the Freshclam profile) list capabilities such as setuid and setgid, readable paths, and explicit denies. The kernel module enforces them.
  - SELinux on RHEL is on by default. `sestatus` shows enabled and the current mode. Enforcing applies policy. Permissive only logs. `setenforce` changes the mode now. `/etc/selinux/config` sets the boot mode and the type: `targeted`, `minimum`, or `mls`.
  - `ls -Z` shows user, role, and type. Copying `/var/www/html/index.html` into a home directory relabels it to the home type. `chcon -t httpd_sys_content_t` fixes the type for now. `semanage fcontext -a -t httpd_sys_content_t` records the type so a relabel keeps it. `restorecon` puts a file back to the type the policy expects. A `mv` into the web directory keeps the source type, which is why the web file then needs a restore.
- [x] **PAM**
  - Files in `/etc/pam.d` stack modules per program. FTP in the lesson includes `common-auth`, `common-account`, `common-session`, `pam_ftp`, and `pam_listfile`. SSH can use a different stack because those logins are remote.
- [x] **Processes**
  - `top` refreshes CPU, memory, swap, task counts, and three load averages. `q` quits.
  - `ps` shows your processes. `ps -e` shows everyone. `ps -ef` adds a full listing. `ps auxw` is the wide BSD-style listing the instructor uses, often piped to `less` or to `grep`. `grep -v grep` drops the grep line itself.
  - `kill PID` sends the default terminate signal. `kill -9 PID` sends signal 9 when the process ignores that. `killall firefox` signals every process with that name. `killall -9` is the forced version. Killing by name kills every match.
- [x] **Scanners and packet capture**
  - `nmap -sS` is a SYN (half-open) scan: SYN, SYN-ACK, then RST, with no completed handshake. `-v` prints progress. `-T5` is the fastest timing. Default coverage is about the common 1,000 ports. `-p 80` or a list such as `443,1089,8080` limits the scan. `-p-` or `-p 0-65535` scans every port. An OS fingerprint uses Nmap’s database. A `/24` scans the subnet. `-sU` is UDP and is slower because a closed port returns ICMP port unreachable and silence can mean open, filtered, or lost.
  - OpenVAS on Kali is under Vulnerability Analysis, checked with its setup command, and used from the browser on port 9392 as admin. Nexpose is the other vulnerability scanner in the module.
  - `find` is used to search the filesystem for files you need to inspect.
  - `tcpdump` prints packet headers on a console. Filter by host name or IP, pick an interface such as `eth0`, add `-v` or `-vv`, and write a pcap with snap length 0 so the full frame (up to the 1500-byte Ethernet MTU) is saved. Ctrl+C stops the capture. Wireshark is the graphical reader for those files and for Snort pcaps.
  - `lspci` and `lsusb` list PCI and USB hardware.
- [x] **Kernel modules and parameters**
  - A `vmlinuz` image with a `z` in the name is compressed. Modular kernels keep drivers as `.ko` objects under `/lib/modules/<version>/` instead of compiling every driver into one file. The demo looks in `3.16.0-34-generic`.
  - `lsmod` lists loaded modules. `insmod` takes the full path of a `.ko` under `/lib/modules/3.16.0-34-generic/` in the demo, including an HFS module. `rmmod` removes a module by name. A module with nothing to attach to may not stay loaded.
  - `sysctl net.ipv4.ip_forward` reads the forwarding flag. `sysctl -w net.ipv4.ip_forward=0` changes it until reboot. Lasting changes go in `/etc/sysctl.conf`, which is read at boot.
  - Building a kernel needs a compiler, `make`, and the rest of the build tools. After unpacking the source, `make menuconfig` chooses options such as 64-bit versus 32-bit. You can also read the config of the kernel that is already running.
- [x] **iptables**
  - Four built-in tables: `filter` (default; INPUT, OUTPUT, FORWARD), `nat` (PREROUTING, POSTROUTING, OUTPUT), `mangle`, and `raw`. `iptables -t mangle -L` and `iptables -t nat -L` show those tables. Most hosts only need the built-in tables.
  - NAT needs two interfaces and forwarding. The lesson appends a POSTROUTING rule on `eth0` that jumps to MASQUERADE, accepts NEW traffic forwarded from internal `eth1`, and accepts only RELATED,ESTABLISHED traffic coming back in `eth0`. Uncomment the forwarding line in `/etc/sysctl.conf` so it survives reboot.
  - Match with `-p tcp` or `udp`, `--sport`, `--dport`, `--tcp-flags`, `--syn`, ICMP type (8 is echo request), `-s`, and `-d`. The demo destinations include `192.168.1.7` and `172.16.42.42`.
  - Rate limits: one TCP SYN per second, RST-only packets among SYN,ACK,FIN,RST at one per second, and ICMP echo-request at one per second, each jumping to ACCEPT.
  - Connection states are NEW, ESTABLISHED (the firewall has already seen the flow, even before the handshake finishes), RELATED (an FTP data connection tied to an existing control connection), and INVALID (drop or log).
  - `-j ACCEPT` lets the packet through. `-j DROP` discards it with no reply. `-j LOG` writes a syslog line and does not stop processing, so log and drop are two rules.
- [x] **firewalld, ufw, and gufw**
  - firewalld groups rules into zones so a laptop can switch networks without reloading a giant iptables ruleset. `firewall-cmd` shows it is running and lists zones: block, dmz, drop, external, home, internal, public, trusted, and work. It is the RHEL default. On Ubuntu it is optional and replaces ufw if you want it.
  - The firewalld applet edits zones, services, ports, forwarding, masquerade, and interfaces. Runtime changes are memory-only. Permanent changes are stored on disk.
  - ufw is Ubuntu’s uncomplicated front end on iptables. `ufw enable`, `ufw disable`, and `ufw status verbose` control it. `ufw allow 80/tcp` and `ufw deny 8080/tcp` add rules for IPv4 and IPv6. `ufw delete deny 8080/tcp` removes one. `ufw allow ssh` looks up port 22 in `/etc/services`.
  - gufw adds Home, Public, and Office profiles, an on/off switch, and a default of deny inbound and allow outbound. You can add a rule from a listener (the demo uses named) and delete it with the minus button. The status log shows the ufw commands the GUI ran.

<details>
  <summary>Lab</summary>

## Lab

Walk through the course on a disposable virtual machine. CentOS stands in for RHEL. Ubuntu covers `apt`, Apache, and ufw. Do not point scanners or password crackers at systems you do not own.

### **Overview**

- [ ] Install CentOS and Ubuntu in a free hypervisor (VirtualBox or VMware Player) and confirm you can open a terminal without relying on the desktop.
- [ ] You will:
  - [ ] Update packages with `apt` and with `yum`.
  - [ ] Read the boot path and set a GRUB superuser password.
  - [ ] Switch systemd targets and stop or start `sshd`.
  - [ ] Add a user, a password policy, and a file mode.
  - [ ] Check SELinux or AppArmor context on a copied web file.
  - [ ] List listeners, run a SYN scan against your own host, and allow a port in ufw.
- [ ] Success: you can update packages, explain the boot menu password, create a user whose password must be complex, and show a firewall rule that allows only the port you chose.

### **Task 1: Update packages**

- [ ] On Ubuntu:

```bash
sudo apt-get update
sudo apt-get upgrade
apt-cache search logwatch
sudo apt-get install vim
```

- [ ] On CentOS, search does not need root. Install and update do. Accept the update only after you read the list. The default answer is No.

```bash
yum search vim
sudo yum install vim-enhanced
sudo yum check-update
sudo yum update
```

### **Task 2: Protect the boot menu**

- [ ] Set a firmware password so a live USB cannot boot ahead of the hard disk.
- [ ] On Ubuntu, edit the GRUB header script in `/etc/grub.d` as root. Set a superuser and a password, export the superuser variable, then rebuild:

```bash
sudo update-grub
```

- [ ] Replace the clear-text password with the hash from `grub-mkpasswd-pbkdf2`. Keep a second superuser until that hash works at the menu, then run `update-grub` again.
- [ ] Confirm a one-time edit in the GRUB menu (for example adding single-user mode) disappears on the next boot.

### **Task 3: Switch runlevels and services**

- [ ] On the CentOS VM:

```bash
systemctl get-default
sudo systemctl isolate multi-user.target
systemctl get-default
sudo systemctl isolate graphical.target
sudo systemctl set-default multi-user.target
```

- [ ] `isolate` changes the running target only. `set-default` changes the next boot. Set the default back to `graphical.target` if you still want a desktop.
- [ ] Manage SSH:

```bash
systemctl status sshd.service
systemctl is-enabled sshd.service
sudo systemctl restart sshd.service
sudo systemctl stop sshd.service
sudo systemctl start sshd.service
```

### **Task 4: See who is listening**

- [ ] Page through listeners, then show the program and the numeric port:

```bash
netstat -ap | less
netstat -n
```

- [ ] Quit `less` with `q`. Map a name such as `ssh` back to `/etc/services` (TCP 22).

### **Task 5: Add a user and a password policy**

- [ ] Create a group and a user. The names below are the ones in the lesson.

```bash
sudo groupadd newgroup
sudo useradd -g newgroup -d /home/newuser -s /bin/bash -m newuser
sudo passwd newuser
```

- [ ] Do not run `sudo passwd` with no username. That changes the root password.
- [ ] In `/etc/login.defs`, set the maximum days, minimum days, and warning days a password may be used.
- [ ] On Ubuntu, add a `requisite` `pam_cracklib` line to `/etc/pam.d/common-password` with three retries and requirements for two digits, two lowercase letters, and two symbols.
- [ ] On a key file, leave only the owner able to read and write:

```bash
chmod 600 server.key
```

### **Task 6: Put a web file back in the right SELinux type**

- [ ] On the RHEL or CentOS VM:

```bash
sestatus
ls -Z /var/www/html
cp /var/www/html/index.html .
ls -Z index.html
chcon -t httpd_sys_content_t index.html
restorecon index.html
ls -Z index.html
```

- [ ] `chcon` changes the type now. `restorecon` returns the type the policy already expects for that directory. Use `semanage fcontext -a -t httpd_sys_content_t` when the file should keep the web type across a relabel.
- [ ] On Ubuntu, open an AppArmor profile and read which paths that program may read or write. Owners cannot override those rules with `chmod`.

### **Task 7: Scan and firewall your own host**

- [ ] SYN-scan one address you control, then only port 80, then UDP. Stop a whole-subnet scan with Ctrl+C if you only needed the syntax.

```bash
sudo nmap -sS -v 172.30.42.1
sudo nmap -sS -p 80 172.30.42.1
sudo nmap -sU 172.30.42.1
```

- [ ] On Ubuntu, allow HTTP and SSH, deny 8080, then delete the deny rule:

```bash
sudo ufw enable
sudo ufw allow 80/tcp
sudo ufw deny 8080/tcp
sudo ufw status verbose
sudo ufw allow ssh
sudo ufw delete deny 8080/tcp
sudo ufw status verbose
```

- [ ] If you build the NAT example, use two interfaces, `eth0` outside and `eth1` inside. Masquerade POSTROUTING out `eth0`, accept forwarded traffic from `eth1`, and accept only RELATED,ESTABLISHED traffic back in. Persist forwarding by uncommenting `net.ipv4.ip_forward` in `/etc/sysctl.conf`. The kernel-parameter demo sets the live value to 0:

```bash
sysctl net.ipv4.ip_forward
sudo sysctl -w net.ipv4.ip_forward=0
```

You can update packages on both families, lock the GRUB menu with a hashed superuser password, add a user whose password is checked by PAM, restore an SELinux label, and show a ufw rule that allows only the ports you added.

</details>

<details>
  <summary>Terminal Commands</summary>

## Terminal Commands

Debian-family package commands. `update` refreshes the index. `upgrade` installs newer installed packages.

```bash
sudo apt-get update
sudo apt-get upgrade
apt-cache search logwatch
sudo apt-get install vim
sudo apt-get install fwlogwatch
sudo apt-get remove fwlogwatch
sudo apt-get install snort
```

Red Hat-family package commands. Search works without root. A bare `yum update` prompts, and the capital N means the default is No.

```bash
yum search vim
sudo yum install vim-enhanced
sudo yum check-update
sudo yum update
sudo yum update vim-enhanced
sudo yum remove vim-enhanced
sudo yum erase vim-enhanced
```

Boot loader. Rebuild GRUB after editing `/etc/grub.d`. Hash the superuser password before you rely on it.

```bash
sudo grub-mkconfig
sudo update-grub
grub-mkpasswd-pbkdf2
sudo liloconfig
sudo lilo
```

systemd targets and services.

```bash
systemctl get-default
sudo systemctl isolate multi-user.target
sudo systemctl isolate graphical.target
sudo systemctl set-default multi-user.target
systemctl status sshd.service
systemctl is-enabled sshd.service
sudo systemctl restart sshd.service
sudo systemctl enable sshd.service
sudo systemctl disable sshd.service
sudo systemctl stop sshd.service
sudo systemctl start sshd.service
```

Listeners, logins, and processes.

```bash
netstat -ap | less
netstat -n
last
ps
ps -e
ps -ef
ps auxw | less
ps auxw | grep bash | grep -v grep
top
kill 13596
kill -9 17340
killall firefox
killall -9 firefox
```

`13596` and `17340` are the Firefox PIDs from the lesson. Substitute the PID you see. `q` quits `top` and `less`.

Users and permissions.

```bash
sudo groupadd newgroup
sudo useradd -g newgroup -d /home/newuser -s /bin/bash -m newuser
sudo passwd newuser
chmod 600 server.key
chmod g-w server.key
```

SELinux, integrity, and rootkits.

```bash
sestatus
sudo setenforce permissive
ls -Z
chcon -t httpd_sys_content_t index.html
semanage fcontext -a -t httpd_sys_content_t index.html
restorecon index.html
sudo rkhunter --update
sudo rkhunter --check
sudo tripwire --init
sudo tripwire --check
john password.txt
john --wordlist=wordlist password.txt
```

Scanners and capture. Stay on addresses you administer.

```bash
sudo nmap -sS -v 172.30.42.1
sudo nmap -sS -T5 172.30.42.1
sudo nmap -sS -p 80 172.30.42.1
sudo nmap -sS -p- 172.30.42.1
sudo nmap -sU 172.30.42.1
sudo tcpdump -v
sudo tcpdump -vv
```

Kernel parameters and modules.

```bash
sysctl net.ipv4.ip_forward
sudo sysctl -w net.ipv4.ip_forward=0
lsmod
sudo rmmod hfs
make menuconfig
```

Firewalls.

```bash
sudo iptables -t filter -L
sudo iptables -t nat -L
sudo iptables -t mangle -L
sudo ufw enable
sudo ufw disable
sudo ufw status verbose
sudo ufw allow 80/tcp
sudo ufw deny 8080/tcp
sudo ufw delete deny 8080/tcp
sudo ufw allow ssh
```

`firewall-cmd` is how the lesson checks that firewalld is running and lists the zones (block, dmz, drop, external, home, internal, public, trusted, work). The on-screen tool is that command. The exact switches are not dictated in the transcript.

</details>

<details>
  <summary>Code</summary>

## Code

BIND options the lesson turns on for DNSSEC:

```text
dnssec-enable yes;
dnssec-validation yes;
dnssec-lookaside auto;
```

PostgreSQL role with an expiration, as entered in `psql`:

```text
CREATE ROLE myuser WITH LOGIN PASSWORD 'password' VALID UNTIL '2016-12-31';
```

MySQL account rename from the lesson. Run it only after you can still log in as an administrator:

```text
UPDATE mysql.user SET user = 'newroot' WHERE user = 'root';
```

iptables NAT shape from the lesson. `eth0` is outside, `eth1` is inside. Log and drop are separate rules. A `-j LOG` rule does not discard the packet.

```bash
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
iptables -A FORWARD -i eth1 -j ACCEPT
iptables -A FORWARD -i eth0 -o eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A INPUT -p tcp --syn -m limit --limit 1/second -j ACCEPT
iptables -A INPUT -p icmp --icmp-type echo-request -m limit --limit 1/second -j ACCEPT
iptables -A INPUT -m state --state NEW -j ACCEPT
iptables -A INPUT -m state --state ESTABLISHED -j ACCEPT
```

</details>

<details>
  <summary>Questions and Answers</summary>

## Questions and Answers

### Question 1: What is Linux, as opposed to a distribution?

<details>
<summary>Answer</summary>

- [x] Linux is the kernel that sits between hardware and programs.
- [x] A distribution adds a desktop, GNU and other user software, and a package manager.
- [x] Mint, Ubuntu, Debian, Fedora, RHEL, and CentOS are distributions. They are not different kernels.

</details>

### Question 2: Which package commands belong on Ubuntu, and which belong on CentOS?

<details>
<summary>Answer</summary>

- [x] Ubuntu, Debian, and Mint use `apt-get` and `apt-cache`.
- [x] Fedora, RHEL, and CentOS use `yum`, which installs RPM packages and resolves dependencies.
- [x] `yum search` does not need root. `yum install` and `yum update` do.

</details>

### Question 3: What is the difference between `apt-get update` and `apt-get upgrade`?

<details>
<summary>Answer</summary>

- [x] `apt-get update` downloads the list of available package versions.
- [x] `apt-get upgrade` installs newer versions of packages that are already installed.
- [x] Run update before upgrade so the upgrade sees the current index.

</details>

### Question 4: Why can a firmware password matter more than a user password?

<details>
<summary>Answer</summary>

- [x] A person with physical access can boot a live CD or USB and skip account passwords.
- [x] A password-on-boot prompt runs before the boot loader and the operating system.
- [x] Disk encryption is what protects data if the drive is removed.

</details>

### Question 5: Why does the lesson say not to edit `grub.cfg` by hand?

<details>
<summary>Answer</summary>

- [x] `grub-mkconfig` or `update-grub` regenerates `/boot/grub/grub.cfg` from `/etc/grub.d`.
- [x] Hand edits are overwritten the next time that command runs.
- [x] A change typed at the GRUB menu applies to that boot only.

</details>

### Question 6: How do you stop a GRUB superuser password sitting in clear text?

<details>
<summary>Answer</summary>

- [x] Run `grub-mkpasswd-pbkdf2` and paste the SHA-512 hash into the GRUB script.
- [x] Run `update-grub` afterward.
- [x] Keep a second superuser until you have tested the hash at the boot menu.

</details>

### Question 7: Which systemd target matches runlevel 5, and which command changes it only until reboot?

<details>
<summary>Answer</summary>

- [x] `graphical.target` matches runlevel 5.
- [x] `multi-user.target` matches runlevel 3.
- [x] `systemctl isolate` switches now.
- [x] `systemctl set-default` changes the next boot. `get-default` still shows the old target after an isolate.

</details>

### Question 8: What do `/etc/hosts.allow` and `/etc/hosts.deny` do?

<details>
<summary>Answer</summary>

- [x] They are the TCP wrappers policy used with `inetd` or `xinetd`.
- [x] `hosts.allow` is the allow list. `hosts.deny` is the deny list.
- [x] A client that appears in neither file is allowed, so you allow what you need and deny the rest.

</details>

### Question 9: What does `netstat -n` change?

<details>
<summary>Answer</summary>

- [x] It skips service-name and address lookups.
- [x] Port 22 stays `22` instead of `ssh`. Port 25 stays `25` instead of `smtp`.
- [x] `-p` is the separate switch that adds the program and PID.

</details>

### Question 10: Why send syslog to another machine?

<details>
<summary>Answer</summary>

- [x] An attacker who compromises the host can edit or delete local logs.
- [x] rsyslog can keep a local copy and also send facilities to a remote host.
- [x] UDP 514 is the historical syslog port. TCP is more reliable because delivery is acknowledged.
- [x] Trust the copy on the hardened log host when the two copies disagree.

</details>

### Question 11: What does `passwd` do when you run it with `sudo` and no username?

<details>
<summary>Answer</summary>

- [x] It changes the root password, because `sudo` is root.
- [x] `sudo passwd newuser` sets the password for `newuser`.
- [x] Running `passwd` as yourself changes your own password.

</details>

### Question 12: What do the digits in `chmod 600` mean?

<details>
<summary>Answer</summary>

- [x] Read is 4, write is 2, and execute is 1.
- [x] The three digits are user, group, and other.
- [x] `600` is read and write for the owner and nothing for group or other.
- [x] The lesson uses that mode on `server.key`.

</details>

### Question 13: How is SELinux enforcing mode different from permissive mode?

<details>
<summary>Answer</summary>

- [x] Enforcing applies the policy and blocks what the policy denies.
- [x] Permissive still evaluates the policy but only warns.
- [x] `sestatus` shows the current mode. `setenforce` changes it now. `/etc/selinux/config` changes it at boot.

</details>

### Question 14: Why can `chcon` appear to “stick” and then vanish?

<details>
<summary>Answer</summary>

- [x] `chcon -t` changes the type on the file immediately.
- [x] A later relabel restores the type stored in file-context policy.
- [x] `semanage fcontext -a -t` updates that policy. `restorecon` applies the policy type now.

</details>

### Question 15: What is an established packet, from iptables’ point of view?

<details>
<summary>Answer</summary>

- [x] NEW is the first packet of a flow.
- [x] ESTABLISHED means the firewall has already seen that flow, even if the TCP handshake is not finished.
- [x] RELATED is a new connection that belongs to an existing one, such as an active-FTP data channel.
- [x] INVALID traffic is a candidate to drop or log.

</details>

### Question 16: Why are log and drop two iptables rules?

<details>
<summary>Answer</summary>

- [x] `-j DROP` discards the packet and does not write a log line.
- [x] `-j LOG` writes a syslog message and continues to the next rule.
- [x] To record a drop, log in one rule and drop in a later rule.

</details>

### Question 17: What does `ufw allow ssh` look up?

<details>
<summary>Answer</summary>

- [x] The service name `ssh` in `/etc/services`.
- [x] That name is TCP port 22.
- [x] You can also name a port directly, as in `ufw allow 80/tcp`.

</details>

</details>

## Summary

Secure the machine before the operating system starts: firmware password, physical locks, and a hashed GRUB superuser, rebuilt with `update-grub`. Know which family you are on. Debian-family systems use `apt-get` and `apt-cache`. Red Hat-family systems use `yum` and RPM. systemd targets replace SysV runlevels: `graphical.target` is runlevel 5, `multi-user.target` is runlevel 3, `isolate` is temporary, and `set-default` sticks. Services, listeners, and logins are `systemctl`, `netstat`, and `last`. Ship rsyslog off the box so a compromised host cannot be the only copy of the logs. Add users with `useradd` and `passwd`, enforce complexity in PAM, and treat John the Ripper as a check for weak passwords. AppArmor profiles and SELinux types are mandatory. `chcon` is temporary unless `semanage fcontext` records the label. iptables tables and chains, connection state, and separate log and drop rules are the packet filter. firewalld zones and ufw are the easier front ends. The course ends by telling you to install CentOS, Ubuntu, or Kali in a VM and repeat the tools yourself.

## References

- [Linux Security & Administration: From Boot Process to Firewalls (YouTube)](https://www.youtube.com/watch?v=_WB3evmgxYA)
- [Local transcript](../course_videos/Linux%20Security%20%26%20Administration%20From%20Boot%20Process%20to%20Firewalls/Linux%20Security%20%26%20Administration%20From%20Boot%20Process%20to%20Firewalls.txt)
- [DistroWatch](https://distrowatch.com/)
- [CentOS](https://www.centos.org/)
- [Ubuntu](https://ubuntu.com/)

</details>








