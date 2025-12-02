# Advent of Cyber 2025 Day 1 Write Up

First part was relatively straight forward - this is going to focus on the side quest.

First I checked out the note in the /home/mcskidy/Documents/ directory. This note is in a file called read-me-please.txt and contains the following contents:

From: mcskidy
To: whoever finds this

I had a short second when no one was watching. I used it.

I've managed to plant a few clues around the account.
If you can get into the user below and look carefully,
those three little "easter eggs" will combine into a passcode
that unlocks a further message that I encrypted in the
/home/eddi_knapp/Documents/ directory.
I didn't want the wrong eyes to see it.

Access the user account:
username: eddi_knapp
password: S0mething1Sc0ming

There are three hidden easter eggs.
They combine to form the passcode to open my encrypted vault.

Clues (one for each egg):

1)
I ride with your session, not with your chest of files.
Open the little bag your shell carries when you arrive.

2)
The tree shows today; the rings remember yesterday.
Read the ledger’s older pages.

3)
When pixels sleep, their tails sometimes whisper plain words.
Listen to the tail.

Find the fragments, join them in order, and use the resulting passcode
to decrypt the message I left. Be careful — I had to be quick,
and I left only enough to get help.

~ McSkidy

First I logged in with the credentials provided by using the following command:

su eddi_knapp

And entering the password when prompted. The following is a list (including hidden files) of the users home directory:

total 124
drwxr-x--- 18 eddi_knapp eddi_knapp 4096 Dec  2 02:54 .
drwxr-xr-x  6 root       root       4096 Oct 10 17:27 ..
-rw-------  1 eddi_knapp eddi_knapp  270 Dec  2 02:59 .bash_history
-rw-r--r--  1 eddi_knapp eddi_knapp  220 Feb 25  2020 .bash_logout
-rw-r--r--  1 eddi_knapp eddi_knapp 3797 Nov 11 16:24 .bashrc
-rw-r--r--  1 eddi_knapp eddi_knapp 3797 Nov 11 16:19 .bashrc.bak
drwxrwxr-x  3 eddi_knapp eddi_knapp 4096 Nov 30 18:18 .cache
drwx------  2 eddi_knapp eddi_knapp 4096 Oct  9 16:50 .config
drwx------  3 eddi_knapp eddi_knapp 4096 Dec  2 02:51 .gnupg
-rw-------  1 eddi_knapp eddi_knapp   68 Oct 10 18:16 .image_meta
-rw-------  1 eddi_knapp eddi_knapp   20 Oct 10 10:34 .lesshst
drwxrwxr-x  4 eddi_knapp eddi_knapp 4096 Nov 30 18:18 .local
-rw-------  1 eddi_knapp eddi_knapp   19 Nov 11 16:30 .pam_environment
-rw-------  1 eddi_knapp eddi_knapp   19 Nov 11 16:24 .pam_environment.bak
-rw-r--r--  1 eddi_knapp eddi_knapp  833 Nov 11 16:30 .profile
-rw-r--r--  1 eddi_knapp eddi_knapp  833 Nov 11 16:24 .profile.bak
drwxrwxr-x  2 eddi_knapp eddi_knapp 4096 Dec  1 08:32 .secret
drwx------  3 eddi_knapp eddi_knapp 4096 Nov 11 12:07 .secret_git
drwx------  3 eddi_knapp eddi_knapp 4096 Oct  9 17:20 .secret_git.bak
-rw-------  1 eddi_knapp eddi_knapp 7167 Nov 11 16:23 .viminfo
drwxr-xr-x  2 eddi_knapp eddi_knapp 4096 Oct 10 18:15 Desktop
drwxr-xr-x  2 eddi_knapp eddi_knapp 4096 Nov 14 19:31 Documents
drwxr-xr-x  2 eddi_knapp eddi_knapp 4096 Oct 10 18:15 Downloads
drwxr-xr-x  2 eddi_knapp eddi_knapp 4096 Oct  9 16:50 Music
drwxr-xr-x  2 eddi_knapp eddi_knapp 4096 Oct 10 18:16 Pictures
drwxr-xr-x  2 eddi_knapp eddi_knapp 4096 Oct  9 16:50 Public
drwxr-xr-x  2 eddi_knapp eddi_knapp 4096 Oct  9 16:50 Templates
drwxr-xr-x  2 eddi_knapp eddi_knapp 4096 Oct  9 16:50 Videos
drwxrwxr-x  2 eddi_knapp eddi_knapp 4096 Nov 11 16:24 fix_passfrag_backups_20251111162432
-rw-rw-r--  1 eddi_knapp eddi_knapp  429 Oct  9 17:53 wget-log

