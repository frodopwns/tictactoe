#TicTacToe Prototype

##Prereqs

    sudo apt-get install virtualbox
    sudo pip install ansible

##Running

    vagrant up
    
When the provisioning is finished the Webapp will be available at http://192.168.33.19:5000. The code lives at /vagrant on the VM.

To see the server log:

    vagrant ssh
    screen -x tictactoe

To exit screen without stopping the server press ctrl+a then 'd'.

To run the app manually:

    vagrant ssh #if not already logged into VM
    python /vagrant/run.py
