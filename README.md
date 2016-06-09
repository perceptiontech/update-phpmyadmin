# Update PHPMyAdmin

This is a simple script that allows to auto-update your PHPMyAdmin
installation. Go straight to [step 2](#2.-configure-autoupdate) if you
already have the stable version of 

## 1. Install PHPMyAdmin from the git repository

Go to the folder where you want to install the files within your server
and install download the `STABLE` branch by executing:

```bash
$ git clone --depth=1 -b STABLE https://github.com/phpmyadmin/phpmyadmin.git .
```

Then, install the [composer](https://getcomposer.org/) dependencies for the
project:

```bash
$ composer update --no-dev
```

Then you have to change the `blowfish_secret` of the installation. First,
you have to create the configuration file from the sample configuration
file that is shipped with the project:

```bash
$ cp config.sample.inc.php config.inc.php
```

Then, edit the file add a random string to the string in the line:

```php
$cfg['blowfish_secret'] = '';
```

Now you have PHPMyAdmin configured, and you can setup the script for
automatic updates.

## 2. Configure autoupdate

Clone this repository within a folder that you want. Then, test the
command:

```bash
$ python update-phpmyadmin.py -p /path/to/phpmyadmin/
```

If there is no error, you may configure to run the script once a day by
adding it to your crontab. For example, if you want to execute the
script at 12:05 AM every day:

```
5 12 * * * /path/to/python /path/to/script -p /path/to/phpmyadmin >/dev/null 2>&1
```

That's it! Now, you will always have the latest stable version of
PHPMyAdmin. Take into account that this means that the installation
will also be updated when new major versions are released, and it
may require to reconfigure some things, if needed.

## 3. Command reference

```bash
usage: update-phpmyadmin.py [-h] -p PATH

Command to pull changes from the STABLE branch of PHPMyAdmin

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Absolute path where PHPMyAdmin is installed
```