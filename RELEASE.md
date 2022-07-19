# How to release a version

### 1 - Change package version

You should find 3 files in the repository:
    - meta.yml (not really needed as conda is not automatized yet but to follow the version)
    - pyproject.toml
    - setup.py

In all 3 files you must changes actual package version to the new one, for example if actual version is `0.0.6` yo should change that value in all 3 files with `0.0.7`. Push changes

#### meta.yml

```
{% set name = "sequence_annotation" %}
{% set version = "0.0.7" %}
```

#### pyproject.toml

```
[project]
name = "sequence_annotation"
version = "0.0.7"
```

#### setup.py

```
setup(
    name='sequence_annotation',
    version='0.0.7',
```

### 2 - Release version

You must create a tag and a release in github with same version following the previous release, for example `0.0.7`

### AUtomatic publish

If all was done fine, then a job must publish the new version to Test Pypi and Pypi
