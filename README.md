# PYTHON CSV SUMMARIZER

> This is a requirement for CSC510 Software Engineering HW2,HW3,HW4,HW5 for Group 10

[![DOI](https://zenodo.org/badge/531310181.svg)](https://zenodo.org/badge/latestdoi/531310181)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/boscosylvester-john/se_hw_LuaToPython)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/boscosylvester-john/se_hw_LuaToPython?color=g)](https://github.com/boscosylvester-john/se_hw_LuaToPython/commits/main)
[![Python CI](https://github.com/boscosylvester-john/se_hw_LuaToPython/actions/workflows/tests.yaml/badge.svg)](https://github.com/boscosylvester-john/se_hw_LuaToPython/actions/workflows/tests.yaml)
[![GitHub top language](https://img.shields.io/github/languages/top/boscosylvester-john/se_hw_LuaToPython)](https://docs.python.org/3/)
[![GitHub Workflow Status (event)](https://img.shields.io/github/workflow/status/boscosylvester-john/se_hw_LuaToPython/Tests?event=push)](https://img.shields.io/github/workflow/status/boscosylvester-john/se_hw_LuaToPython/Tests?event=push)
[![GitHub contributors](https://img.shields.io/github/contributors/boscosylvester-john/se_hw_LuaToPython)](https://github.com/boscosylvester-john/se_hw_LuaToPython/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/boscosylvester-john/se_hw_LuaToPython)](https://github.com/boscosylvester-john/se_hw_LuaToPython/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/boscosylvester-john/se_hw_LuaToPython)](https://github.com/boscosylvester-john/se_hw_LuaToPython/pulls)
[![GitHub last commit](https://img.shields.io/github/last-commit/boscosylvester-john/se_hw_LuaToPython)](https://github.com/boscosylvester-john/se_hw_LuaToPython/commits/main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![GitHub forks](https://img.shields.io/github/forks/boscosylvester-john/se_hw_LuaToPython?style=social)](https://github.com/boscosylvester-john/se_hw_LuaToPython/network/members)

## Goal

Implement the functionalities of [this](https://github.com/txt/se22/blob/main/etc/pdf/csv.pdf) Lua code in Python. Basically this code will read and help store CSV data in an appropriate format. It also summarizes the data column wise and displays a few statistics.

### Functionality

- Read CSV
- CLI
- Generate Summary

### DataTypes

- Sym
- Num

### Classes

- Num
- Sym
- Data
- Cols
- Row

## Getting Started

### Installation

- Install python 3.10.7 from [here](https://www.python.org/downloads/).
- Create working directory named _Python_Summarizer_
  ```bash
  $ mkdir Python_Summarizer
  ```
- Clone this repository from [here](https://github.com/boscosylvester-john/se_hw_LuaToPython.git) or use
  ```bash
  $ git clone https://github.com/boscosylvester-john/se_hw_LuaToPython
  ```
- Install all the requirements using
  ```bash
  $ cd Python_Summarizer
  $ pip install -r requirements.txt
  ```

### Running Tests

## Coverage Reports

<table class="index" data-sortable>
    <thead>
        <tr class="tablehead" title="Click to sort">
            <th class="name left" aria-sort="none" data-shortcut="n">Module</th>
            <th aria-sort="none" data-default-sort-order="descending" data-shortcut="s">statements</th>
            <th aria-sort="none" data-default-sort-order="descending" data-shortcut="m">missing</th>
            <th aria-sort="none" data-default-sort-order="descending" data-shortcut="x">excluded</th>
            <th class="right" aria-sort="none" data-shortcut="c">coverage</th>
        </tr>
    </thead>
    <tbody>
        <tr class="file">
            <td class="name left">src\Cols.py</td>
            <td>22</td>
            <td>1</td>
            <td>0</td>
            <td class="right" data-ratio="21 22">95%</td>
        </tr>
        <tr class="file">
            <td class="name left">src\Data.py</td>
            <td>36</td>
            <td>4</td>
            <td>0</td>
            <td class="right" data-ratio="32 36">89%</td>
        </tr>
        <tr class="file">
            <td class="name left">src\Num.py</td>
            <td>37</td>
            <td>0</td>
            <td>0</td>
            <td class="right" data-ratio="37 37">100%</td>
        </tr>
        <tr class="file">
            <td class="name left">src\Row.py</td>
            <td>6</td>
            <td>0</td>
            <td>0</td>
            <td class="right" data-ratio="6 6">100%</td>
        </tr>
        <tr class="file">
            <td class="name left">src\Sym.py</td>
            <td>28</td>
            <td>0</td>
            <td>0</td>
            <td class="right" data-ratio="28 28">100%</td>
        </tr>
        <tr class="file">
            <td class="name left">src\Utils.py</td>
            <td>90</td>
            <td>18</td>
            <td>0</td>
            <td class="right" data-ratio="72 90">80%</td>
        </tr>
        <tr class="file">
            <td class="name left">tests\__init__.py</td>
            <td>6</td>
            <td>0</td>
            <td>0</td>
            <td class="right" data-ratio="6 6">100%</td>
        </tr>
        <tr class="file">
            <td class="name left">tests\test_cases.py</td>
            <td>56</td>
            <td>1</td>
            <td>0</td>
            <td class="right" data-ratio="55 56">98%</td>
        </tr>
        <tr class="file">
            <td class="name left">tests\test_engine.py</td>
            <td>55</td>
            <td>11</td>
            <td>0</td>
            <td class="right" data-ratio="44 55">80%</td>
        </tr>
    </tbody>
    <tfoot>
        <tr class="total">
            <td class="name left">Total</td>
            <td>336</td>
            <td>35</td>
            <td>0</td>
            <td class="right" data-ratio="301 336">90%</td>
        </tr>
    </tfoot>
</table>

The basic mathemtical operations that this repo does are-

- Addition
- Subtraction
- Multiplication
- Division

---

## Languages and Tools used

- Python
- Github Desktop
- Git Bash
- VS Code
- Codacy

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[License Guidelines](https://github.com/boscosylvester-john/se_hw_LuaToPython/blob/main/LICENSE.md)

### Contribute

Please have a look at the [guidelines](https://github.com/boscosylvester-john/se_hw_LuaToPython/blob/main/CONTRIBUTING.md) before contributing.

### Authors

- Ankur Banerji [Github](https://github.com/ankurbanerji3)
- Boscosylvester Chittilapilly [Github](https://github.com/boscosylvester-john)
- Prasad Kamath [Github](https://github.com/kamathprasad9)
- Shlok Naik [Github](https://github.com/shlokio)
- Tushar Kini [Github](https://github.com/tusharkini)
