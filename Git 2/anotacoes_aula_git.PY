'''
------------------- GIT -------------------------

- GIT BRANCH

git branch - Lista todas as ramificações no seu repositório. Isso é um sinônimo de git branch --list
git branch <nome-branch> - Cria uma nova ramificação
git branch -d <nome-branch> - Exclui a ramificação especificada. Esta é uma operação "segura" em que o Git impede
                              que você exclua a ramificação se tiver mudanças não mescladas
git branch -D <branch> - Forçar a exclusão da ramificação especificada, mesmo que ela tenha mudanças não mescladas
git branch -m <branch> - Renomear a ramificação atual


--------------------------------------------------

- GIT CHECKOUT

git checkout <nome-do-branch> - Altera a branch que estará no seu Working Directory
git checkout -b <nome-do-branch> - Além de criar, altera para o branch criado
git checkout -- [paths]
git checkout --.


----------------------------------------------------

- GIT RESET

git reset <hash> --[paths]
git reser --hard
git reset HEAD <file-to-reset>
git reset HEAD~<commits-to-reset>


----------------------------------------------------

- GIT REVERT

git revert <hash>



'''