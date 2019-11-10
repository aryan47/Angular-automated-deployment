# Angular-automated-deployment
    This script is made to deploy UI in any platform (based on configuration provide by user)
## Features are:
    1.Auto one click deployment
    2.RollBack feature
    3.Backup feature
    4.Tag based deployment
    5.Deployment with npm install
## Upcoming features are:
    1.Notification to concerned people via mail while deployement and in case of failure
    1.Notification to concerned people via mail while rollback
## To use this script
    1.First configure the deployUIConfig.py file with all the required details
    2.For help we can use command:eg: ./deployUI --help (or) ./deployUI -h
    3.To deploy with Tags.eg: ./deployUI --tag v2.3 (or) ./deployUI -t v2.3 
    4.To rollback to previous build. eg: ./deployUI --rollback (or) 
    5.To deploy with npm install. eg: ./deployUI --npm (or) ./deploy -n
