for /d /r . %%d in (__pycache__) do (
    pushd "%%d"
    if exist .git (
        git rm -r --cached .
        git commit -m "Remove __pycache__"
        git push origin develop
    )
    popd
)