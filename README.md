# `CoverageException: Can't add file tracer data for unmeasured file` bug reproduction

## Description

A combination of `django`, `pytest`, `pytest-cov`, `django-coverage-plugin` and `pytest-django` seems to interact with each other causing `CoverageException` when tests cause templates to be rendered. My guess is it's somewhere in `django-coverage-plugin` as disabling it, removes the exception.

## Expected behavior

Coverage report has been generated

## Actual behavior

Creating raport crashes with `CoverageException`:

```
pipenv run pytest --cov=.
==================================================== test session starts ====================================================
platform darwin -- Python 3.7.5, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
django: settings: test_cov.settings (from ini)
rootdir: /Users/suda/tmp/pytest_django_coverage_test, inifile: pytest.ini
plugins: django-3.9.0, cov-2.8.1
collected 1 item

render_something/tests.py .                                                                                           [100%]
INTERNALERROR> Traceback (most recent call last):
INTERNALERROR>   File "/Users/suda/.virtualenvs/pytest_django_coverage_test-wtRTEdEB/lib/python3.7/site-packages/_pytest/main.py", line 191, in wrap_session
INTERNALERROR>     session.exitstatus = doit(config, session) or 0
INTERNALERROR>   File "/Users/suda/.virtualenvs/pytest_django_coverage_test-wtRTEdEB/lib/python3.7/site-packages/_pytest/main.py", line 247, in _main
INTERNALERROR>     config.hook.pytest_runtestloop(session=session)
INTERNALERROR>   File "/Users/suda/.virtualenvs/pytest_django_coverage_test-wtRTEdEB/lib/python3.7/site-packages/pluggy/hooks.py", line 286, in __call__
INTERNALERROR>     return self._hookexec(self, self.get_hookimpls(), kwargs)
INTERNALERROR>   File "/Users/suda/.virtualenvs/pytest_django_coverage_test-wtRTEdEB/lib/python3.7/site-packages/pluggy/manager.py", line 93, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook, methods, kwargs)
INTERNALERROR>   File "/Users/suda/.virtualenvs/pytest_django_coverage_test-wtRTEdEB/lib/python3.7/site-packages/pluggy/manager.py", line 87, in <lambda>
INTERNALERROR>     firstresult=hook.spec.opts.get("firstresult") if hook.spec else False,
INTERNALERROR>   File "/Users/suda/.virtualenvs/pytest_django_coverage_test-wtRTEdEB/lib/python3.7/site-packages/pluggy/callers.py", line 203, in _multicall
INTERNALERROR>     gen.send(outcome)
INTERNALERROR>   File "/Users/suda/.virtualenvs/pytest_django_coverage_test-wtRTEdEB/lib/python3.7/site-packages/pytest_cov/plugin.py", line 254, in pytest_runtestloop
INTERNALERROR>     self.cov_controller.finish()
INTERNALERROR>   File "/Users/suda/.virtualenvs/pytest_django_coverage_test-wtRTEdEB/lib/python3.7/site-packages/pytest_cov/engine.py", line 197, in finish
INTERNALERROR>     self.cov.stop()
INTERNALERROR>   File "/Users/suda/.virtualenvs/pytest_django_coverage_test-wtRTEdEB/lib/python3.7/site-packages/coverage/control.py", line 642, in save
INTERNALERROR>     data = self.get_data()
INTERNALERROR>   File "/Users/suda/.virtualenvs/pytest_django_coverage_test-wtRTEdEB/lib/python3.7/site-packages/coverage/control.py", line 696, in get_data
INTERNALERROR>     if self._collector and self._collector.flush_data():
INTERNALERROR>   File "/Users/suda/.virtualenvs/pytest_django_coverage_test-wtRTEdEB/lib/python3.7/site-packages/coverage/collector.py", line 426, in flush_data
INTERNALERROR>     self.covdata.add_file_tracers(self.mapped_file_dict(self.file_tracers))
INTERNALERROR>   File "/Users/suda/.virtualenvs/pytest_django_coverage_test-wtRTEdEB/lib/python3.7/site-packages/coverage/sqldata.py", line 516, in add_file_tracers
INTERNALERROR>     "Can't add file tracer data for unmeasured file '%s'" % (filename,)
INTERNALERROR> coverage.misc.CoverageException: Can't add file tracer data for unmeasured file '/Users/suda/tmp/pytest_django_coverage_test/render_something/templates/render_something/index.html'

===================================================== 1 passed in 0.56s =====================================================
```

## Steps to reproduce

```
$ git clone https://github.com/suda/pytest_django_coverage_test.git
$ cd pytest_django_coverage_test
$ pipenv install
$ pipenv run pytest --cov=.
```