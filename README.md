# Proj_qr_gen_team_58
This Project is for generating Qr Code and right now,
the following functions have been successfully implemented
1. login
2. logout
3. web Qr code
4. user upload of link and converting to qr code
5. User registration
6. Rendering generated qr codes
7. Social Share
8.  recieving inputs from the user

Task not yet implemented
1. email auth
2. saving to user dashboard


# Contribution Guide
### Fork The Repo
* Navigate to the Spoon-Knife project at [https://github.com/zuri-training/Proj_qr_gen_team_58](https://github.com/zuri-training/Proj_qr_gen_team_58)
* Click on the fork button
* Confirm that the owner name is yours and name of the name of the project matches the original. Optionally, you can add a description to your fork.
* Copy the default main branch
* Click create fork.

### Clone The Repo
* Navigate to your fork of the repository
* Click on **Code** .
* Copy the URL for the repository.
    To clone the repository using HTTPS, under "HTTPS", click on the copy button.
* Open git bash
* Cd into the directory you want to clone your project
* Use the command `git clone https://github.com/YOUR-USERNAME/Proj_qr_gen_team_58` and press enter.

### Configuring Git To Sync Your Fork With The Original Repository
* Use command `git remote -v` and press enter to view the configured remote repository of your fork.
* Add the parent repo using command `git remote add upstream https://github.com/zuri-training/Proj_qr_gen_team_58.git`, then press enter.
* To verify the new upstream, use command `git remote -v` again and press enter. You should see your fork as the origin url and original repo as the upstream url:
```
$ git remote -v
origin  https://github.com/YOUR-USERNAME/Proj_qr_gen_team_58.git (fetch)
origin  https://github.com/YOUR-USERNAME/Proj_qr_gen_team_58.git (push)
upstream        https://github.com/zuri-training/Proj_qr_gen_team_58.git (fetch)
upstream        https://github.com/zuri-training/Proj_qr_gen_team_58.git (push)

```

### Creating Your Branch
* Once you have successfully forked and cloned the repo on your local, cd into the project folder using  `cd Proj_qr_gen_team_58`.
* Use command `git branch` to see the branches available.
* Use command `git checkout -b branch_name` to create your new branch that you would be working on. If you already have a branch, use command `git checkout branch_name`.
Now you can go ahead and make changes on your branch to thereafter send a pull request to be reviewed and merged with the main branch.

### Syncing Forked Branch To Get Latest Code
* Use command `git pull upstream main` else if stated that there is a dev branch, then use `git pull upstream branch-name`.

### Pushing Your Code And Sending Pull Requests
* Before you begin working on your branch, always ensure to pull upstream to get latest code update and avoid merge conflict.
 Tip 💡: You can check the branch you are working on using `git branch`
* Once you are done coding, stage your changes using `git add`.
* Then commit your changes your local branch: `git commit -m 'your reason for adding the code'`.
 Tip 💡: You can check the files yet to be staged and committed using `git status`.
* Check the parent repo if there has been any update since your recent pull to avoid conflicts and have a work that is in sync by pulling from the parent repo again using command `git pull upstream main` (except otherwise stated that there is a dev branch, then use `git pull upstream branch-name`)
* Once the pull is completed without any conflicts, push your changes to your own repo using `git push origin branch-name`.
* Go to your repo, click on make contributions (if create a pull request doesn't show up) and create a pull request.
* Compare parent development branch with your own development branch and create a pull request
