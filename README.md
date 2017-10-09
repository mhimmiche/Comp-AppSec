# CyberSEED-AppSec
Code for the App Sec competition for CyberSEED 2017


# Setting up the environment

## For Windows 10 Users
### Automatic Setup
I wrote a PowerShell script to automate installation:
1. Download [Python v2.7.3](https://www.python.org/download/releases/2.7.3/) && install it.
2. Open a Power Shell script as administrator
3. Run the following commands:
```powershell
$autoScript=curl https://raw.githubusercontent.com/mhimmiche/RandomScripts/master/pythonSetupScript.ps1
$autoScript.Content >> installScript.ps1
powershell.exe -ExecutionPolicy ByPass -File .\installScript.ps1
```
After running the script, you should have everything set up!
### Manual Setup
#### Installing Python
Ensure that you have the right version of Python installed, we're supposed to use [Python v2.7.3](https://www.python.org/download/releases/2.7.3/).
Once installed, make sure you add it to the Path system variable to make your life easy:
1. Right-click the windows logo (bottom left) && select system
2. In the search bar, type *View Advanced System Settings* and select it
3. Click on *Environment Variables...* 
4. Under *System Variables* look for **Path**
5. Add the path to your Python installation (usually it's something like *C:\Python24*)

#### Installing Packages
In order to use Python's packages, you'll need to install Pip. To do so, open a powershell window (***shift + right-click** anywhere and select **Open Powershell window here***) and copy and paste the following lines:
```powershell
$pipInstall=curl https://bootstrap.pypa.io/get-pip.py
$pipInstall.Content | python.exe
```
You should add the path for Pip as a system variable to make it easier to use, follow the steps above but add path to Pip (usually it's something like *C:\Python24\Scripts*)

## For Linux Users
Just use your package manager, man... Come on... It's pretty straightforward for you


## Running Your Code
In order to run your code:
1. Open up a terminal in your working directory
2. type **python.exe *Name of python script* *Whatever arguments it needs***
Example:

python.exe BackdoorClient.py testAdmin.xml



