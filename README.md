# Power to Choose Notifications

If you live in Texas, you have countless electrical providers to choose from on [Powertochoose.com](http://powertochoose.com).  Sometimes great deals come up when you're ready to switch power providers but you can't be bothered to check them everyday.  In this case, you'll want to download this Python script.

## Installation:

I assume you're using [Anaconda](http://anaconda.org).  If not, please get that (or [Miniconda](https://conda.io/miniconda.html)).

Either Python 2 or 3 is fine.

Then download the essential libraries:

```
conda install numpy pandas selenium
```

```
conda install -c conda-forge phantomjs
```

```
pip install py2ifttt fake_useragent
```



##IFTTT Setup



Then sign up for an [IFTTT](www.ifttt.com) account if you don't already have one.  This program uses IFTTT to manage the notifications.

Create a new applet with the **IF** part using the Webhooks service.  You can select whatever service you want for the **THEN** part later on, but I recommend SMS.

Name your Webhook service whatever you want, but I pick **Powertochoose**.

When creating your **THEN** service, make sure you include the ingredients **Value1**, **Value2**, and **Value3** in the output for the best effect.  These 3 values will tell you the average and min prices for **Today**, **Yesterday**, and the **Last N Days** where you can pick **N** later in the settings.

## Create your settings.cfg file

A settings.cfg template is included in settings.cfg.sample.

Open that and save it as **settings.cfg** in the same directory

On the second line, put the name of your Webhook service after the ":" without any trailing spaces.  For example, if you named it **Powertochoose**, that line should be **IFTTT Webhook Name:Powertochoose**

Next, your **IFTTT Webhook Key** can be found [here](https://ifttt.com/services/maker_webhooks/settings) after you've created your Webhook.  Scroll down to the **URL** and it should be the portion right after **maker.ifttt.com/use/**.

**# of Days to Calc Min/Max Over:** any number is fine, I use 30 (which reports the average and min price over the last 30 days)

**Zipcode**: self explanatory, put your zip code in, make sure it's a valid Texas zip code that Powertochoose supports.



## Running

```
python simple.py
```



## Scheduling

You'll need to schedule it to run once at the same time everyday for this to function correctly, especially the parts that notify you yesterday's prices and the avg and min prices of the last N days.  Refer to your OS for the precise instructions.  In Windows, use the Task Scheduler and create a task that runs the above command from the folder where you cloned this repository.  On a Mac or Linux, run the following and add it to your crontab:

```
crontab -e
```

Then add the following line if you want to run it, say, everyday at 7am:

0 7 * * * **/path/to/python /path/to/simple.py**

Where you replace the bold statements with the respective paths to your python interpreter and simple.py.  NOTE: you may need to dig around to find where the python interpreter for your Anaconda environment is installed!