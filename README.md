# callcamping
Automated notifications for camping site(s) availability

## Description
The core script is outlined in this repo:
https://github.com/banool/recreation-gov-campsite-checker

This program will:
* Identify all weekends (and US holiday weekends) in a certain date range. Default: from today's date until 6 months from today. 
* Hit the recreation.gov API endpoints for availability using valid dates for a list of pre-defined recreation.gov camping sites
* Output results and compare them to the most recent previous run
* If any changes are identified, a notification will be pushed via pushbullet with the new results
* Executable script is an example. User can run this on a time interval using launchcontrol or similar. 

## Pre-requisites
In order to run this program, you will need:
* Pushbullet API key
* Recreation.gov park IDs (drop into the parks.txt file)

## Usage
* Install Conda and Python
* Create a new virtual environment
* Install packages in requirements.txt
* Make any desired changes to weekends.py script. 

*For example, the input date range:*
```
# start=(sys.argv[1])
start=str(datetime.date.today())
# end=(sys.argv[2])
end=str(datetime.date.today() + relativedelta(months=6))
```
*Valid days (0 is Monday, 6 is Sunday):*
```
if ((start_date + datetime.timedelta(days=x)).isoweekday() >= 5 or (start_date + datetime.timedelta(days=x)).isoweekday() == 1)}
```
*Number of nights for regular weekends vs US holiday weekends:*
```
if Starting_Date in us_holidays or Ending_Date in us_holidays:
			nights = 3
		else:
			nights = 2
```
* Run the script specifying function arguments in the following order: weekends.py | pushcamp.py YOUR_PUSHBULLET_API_KEY. Example:

```
/Users/saket/opt/anaconda3/envs/camping_env/bin/python3.8 /Users/saket/Downloads/recreation-gov-campsite-checker-master/weekends.py | /Users/saket/opt/anaconda3/envs/camping_env/bin/python3.8 /Users/saket/Downloads/recreation-gov-campsite-checker-master/pushcamp.py YOUR_PUSHBULLET_API_KEY
```
* Note the weekends.py will automatically call the camping.py script and feed in all necessary variables. Results will be shown in terminal 
* Note the pushcamp.py script will compare compare the most recent results (old_available.txt) with the newest results and then push the updated list (Master_Availability.txt) via Pushbullet and also update the old_available.txt file

## Bonus
It can be helpful to package the terminal commands into an excutable shell command. An example is provided (callcamping.sh). Make appropriate edits as explained in the comments on that file. In order to create the executable file, you'll want to run this in the terminal: 

```
chmod a+x PATH_TO_CALLCAMPING
```
At this point, you can run this shell command on a regular time interval using launchcontrol, for example. 
