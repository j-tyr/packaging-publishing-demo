# packaging-publishing-demo

A small demo of an automated release pipeline, built before adopting it in a real project.

It shows three things:

1. **Versioning from git tags.** The version number is not written in any file. It is computed by [setuptools-scm](https://setuptools-scm.readthedocs.io/) from git, so `git tag v0.1.0` *is* the release.
2. **CI on every push and PR.** Tests run on Python 3.11, 3.12 and 3.13 via tox, using the Neuroinformatics Unit's reusable GitHub Actions (`neuroinformatics-unit/actions/*@v2`).
3. **Publishing on tag push.** The package is built (sdist + wheel) and uploaded to **TestPyPI** using [trusted publishing](https://docs.pypi.org/trusted-publishers/) (OIDC), so no API tokens are stored anywhere.

The package itself (`packaging-publishing-demo-jt`) is a trivial placeholder.

## The flow

```
 push to branch / PR          push of a tag like v0.1.0
         |                              |
         v                              v
   tests (3.11, 3.12, 3.13)       tests (3.11, 3.12, 3.13)
         |                              |
         v                              v
       done                       build sdist + wheel
                                        |
                                        v
                              publish to TestPyPI
                       (waits for approval, if configured)
```

On an ordinary push only the tests run. The build and publish jobs run only when a tag is pushed.

## Demo script

1. **Ordinary push.** Push `main` (or a branch / PR). CI runs the 3 test jobs only. Each log prints `installed version: 0.1.dev1+g<hash>`. This is not a "real" version: with no tag visible, setuptools-scm falls back to `0.1.devN+g<hash>`.
2. **Release.**
   ```bash
   git tag v0.1.0
   git push origin v0.1.0
   ```
   CI runs the tests, then the build, then (after approval, if configured) the publish step. The project appears at <https://test.pypi.org/project/packaging-publishing-demo-jt/>.
3. **Install** in a fresh virtual environment:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ packaging-publishing-demo-jt
   python -c "import packaging_publishing_demo as m; print(m.__version__, m.greet())"
   ```
   This prints `0.1.0`.
4. **Next release.** Commit a small change, then `git tag v0.1.1` and push the tag. A new version appears with no files edited to bump the version.
5. *(Optional)* **Version numbers can't be reused.** Re-publishing an existing version is refused, and deleting a release on (Test)PyPI doesn't free its number either.

## Install

```bash
pip install --index-url https://test.pypi.org/simple/ packaging-publishing-demo-jt
```

The package has no dependencies, so no `--extra-index-url` is needed.

## Development

```bash
pip install -e . --group dev   # needs pip >= 25.1
tox                            # needs Python 3.11-3.13
```
