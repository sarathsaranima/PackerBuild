# PackerBuild

A simple python program that creates an amazon AMI using using packer.py. The program uses 
a configuration file to generate the packer template and bootstraps the image by starting 
an apache server and a sample web page. The user is prompted to enter a tag which would be 
attached to the AMI created. On successful creation of the AMI a new EC2 instance is launched 
with the newly created AMI.
AWS access key and secret keys are configured under 
./generate_ami/resources/vars.json

#### Pre-requisites

1. Python3.2+ installed

#### Installation

1. Open up terminal and navigate to the `Products` folder
2. Execute the following commands:

```cmd

pip install -r requirements.txt

```

#### Verify installation

1. Execute the following command in a CMD window and check if all dependencies are installed.

```cmd
pip freeze
```


#### Running the application
1. Open up terminal and navigate to the `SearchWords` folder
2. Execute the following commands:

```cmd

py -3 run.py
```

This prompts to input a search file and a keyword as below

```
Enter the tag for AMI : awspacker
```

On Completion gives the below message and the AMI and a new EX2 instance 
will be created in the AWS account.

``` 
AMI generation successful xxxxxx
Ec2 instance created successfully with Image xxxxxx
```

