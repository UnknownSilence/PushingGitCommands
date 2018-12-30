# PushingGitCommands
I forget the Git commands too often so I made this to help remember.


----------------------------------------------------------------------

To push a project folder to GitHub:

-Open Git Bash in the folder you wish to push

- git init
(Initializes local directory as a repository)

- git add .
(Adds all files in that directory)

- git commit -m "YOUR COMMIT MESSAGE HERE"
(Optional: adds a commit message for your push)

- git remote add origin URLofREPOSITORY
(Adds what repository you are pushing to)

- git remote -v
(Verifies the location of the repository)

- git push origin master
(Pushes your folder to your repository

----------------------------------------------------------------------

If you get an error like this
----------------------------
"! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'git@github.com:NAME/NAME.git'
To prevent you from losing history, non-fast-forward updates were rejected
Merge the remote changes (e.g. 'git pull') before pushing again.  See the
'Note about fast-forwards' section of 'git push --help' for details."

Try This
---------------------------

- git push --force URLofRepository
(This will force push your repository)



