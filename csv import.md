csv import

```
$ sqlite3 db.sqlite
```

```
.mode csv
.import test.csv table_name
```

----



dumpdata

```
python manage.py dumpdata --indent 4 app_name.model_name > test.json
```



---

loaddata

```
python manage.py loaddata app_name/test.json
```

-  반드시 파일 위치는 app/fixtures/app/  안에 있어야 함



```
i9i91@DESKTOP-B5GL7LM MINGW64 ~/OneDrive/바탕 화면/github 저장내용/portfolio.io/githubservice (heejungnew)
$ sqlite3 db.sqlite3
SQLite version 3.32.3 2020-06-18 14:00:33
Enter ".help" for usage hints.
sqlite> .tables
accounts_user                   django_session
accounts_user_groups            mains_comment
accounts_user_user_permissions  mains_post
auth_group                      mains_post_like_users
auth_group_permissions          portfolios_color
auth_permission                 portfolios_github
django_admin_log                portfolios_skill
django_content_type             portfolios_usercontent
django_migrations
sqlite> .mode csv
sqlite> .import Application_Data.csv portfolios.
sqlite> .import Application_Data.csv portfolios.Skill
sqlite> .import Application_Data.csv portfolios.Skill
CREATE TABLE portfolios.Skill(...) failed: unknown database portfolios
sqlite> .import Application_Data.csv portfolios_skill
Application_Data.csv:1: INSERT failed: datatype mismatch
sqlite>
sqlite> .exit

i9i91@DESKTOP-B5GL7LM MINGW64 ~/OneDrive/바탕 화면/github 저장내용/portfolio.io/githubservice (heejungnew)
$ python manage.py dumpdata --indent 4 portfolios.Skill > skills.json
```

