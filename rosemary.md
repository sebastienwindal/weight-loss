# One time setup instructions:

* git clone https://github.com/sebastienwindal/weight-loss
* install brew: https://brew.sh
* install python2: `brew install python@2`
* install vovpal wabbit: `brew install vowpal-wabbit`

congrats you are now ready to use the thing. You don't need to ever run those thing on this machine, just the generate command part below.

Create a csv file in that folder (for instance rosemary.csv) that uses the following format:

```
Date,MorningWeight,YesterdayFactors
2018-08-03,104.8,start
2018-08-04,105.1,salad badsleep cheese egg halfnhalf:1.5 stress travel
2018-08-05,104.6,bacon soulcycle goodsleep wfh nuts:2 
```

you can check ariel.csv

any keywords goes. It is space separated, you cannot use space so to log "bad sleep" or steak tartare, use no space or an underscore otherwise "bad" and "sleep" will be treated separately which could be a problem for instance if you decide to log "good sleep" too, it makes the keyword "sleep" meaningless.
You can weigh keyworks using :amount like nuts:2 (2 portions of nutes.)

generate the results by typing

`generate rosemary.csv`

this will create a new file: `rosemary.results.csv` that contains the machine learning results.