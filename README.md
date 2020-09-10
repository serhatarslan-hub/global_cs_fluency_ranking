
# Introduction

This repository contains the code for the paper
"Estimating Global Patterns in Learning Quality Using Global Search Trends" by
Serhat Arslan, Mo Tiwari, and Chris Piech, which appeared in Learning at Scale
(L@S) 2020.

If you use code from this repository, please cite the following paper:

```
@inproceedings{arslan2020cslearning,
  title={Estimating Global Patterns in Learning Quality Using Global Search Trends},
  author={Arslan, Serhat and Tiwari, Mo and Piech, Chris},
  year={2020},
  publisher={Learning at Scale},
}
```

# Requirements

The code requires Python 3.7.4 or above. The required python packages can be
installed via `pip install -r requirements.txt`.

This project also requires chromedriver, specifically for Chrome v.75 on MacOS.
Once installed, chromedriver must be added to your environment's `PATH` variable.

For further instructions and troubleshooting, please see:
https://saucelabs.com/resources/articles/getting-started-with-webdriver-in-python-on-osx

# Explanation of Files
- `requirements.txt` contains the necessary python dependencies; install with
`pip install -r requirements.txt`
- `constants.py` contains the parameters for querying Google trends, including
the string URL for each query
- `downloader.py` contains the code to loop through each search query on Google
Trends and automatically download the statistics used in the computation of
CSLI-s scores
- `GT_Analysis_All_Final.xlsx` contains the statistics downloaded from Google
Trends using `downloader.py`, which are used in the computation of CLSI-s scores
- `CLSI_scores_2014_to_2018.csv` contains the computed CLSI-s scores
- `cluster_data.py` contains the code to plot countries' embeddings,
both via an arbitrary 2D embedding and via t-SNE (typically applied to the CSLI scores)
