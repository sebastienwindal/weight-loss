# One time setup instructions:

* install brew: https://brew.sh
* install git: brew install git
* create a folder in the finder where the thig will live, and go there in the terminal (cd blah)
* get the source code: git clone https://github.com/sebastienwindal/weight-loss
* install python2: `brew install python@2`
* install vovpal wabbit: `brew install vowpal-wabbit`

congrats you are now ready to use the thing. You don't need to ever run that on this machine, just the generate command part below.

# daily usage:

Create a csv file in that folder (for instance rosemary.csv) that uses the following format and keep updating it everyday:

```
Date,MorningWeight,YesterdayFactors
2018-08-03,104.8,start
2018-08-04,105.5,salad badsleep cheese egg halfnhalf:1.5 stress travel croissant icecream
2018-08-05,104.6,bacon soulcycle goodsleep wfh nuts:2 salad
```

you can check ariel.csv for inspiration.

The YesterdayFactors is just a list (space separated) of text keywords. Any keywords goes. The artifical intelligence does not know and care what it is, it is all based on finding corelation between keywords and weight variations. Again, the list is space separated, so to log "bad sleep" or "steak tartare" (yum), use no space (steaktartare) or an underscore (bad_sleep) otherwise "bad" and "sleep" will be treated separately which could be a problem for instance if you decide to log "good sleep" too, it makes the keyword "sleep" meaningless.
You can weigh keyworks if you want by appending an number after a :, for instance nuts:2 (2 portions of nuts.) The default weight of a keyword is 1.

You generate the results by typing:

`generate rosemary.csv`


this will create a new file: `rosemary.results.csv` that contains the machine learning results.

To open in numbers, just type `open rosemary.results.csv`.



# terminal usage:

in finder, applicatinos -> Utilities, open Terminal

inside the terminal:

* cd Desktop
* cd Seb (hit tab for auto complete)

some commands:
- cd (change directory)
- ls (list all files in current directory)
