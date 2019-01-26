# random_football_score_generator
Randomly generate a set of football scores. Uses full time scores from English 
top 4 tiers between 1993-2018 to generate realistic scores.

## Requirements and Installation

Requires python3. No additional modules should be required.

Retrieve the project from github:

    git clone https://github.com/gantzgraf/random_football_score_generator.git

Alternatively, use the 'Clone or download' button on the github page to
download a zip and extract the zip file.

After cloning the project or downloading and extracting the zip file, change
directory to the project folder and run the score_generator script:

    cd random_football_score_generator
    ./score_generator.py

To view options use the -h/--help flag:

    ./score_generator.py -h 

## Options

    usage: score_generator.py [-h] [-n NUMBER] [-y [1993-2018] [[1993-2018] ...]]
                              [-t [1-4] [[1-4] ...]] [-s]

    Generate a random set of football (soccer) scores based on historical data
    from the English first four divisions.

    optional arguments:
      -h, --help            show this help message and exit
      -n NUMBER, --number NUMBER
                            Number of scores to generate. Default=10
      -y [1993-2018] [[1993-2018] ...], --years [1993-2018] [[1993-2018] ...]
                            One or more years (seasons) to read data from.
                            Defaults to all available years (1993-2018). The
                            year(s) given corresponds to the season starting in
                            the given year - e.g. 2017 correponds to the season
                            starting August 2017 and ending May 2018.
      -t [1-4] [[1-4] ...], --tiers [1-4] [[1-4] ...]
                            Which tiers/divisions to read data from. Defaults to
                            all available tiers (1-4).
      -s, --scorelines      Pick from results from full scorelines. By default
                            goals for home and away sides are randomly drawn
                            separately from the historical data. If you prefer
                            to randomly pull full scorelines use this option.
