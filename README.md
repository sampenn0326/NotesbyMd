# NotesbyMd 跨设备工作流

使用 **Typora + Git + GitHub** 管理 Markdown 笔记。

- Typora：编辑笔记
- Git：版本管理与同步
- GitHub：云端仓库
- GitHub Pages：自动发布网站

## 1. 开始编辑前

在 PowerShell 中执行：

```
cd D:\ResearchNote\NotesbyMd
git pull
```

## 2. 编辑笔记

使用 Typora 打开 `NotesbyMd` 文件夹，正常编辑 Markdown。

图片应保存在仓库内部，确保 Git 可以同步。

## 3. 编辑完成后

```
git add .
git commit -m "Update notes"
git push
```

## 4. 跨设备同步规则

- 在当前电脑编辑完成后，必须先 `git push`。
- 换另一台电脑时，编辑前先执行 `git pull`。
- 避免多台电脑同时修改同一文件。
- Push 后 GitHub Pages 自动更新网站。

## 5. 常用命令

| 命令                           | 功能             |
| ------------------------------ | ---------------- |
| `git pull`                     | 拉取远程更新     |
| `git status`                   | 查看文件修改状态 |
| `git add .`                    | 添加所有修改     |
| `git commit -m "Update notes"` | 提交本地版本     |
| `git push`                     | 推送到 GitHub    |

**核心原则：编辑前 Pull，编辑后 Push。**