There's a lot to look through here so the clues are helpful.

_I ride with your session, not with your chest of files.
Open the little bag your shell carries when you arrive._

Initially I thought this would have to do with an ssh session running to the machine. After trying to look at running processes and having no luck,
I realized the clue is referring to environment variables:
- Environment variables are shell session dependent
- While user/global environment variables are saved in configuration files, the environment variables for a session exist in the sessions memory

The environment variables can be printed with the following command:

printenv

This produced the following output:

SHELL=/bin/bash
COLORTERM=truecolor
SUDO_GID=1000
SUDO_COMMAND=/usr/bin/su mcskidy
PASSFRAG1=3ast3r
SUDO_USER=ubuntu
PWD=/home/eddi_knapp
LOGNAME=eddi_knapp
XAUTHORITY=/home/ubuntu/.Xauthority
HOME=/home/eddi_knapp
LANG=C.UTF-8
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=00:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.avif=01;35:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:*~=00;90:*#=00;90:*.bak=00;90:*.crdownload=00;90:*.dpkg-dist=00;90:*.dpkg-new=00;90:*.dpkg-old=00;90:*.dpkg-tmp=00;90:*.old=00;90:*.orig=00;90:*.part=00;90:*.rej=00;90:*.rpmnew=00;90:*.rpmorig=00;90:*.rpmsave=00;90:*.swp=00;90:*.tmp=00;90:*.ucf-dist=00;90:*.ucf-new=00;90:*.ucf-old=00;90:
XDG_CURRENT_DESKTOP=MATE
LESSCLOSE=/usr/bin/lesspipe %s %s
TERM=xterm-256color
LESSOPEN=| /usr/bin/lesspipe %s
USER=eddi_knapp
DISPLAY=:1
SHLVL=2
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
SUDO_UID=1000
MAIL=/var/mail/eddi_knapp
OLDPWD=/home
_=/usr/bin/printenv

Note that the first password fragment is contained in this output:

PASSFRAG1=3ast3r

_The tree shows today; the rings remember yesterday.
Read the ledger’s older pages._

Initially I thought this was going to have to do with file trees and ring buffers. Specifically, I was looking for a Linux ring buffer
that stores a history of file tree changes that I could revert to. This yielded no results.

Then I noticed that within the users home directory there is a .secret_git directory. This lends itself well to the clue:
- The rings remembering yesterday is a reference to gits commit history
- In this instance the ledger is the history of commits - an older commit should contain the answer

Going into this directory and running the git status command reveals that this is a git directory. Listing the contents of the directory
reveals nothing except the .git directory. The history of this repository can be obtained by running the git log command:

commit e924698378132991ee08f050251242a092c548fd (HEAD -> master)
Author: mcskiddy <mcskiddy@robco.local>
Date:   Thu Oct 9 17:20:11 2025 +0000

    remove sensitive note

commit d12875c8b62e089320880b9b7e41d6765818af3d
Author: McSkidy <mcskiddy@tbfc.local>
Date:   Thu Oct 9 17:19:53 2025 +0000

    add private note

From this output it is clear that a sensitive note was created and deleted. 

To gain access to the deleted note, I used the git checkout command with the hash for the commit that added the file (note this command
results in a detached HEAD state):

git checkout d12875c8b62e089320880b9b7e41d6765818af3d

Now typing ls -la shows a new file in the directory:

total 16
drwx------  3 eddi_knapp eddi_knapp 4096 Dec  2 04:01 .
drwxr-x--- 18 eddi_knapp eddi_knapp 4096 Dec  2 03:33 ..
drwx------  8 eddi_knapp eddi_knapp 4096 Dec  2 04:01 .git
-rwxrwxr-x  1 eddi_knapp eddi_knapp  151 Dec  2 04:01 secret_note.txt

Openning up secret_note.txt yields the second password fragment:

========================================
Private note from McSkidy
========================================
We hid things to buy time.
PASSFRAG2: -1s-

_When pixels sleep, their tails sometimes whisper plain words.
Listen to the tail._

Initially I assumed this clue was related to the computer screen sleeping. After attempting to check sleep/shutdown/reboot logs with no 
luck I noted that pixel could also relate to an image file. Here is the output of running ls -la on the Pictures directory:

