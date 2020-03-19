
# GitSync

Set path to `gitsync.service`,  
Set branch filter regex to `sync.sh`    
add `gitsync.service` and `gitsync.timer` to `~/.config/systemd/user/`, use `systemd --user enable gitsync.timer` to run.  
add your origin token(GitHub) token to `origin_token`  
add your origin ssh key to `origin_url`   
add your mirror ssh to `mirror_url`   
add your ssh mirror url to `mirror_url`  
