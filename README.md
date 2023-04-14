# python_import_example_20230415

Pythonのimport挙動をテストするためのリポジトリ。

```shell
pyenv local 3.8.10

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

pytest .
```

|test function|result|
|:--|:--|
|test_utility_hoge_execute_hoge|OK|
|test_utility_fuga_execute_fuga|NG|
|test_utility_fuga_execute_fuga_after_import_fuga|OK|
|test_hoge_execute_hoge|OK|
|test_fuga_execute_fuga|OK|
|test_execute_hoge|OK|
|test_execute_fuga|OK|