total 160680
drwxr-xr-x  2 eddi_knapp eddi_knapp    4096 Oct 10 18:16 .
drwxr-x--- 18 eddi_knapp eddi_knapp    4096 Dec  2 04:06 ..
-rw-rw-r--  1 eddi_knapp eddi_knapp    1442 Oct  9 18:07 .easter_egg
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Aug 13 18:15 .hidden_pic_1.png
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Jul 20 18:15 .hidden_pic_2.png
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Sep 11 18:15 .hidden_pic_3.png
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Oct  2 18:15 .hidden_pic_4.png
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Sep 28 18:15 .hidden_pic_5.png
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Sep 19 18:15 banner_01.jpg
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Sep 21 18:15 banner_02.png
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Sep 28 18:15 conference_badge.jpg
-rw-rw-r--  1 eddi_knapp eddi_knapp   47445 Oct  9 17:59 easter.png
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Sep  7 18:15 family_holiday.jpg
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Sep 23 18:15 holiday_card.jpg
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Sep  5 18:15 kids_playground.jpg
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Oct 10 18:15 large_photo_1.jpg
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Oct 10 18:16 large_photo_2.jpg
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Oct 10 18:16 large_photo_3.jpg
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Sep  4 18:15 logo_asset.png
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Sep  7 18:15 meme_asset.png
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Sep 14 18:15 office_building.png
-rw-r--r--  1 eddi_knapp eddi_knapp      39 Oct 10 18:16 photo_meta_1.txt
-rw-r--r--  1 eddi_knapp eddi_knapp      39 Oct 10 18:16 photo_meta_2.txt
-rw-r--r--  1 eddi_knapp eddi_knapp      39 Oct 10 18:16 photo_meta_3.txt
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Oct  9 18:15 profile_pic.png
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Sep  8 18:15 random_image_001.png
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Sep 13 18:15 random_image_002.jpg
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Sep 19 18:15 receipt_scan.jpg
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Oct 10 18:15 scenery_01.png
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Sep 23 18:15 scenery_02.jpg
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Oct 10 18:15 screenshot_2025-06-01.png
-rw-r--r--  1 eddi_knapp eddi_knapp       0 Oct 10 18:15 scuffed_1.jpg
-rw-r--r--  1 eddi_knapp eddi_knapp       0 Oct 10 18:15 scuffed_2.jpg
-rw-r--r--  1 eddi_knapp eddi_knapp       0 Oct 10 18:15 scuffed_3.jpg
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Sep 12 18:15 vacation_beach.jpg
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Sep  6 18:15 wallpaper_autumn.png
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Sep 13 18:15 wallpaper_spring.png
-rw-r--r--  1 eddi_knapp eddi_knapp 5871771 Oct  6 18:15 work_event.png

Most of these files have the same permissions and same size. It is extremely likely that these files all contain the same contents,
so I began my search with the other files.

The clue mentions "tail" twice - a good indication that the tail command will be useful here. Running tail on the first file
produces the final password fragment:

 EASTER ~~~
PASSFRAG3: c0M1nG

Putting all of the pieces together, the password to decrypt the file in the /home/eddi_knapp/Documents/ directory is:

3ast3r-1s-c0M1nG

Navigating to the /home/eddi_knapp/Documents/ directory, there are two files:
- notes_on_photos.txt: This doesn't appear to contain any useful information
- mcskidy_note.txt.gpg: This appears to be the note mcskidy left for us

The .gpg extension indicates this file was encrypted using the Gnu Privacy Guard. The following gpg command decrypts the file:

gpg --batch --yes --passphrase '3ast3r-1s-c0M1nG' --decrypt mcskidy_note.txt.gpg

Explanation of the switches:
- --batch: Specifies non-interactive mode, meaning the program won't ask for a passphrase
- --yes: Automatically answers "yes" to overwriting files when necessary
- --passphrase '3ast3r-1s-c0M1nG': Passes the decryption password as a command line arguement
- --decrypt: Specifies decryption

This produces the following output:

gpg: AES256.CFB encrypted data
gpg: encrypted with 1 passphrase
Congrats — you found all fragments and reached this file.

Below is the list that should be live on the site. If you replace the contents of
/home/socmas/2025/wishlist.txt with this exact list (one item per line, no numbering),
the site will recognise it and the takeover glitching will stop. Do it — it will save the site.

Hardware security keys (YubiKey or similar)
Commercial password manager subscriptions (team seats)
Endpoint detection & response (EDR) licenses
Secure remote access appliances (jump boxes)
Cloud workload scanning credits (container/image scanning)
Threat intelligence feed subscription

