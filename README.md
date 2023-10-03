**請確保虛擬環境啟動 `poetry shell`**

建立 poetry 專案（產生 pyproject.toml 檔案）：`poetry init`

把套件加入 pyproject.toml 當中：`poetry add <packacge name>`

依照 pyproject.toml 的設定建立虛擬環境並安裝套件：`poetry install`


建立 Django 專案：`django-admin startproject core .`

啟動伺服器：`python manage.py runserver` (用瀏覽器訪問 <http://127.0.0.1:8000>)

建立 Django APP：`python manage.py startapp <app name>`


依照 models.py 產生 migrations 檔案：`python manage.py makemigrations`

依照 migrations 建立資料庫：`python manage.py migrate`

建立超級使用者：`python manage.py createsuperuser`

安裝套件到 dev 這個 group 中：`poetry add --group dev <package name>` (例如：`ipython`)

啟動 Django 的互動環境（Python 直譯環境 + Django Setup）：`python manage.py shell`

安裝 djLint: `poetry add --group dev djlint`
安裝 black: `poetry add --group dev black`

安裝 django-bootstrap5: `poetry add django-bootstrap5`

安裝 django-extensions: `poetry add django-extensions`

進入 Django Shell Plus: `python manage.py shell_plus --print-sql`

安裝 django-extensions: `poetry add --group dev werkzeug`

進入 Django Runserver Plus: `python manage.py runserver_plus --print-sql`
111
## 參考資料

Template Tags: <https://docs.djangoproject.com/en/4.2/ref/templates/builtins/>





