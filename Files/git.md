# GIT by Ifeanyi Omeata

<details>
  <summary>CRASH COURSE</summary>
  
## Initialize Git

```bs
git init
git status
```

## Check Git Version

```bs
git -v
```

## Setup Git Config Global Settings

```bs
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### View Git Global Settings:

```bs
git config --global --list
git config --list --show-origin
```

## Write Text to README.md File

```bs
echo "# git-labs-ifeanyi" >> README.md
```

## Commit README.md File

```bs
git add {Filename}
git add -A
git add .
git commit -am "{commit Message}"

git add README.md
git commit -m "first commit"
```

## Set Remote Path

```bs
git branch -M main
git remote remove origin
git remote add origin https://github.com/omeatai/git-labs-ifeanyi.git
```

## Push Local Files to Remote Repo

```bs
git push -u origin main
```

## List git Local Braches

```bs
git branch
```

## List git Remote Branches

```bs
git branch -r
```

## Create git Branch and Switch to Branch

```bs
git branch first-branch
git checkout first-branch
```

```bs
git checkout -b "first-branch"
```

## Delete File from Remote Repo

```bs
git rm --cached ./app/rough.txt
git add .
git commit -m "Removed rough.txt"
git push origin first-branch
```

## Delete Remote Branch

```bs
git push origin -d "first-branch"
```

## Delete Local Branch

```bs
git checkout main
git branch -D "first-branch"
```

## Git Log History

```bs
git log
git log --oneline
```

## Git Restore Staged to Untracked

```bs
git restore {Filename}
git restore --staged {Filename}
```


</details>


### GIT COURSES

<details>
  <summary>Git Beginner</summary>
  
- [ ] [COURSE](https://www.udemy.com/course/github-copilot/)
- [ ] [Introduction](https://www.udemy.com/course/github-copilot/learn/lecture/54062401)
- [ ] [Set up local machine with Github Copilot](https://www.udemy.com/course/github-copilot/learn/lecture/53719561)

</details>


