Secure code review / SAST tool access
Dedicated secure test lab VM pool
Incident response runbook templates and playbooks
Electronic safe drive with encrypted backups

A final note — I don't know exactly where they have me, but there are *lots* of eggs
and I can smell chocolate in the air. Something big is coming.  — McSkidy

---

When the wishlist is corrected, the site will show a block of ciphertext. This ciphertext can be decrypted with the following unlock key:

UNLOCK_KEY: 91J6X7R4FQ9TQPM9JX2Q9X2Z

To decode the ciphertext, use OpenSSL. For instance, if you copied the ciphertext into a file /tmp/website_output.txt you could decode using the following command:

cat > /tmp/website_output.txt
openssl enc -d -aes-256-cbc -pbkdf2 -iter 200000 -salt -base64 -in /tmp/website_output.txt -out /tmp/decoded_message.txt -pass pass:'91J6X7R4FQ9TQPM9JX2Q9X2Z'
cat /tmp/decoded_message.txt

Sorry to be so convoluted, I couldn't risk making this easy while King Malhare watches. — McSkidy

The instructions here are relatively clear. First, I switched back to the mcskidy user profile. I then navigated to the
/home/socmas/2025/wishlist.txt file and swapped the contents for those in the note. Accessing the website on http://10.64.176.76:8080/
Showed an updated wishlist along with a gibberish message

U2FsdGVkX1/7xkS74RBSFMhpR9Pv0PZrzOVsIzd38sUGzGsDJOB9FbybAWod5HMsa+WIr5HDprvK6aFNYuOGoZ60qI7axX5Qnn1E6D+BPknRgktrZTbMqfJ7wnwCExyU8ek1RxohYBehaDyUWxSNAkARJtjVJEAOA1kEOUOah11iaPGKxrKRV0kVQKpEVnuZMbf0gv1ih421QvmGucErFhnuX+xv63drOTkYy15s9BVCUfKmjMLniusI0tqs236zv4LGbgrcOfgir+P+gWHc2TVW4CYszVXlAZUg07JlLLx1jkF85TIMjQ3B91MQS+btaH2WGWFyakmqYltz6jB5DOSCA6AMQYsqLlx53ORLxy3FfJhZTl9iwlrgEZjJZjDoXBBMdlMCOjKUZfTbt3pnlHWEaGJD7NoTgywFsIw5cz7hkmAMxAIkNn/5hGd/S7mwVp9h6GmBUYDsgHWpRxvnjh0s5kVD8TYjLzVnvaNFS4FXrQCiVIcp1ETqicXRjE4T0MYdnFD8h7og3ZlAFixM3nYpUYgKnqi2o2zJg7fEZ8c=

I saved this in the file /tmp/gibberish.txt and then ran the following openssl command:

openssl enc -d -aes-256-cbc -pbkdf2 -iter 200000 -salt -base64 -in /tmp/gibberish.txt -out /tmp/decoded_message.txt -pass pass:'91J6X7R4FQ9TQPM9JX2Q9X2Z'

Opening up the file /tmp/decoded_message.txt shows the following:

Well done — the glitch is fixed. Amazing job going the extra mile and saving the site. Take this flag THM{w3lcome_2_A0c_2025}

NEXT STEP:
If you fancy something a little...spicier....use the FLAG you just obtained as the passphrase to unlock:
/home/eddi_knapp/.secret/dir

That hidden directory has been archived and encrypted with the FLAG.
Inside it you'll find the sidequest key.

I had noticed this file earlier and wondered what it might be for. First I needed to log back in as eddi knapp with the credentials from before.
Next I navigated to the /home/eddi_knapp/.secret/ directory. This directory contains a single file: dir.tar.gz.gpg. As before, this file appears
to be encrypted with GPG encryption. Running the following command decrypts the archive file:

gpg --batch --yes --passphrase 'THM{w3lcome_2_A0c_2025}' --output dir.tar.gz --decrypt dir.tar.gz.gpg

This places the decrypted contents into the dir.tar.gz file.

I then unarchived the file using the command:

tar -xvf dir.tar.gz

This yields the dir directory which contains a single file: sq1.png. I was able to open this file in the operating systems image viewer
(top left Applications -> Graphics -> Eye of MATE Image Viewer). The image is of a an egg with a rabbit on it and contains the message:

now_you_see_me

I assume this is the key to the first side quest
