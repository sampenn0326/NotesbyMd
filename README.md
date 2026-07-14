每次运行

```CMD
git add .
git commit -m "更新笔记"
git push
```

GitHub Actions 都会自动重新构建并更新网站。

也就是，一般工作流为

```CMD
Typora 写 Markdown
        ↓
保存
        ↓
git add .
git commit -m "更新"
git push
        ↓
GitHub 自动更新网站（约30秒~2分钟）
```



**全流程**

1.打开`cmd`，运行`E:`切换到E盘，以`cd MarkDown`打开目录。

2.激活环境(若需要本地预览)

```cmd
.venv\Scripts\activate.bat
```

本地预览

```cmd
mkdocs serve
```

3.上传更新

```cmd
git add .
git commit -m "更新笔记"
git push
```



其它



查看修改了哪些文件`git status`

查看提交历史`git log --oneline`











