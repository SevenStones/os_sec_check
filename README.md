# os_sec_check
Base of a framework for testing PCI-DSS metrics for Windows

Note virtualenv requirements are in requirements.txt in the git root, and there are some server-side Powershell scripts.

The Windows connection to WinRM was tested with "basic authentication" and Windows 2012 Server R2.

settings.py is left in debug=yes, and you will need to edit "AllowedHosts".

Windows target has a username/password and IP address set in tasks.py.

Currently the UI is all default Django.

See Django tutorials for starting a nrew project and then deploying a new app for that project.

Coming soon: 
- more Windows tests.
- testing logic moved away from target-hosted Powershell scripts to python coded tests, not hosted on the target.
- processing of output from the server (pass or fail automatically based on Python-coded logic.
- Linux tests.
- management of targets.
