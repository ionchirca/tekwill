######### Configure SSH for github commits on linux ###########

"""Step 1. Generate 2 keys = public and private"""
--------------------------------------------------
ssh-keygen # generate the ssh-key by running the command in terminal, customize filename and passphrase or hit enter for default
           # once generated the pub (id_rsa.pub) and private key (id_rsa) should appear on location ~/.ssh

           # for better security use {ssh-keygen -t rsa -b 4096} OR {ssh-keygen -t ed25519}. ED25519 beeing better tha RSA algorithms

"""Step 2. Add private key to your client machine(personal PC)"""
-----------------------------------------------------------------
ssh-add ~/.ssh/id_rsa # check if ssh-agent is runing (ps -ax | grep ssh-agent OR eval `ssh-agent`) add your private key to your ssh-agent

"""Step 3. Add public key to your server machine(github)"""
-----------------------------------------------------------
cat ~/.ssh/id_rsa.pub # copy and add the SSH public key to your GitHub account OR install xclip to copy automatically
                      # apt-get install xclip
                      # xclip -sel clip < ~/.ssh/id_rsa.pub -> Copies the contents of the id_rsa.pub file to your clipboard

Go to you github.com

-->> Settings -->> SSH and GPG keys -->> SSH keys -->> New SSH key or Add SSH key -->>
-->> Paste your key into the "Key" field -->> Click Add SSH key -->> If prompted, confirm your GitHub password

"""Step 4. Change remote commit URL"""
--------------------------------------
git remote -v # check current fetch and push paths, should be by default https
git remote set-url origin git@github.com:<Username>/<Project>.git # change the romote url to ssh, where <Username> = your github user and <Project> = your project name
git remote -v # check again if changes applied

######## Now you should be abble to commit without prompting for username and password #########
