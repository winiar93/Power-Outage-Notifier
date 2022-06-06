## Power-Outage-Notifier
Docker container with a python script that notifies if a power outage.

## How to configure ?

1. Navigate to `https://www.tauron-dystrybucja.pl/wylaczenia#cityArea` 
2. Fill form.


    ![image](https://user-images.githubusercontent.com/70263671/172254266-586ad78d-d4cc-4519-8ac3-b64aecb28487.png)

 3. Before clicking `SEARCH` button enable tool for developer and navigate to `Network` tab.
  
  Find response like `GetOutages?gaid=919578&type=street`. Click on it. On `Headers` tab copy request url and paste into config.py


   ![image](https://user-images.githubusercontent.com/70263671/172254837-4a15da15-afe3-4229-b2fb-dcae1e421ae5.png)

4. In confing.py insert mail receiver, sender and password and also village name from form. 


## How to run it ?

1. Install docker.
2. Using terminal navigate to projekt location.
3. Execute command `docker build -t power_outages_notifier .` ( with dot on the end ).  
4. After that `docker run power_outages_notifier`.
